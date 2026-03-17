from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

import joblib
import numpy as np
import pandas as pd
import shap

from .models import CyberScenario
from django.db.models import Avg, Max

# ---------------- LOAD MODEL ----------------

model = joblib.load("models/loss_prediction_model.pkl")

attack_map = {
    "Ransomware": 0,
    "Phishing": 1,
    "DDoS": 2,
    "Malware": 3
}

vector_map = {
    "Email": 0,
    "Network": 1,
    "USB": 2
}

system_map = {
    "EHR": 0,
    "Billing": 1,
    "PACS": 2
}

security_map = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

explainer = shap.TreeExplainer(model)


# ---------------- LOGIN ----------------

def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


# ---------------- HOME ----------------

def home(request):
    return render(request, 'home.html')


# ---------------- PREDICT (FIXED) ----------------

def predict(request):

    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"})

    try:
        # -------- GET DATA --------

        attack_str = request.POST.get('attack')
        vector_str = request.POST.get('vector')
        system_str = request.POST.get('system')
        security_str = request.POST.get('security')

        downtime = int(request.POST.get('downtime', 0))
        delay = int(request.POST.get('delay', 0))
        records = int(request.POST.get('records', 0))

        # -------- MAP VALUES --------

        attack = attack_map.get(attack_str, 0)
        vector = vector_map.get(vector_str, 0)
        system = system_map.get(system_str, 0)
        security = security_map.get(security_str, 0)

        # -------- CREATE INPUT (VERY IMPORTANT FIX) --------

        data = pd.DataFrame([{
            "attack_type": attack,
            "attack_vector": vector,
            "system_affected": system,
            "downtime_hours": downtime,
            "records_compromised": records,
            "detection_delay_minutes": delay,
            "security_level": security
        }])

        # -------- PREDICT --------

        prediction = float(model.predict(data)[0])

        print("INPUT:", data)
        print("PREDICTION:", prediction)

        # -------- RISK --------

        if prediction < 2000000:
            risk = "Low Risk"
        elif prediction < 8000000:
            risk = "Medium Risk"
        else:
            risk = "High Risk"

        # -------- SAVE TO DB --------

        CyberScenario.objects.create(
            attack_type=attack_str,
            system=system_str,
            downtime=downtime,
            records=records,
            predicted_loss=prediction
        )

        # -------- SHAP --------

        shap_values = explainer.shap_values(data)

        shap_data = {
            "Downtime": round(float(shap_values[0][3]), 2),
            "Records": round(float(shap_values[0][4]), 2),
            "Detection Delay": round(float(shap_values[0][5]), 2)
        }

        # -------- RESPONSE --------

        return JsonResponse({
            "prediction": round(prediction, 2),
            "risk": risk,
            "shap": shap_data
        })

    except Exception as e:
        print("ERROR:", str(e))
        return JsonResponse({"error": str(e)})


# ---------------- DASHBOARD ----------------

def dashboard(request):

    total = CyberScenario.objects.count()

    avg_loss = CyberScenario.objects.aggregate(
        Avg("predicted_loss")
    )["predicted_loss__avg"]

    highest = CyberScenario.objects.aggregate(
        Max("predicted_loss")
    )["predicted_loss__max"]

    return render(request, "dashboard.html", {
        "total": total,
        "avg_loss": round(avg_loss, 2) if avg_loss else 0,
        "highest": highest if highest else 0
    })


# ---------------- SIMULATOR ----------------

def simulator(request):
    return render(request, "simulator.html")


# ---------------- ANALYTICS ----------------

def analytics(request):
    return render(request, "analytics.html")


# ---------------- REPORTS ----------------

def reports(request):
    reports = CyberScenario.objects.all().order_by("-created_at")
    return render(request, "reports.html", {"reports": reports})