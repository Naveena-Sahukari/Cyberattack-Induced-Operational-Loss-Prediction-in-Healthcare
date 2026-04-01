from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

import joblib
import json
import numpy as np
import pandas as pd
import shap

from .models import CyberScenario
from django.db.models import Avg, Max, Count

# ---------------- LOAD MODEL ----------------

model = joblib.load("models/loss_prediction_model.pkl")

attack_map   = {"Ransomware": 0, "Phishing": 1, "DDoS": 2, "Malware": 3}
vector_map   = {"Email": 0, "Network": 1, "USB": 2}
system_map   = {"EHR": 0, "Billing": 1, "PACS": 2}
security_map = {"Low": 0, "Medium": 1, "High": 2}

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


# ---------------- PREDICT ----------------

def predict(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"})

    try:
        attack_str   = request.POST.get('attack')
        vector_str   = request.POST.get('vector')
        system_str   = request.POST.get('system')
        security_str = request.POST.get('security')
        downtime     = int(request.POST.get('downtime', 0))
        delay        = int(request.POST.get('delay', 0))
        records      = int(request.POST.get('records', 0))

        data = pd.DataFrame([{
            "attack_type":             attack_map.get(attack_str, 0),
            "attack_vector":           vector_map.get(vector_str, 0),
            "system_affected":         system_map.get(system_str, 0),
            "downtime_hours":          downtime,
            "records_compromised":     records,
            "detection_delay_minutes": delay,
            "security_level":          security_map.get(security_str, 0)
        }])

        prediction = float(model.predict(data)[0])

        # Risk
        if prediction < 2_000_000:
            risk = "Low Risk"
        elif prediction < 8_000_000:
            risk = "Medium Risk"
        else:
            risk = "High Risk"

        # Recommendations
        recommendations = []
        if downtime > 20:
            recommendations.append("Activate backup systems immediately to restore operations")
        if records > 20_000:
            recommendations.append("Notify affected patients and report to authorities as required")
        if security_str == "Low":
            recommendations.append("Upgrade security controls and conduct an immediate security audit")
        if delay > 60:
            recommendations.append("Improve threat detection speed — deploy real-time monitoring tools")
        if attack_str == "Ransomware":
            recommendations.append("Isolate infected systems immediately to prevent lateral spread")
        if attack_str == "Phishing":
            recommendations.append("Conduct emergency staff awareness training and reset credentials")
        if attack_str == "DDoS":
            recommendations.append("Engage DDoS mitigation services and activate failover systems")
        if system_str == "EHR":
            recommendations.append("Switch to paper-based workflows until EHR system is restored")
        if system_str == "Billing":
            recommendations.append("Pause billing operations and notify finance and compliance teams")
        if not recommendations:
            recommendations.append("Routine monitoring — no immediate critical action required")

        # Save to DB
        CyberScenario.objects.create(
            attack_type=attack_str,
            system=system_str,
            downtime=downtime,
            records=records,
            predicted_loss=prediction
        )

        # SHAP
        shap_values = explainer.shap_values(data)
        shap_data = {
            "Downtime":        round(float(shap_values[0][3]), 2),
            "Records":         round(float(shap_values[0][4]), 2),
            "Detection Delay": round(float(shap_values[0][5]), 2),
            "Attack Type":     round(float(shap_values[0][0]), 2),
            "Security Level":  round(float(shap_values[0][6]), 2),
        }

        return JsonResponse({
            "prediction":      round(prediction, 2),
            "risk":            risk,
            "shap":            shap_data,
            "recommendations": recommendations
        })

    except Exception as e:
        print("ERROR:", str(e))
        return JsonResponse({"error": str(e)})


# ---------------- DASHBOARD ----------------

def dashboard(request):
    total      = CyberScenario.objects.count()
    avg_result = CyberScenario.objects.aggregate(Avg("predicted_loss"))
    max_result = CyberScenario.objects.aggregate(Max("predicted_loss"))
    avg_loss   = avg_result["predicted_loss__avg"]
    highest    = max_result["predicted_loss__max"]
    reports    = CyberScenario.objects.all().order_by("-created_at")[:10]

    return render(request, "dashboard.html", {
        "total":    total,
        "avg_loss": round(avg_loss, 2) if avg_loss else 0,
        "highest":  round(highest, 2)  if highest  else 0,
        "reports":  reports,
    })


# ---------------- SIMULATOR ----------------

def simulator(request):
    return render(request, "simulator.html")


# ---------------- ANALYTICS ----------------

def analytics(request):
    scenarios = CyberScenario.objects.all()

    # 1. Attack type distribution (count)
    attack_qs     = scenarios.values("attack_type").annotate(count=Count("attack_type")).order_by("attack_type")
    attack_labels = [a["attack_type"] for a in attack_qs]
    attack_counts = [a["count"]       for a in attack_qs]

    # 2. Average loss by attack type
    aloss_qs      = scenarios.values("attack_type").annotate(avg=Avg("predicted_loss")).order_by("attack_type")
    aloss_labels  = [a["attack_type"]      for a in aloss_qs]
    aloss_values  = [round(a["avg"] or 0)  for a in aloss_qs]

    # 3. Average loss by system
    sys_qs        = scenarios.values("system").annotate(avg=Avg("predicted_loss")).order_by("system")
    sys_labels    = [s["system"]           for s in sys_qs]
    sys_values    = [round(s["avg"] or 0)  for s in sys_qs]

    # 4. Loss vs downtime scatter
    scatter_raw    = list(scenarios.values("downtime", "predicted_loss"))
    scatter_points = [{"x": s["downtime"], "y": round(s["predicted_loss"] or 0)} for s in scatter_raw]

    # 5. Risk level breakdown (pie)
    all_losses  = list(scenarios.values_list("predicted_loss", flat=True))
    risk_low    = sum(1 for l in all_losses if l  < 2_000_000)
    risk_medium = sum(1 for l in all_losses if 2_000_000 <= l < 8_000_000)
    risk_high   = sum(1 for l in all_losses if l >= 8_000_000)

    return render(request, "analytics.html", {
        "attack_labels":  json.dumps(attack_labels),
        "attack_counts":  json.dumps(attack_counts),
        "aloss_labels":   json.dumps(aloss_labels),
        "aloss_values":   json.dumps(aloss_values),
        "sys_labels":     json.dumps(sys_labels),
        "sys_values":     json.dumps(sys_values),
        "scatter_points": json.dumps(scatter_points),
        "risk_counts":    json.dumps([risk_low, risk_medium, risk_high]),
        "total":          scenarios.count(),
    })


# ---------------- REPORTS ----------------

def reports(request):
    all_reports = CyberScenario.objects.all().order_by("-created_at")

    # FIX: annotate risk label and class in Python so the template
    # doesn't need invalid nested {% if/elif/with %} blocks
    for r in all_reports:
        if r.predicted_loss >= 8_000_000:
            r.risk_label = "High Risk"
            r.risk_class = "risk-high"
        elif r.predicted_loss >= 2_000_000:
            r.risk_label = "Medium Risk"
            r.risk_class = "risk-medium"
        else:
            r.risk_label = "Low Risk"
            r.risk_class = "risk-low"

    return render(request, "reports.html", {"reports": all_reports})