from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

import os
import joblib
import numpy as np
import shap

from .models import CyberScenario
from django.db.models import Avg, Max


import matplotlib
matplotlib.use("Agg")   # Prevents GUI errors in Django

import matplotlib.pyplot as plt


# ---------------- LOAD MODEL ----------------

# Load ML model once when server starts
model = joblib.load("models/loss_prediction_model.pkl")
attack_map = {
"Ransomware":0,
"Phishing":1,
"DDoS":2,
"Malware":3
}

vector_map = {
"Email":0,
"Network":1,
"USB":2
}

system_map = {
"EHR":0,
"Billing":1,
"PACS":2
}

security_map = {
"Low":0,
"Medium":1,
"High":2
}

# Create SHAP explainer
explainer = shap.TreeExplainer(model)


# ---------------- LOGIN PAGE ----------------

def login_page(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


# ---------------- HOME PAGE ----------------

def home(request):
    return render(request, 'home.html')


# ---------------- PREDICTION ----------------
from django.http import JsonResponse

def predict(request):

    if request.method == "POST":

        # -------- GET FORM DATA --------

        attack_str = request.POST.get('attack')
        vector_str = request.POST.get('vector')
        system_str = request.POST.get('system')
        security_str = request.POST.get('security')

        downtime = int(request.POST.get('downtime', 0))
        delay = int(request.POST.get('delay', 0))
        records = int(request.POST.get('records', 0))

        # -------- MAP VALUES --------

        attack = attack_map[attack_str]
        vector = vector_map[vector_str]
        system = system_map[system_str]
        security = security_map[security_str]

        # -------- MODEL INPUT --------

        data = np.array([[attack, vector, system, downtime, records, delay, security]])

        prediction = float(model.predict(data)[0])

        # -------- RISK CLASSIFICATION --------

        if prediction < 200000:
            risk = "Low Impact"
        elif prediction < 600000:
            risk = "Medium Impact"
        else:
            risk = "High Impact"

        # -------- SAVE SCENARIO --------

        CyberScenario.objects.create(
            attack_type=attack_str,
            system=system_str,
            downtime=downtime,
            records=records,
            predicted_loss=prediction
        )

        # -------- SHAP EXPLAINABILITY --------

        shap_values = explainer.shap_values(data)

        shap_data = {
            "Downtime": round(float(shap_values[0][3]),2),
            "Records": round(float(shap_values[0][4]),2),
            "Detection Delay": round(float(shap_values[0][5]),2)
        }

        # -------- JSON RESPONSE FOR DASHBOARD --------

        return JsonResponse({
            "prediction": round(prediction,2),
            "risk": risk,
            "shap": shap_data
        })

    return JsonResponse({"error":"Invalid request"})

  
def dashboard(request):

    total = CyberScenario.objects.count()

    avg_loss = CyberScenario.objects.aggregate(Avg("predicted_loss"))["predicted_loss__avg"]

    highest = CyberScenario.objects.aggregate(Max("predicted_loss"))["predicted_loss__max"]

    return render(request,"dashboard.html",{
        "total":total,
        "avg_loss":round(avg_loss,2) if avg_loss else 0,
        "highest":highest
    })

def simulator(request):

    return render(request,"simulator.html")


def analytics(request):

    return render(request,"analytics.html")


def reports(request):

    reports = CyberScenario.objects.all().order_by("-created_at")

    return render(request,"reports.html",{"reports":reports})