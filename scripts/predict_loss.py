import joblib
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import LabelEncoder

# -----------------------------------
# 1. Load trained model
# -----------------------------------
BASE_DIR   = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "loss_prediction_model.pkl"

model = joblib.load(MODEL_PATH)

# -----------------------------------
# 2. Manual encoders (same as training)
# -----------------------------------
attack_type_encoder   = LabelEncoder()
attack_vector_encoder = LabelEncoder()
system_encoder        = LabelEncoder()
security_encoder      = LabelEncoder()

attack_type_encoder.fit(["Ransomware", "Phishing", "DDoS", "Malware"])
attack_vector_encoder.fit(["Email", "Network", "USB"])
system_encoder.fit(["EHR", "Billing", "PACS"])
security_encoder.fit(["Low", "Medium", "High"])

# -----------------------------------
# 3. Example new input
# -----------------------------------
new_data = {
    "attack_type":             "Ransomware",
    "attack_vector":           "Email",
    "system_affected":         "EHR",
    "downtime_hours":          7,
    "records_compromised":     15000,
    "detection_delay_minutes": 60,
    "security_level":          "Medium"
}

# -----------------------------------
# 4. Encode input into DataFrame
# -----------------------------------
X_new = pd.DataFrame([{
    "attack_type":             attack_type_encoder.transform([new_data["attack_type"]])[0],
    "attack_vector":           attack_vector_encoder.transform([new_data["attack_vector"]])[0],
    "system_affected":         system_encoder.transform([new_data["system_affected"]])[0],
    "downtime_hours":          new_data["downtime_hours"],
    "records_compromised":     new_data["records_compromised"],
    "detection_delay_minutes": new_data["detection_delay_minutes"],
    "security_level":          security_encoder.transform([new_data["security_level"]])[0]
}])

# -----------------------------------
# 5. Predict operational loss
# -----------------------------------
predicted_loss = model.predict(X_new)[0]

# -----------------------------------
# 6. Risk classification (matches views.py thresholds)
# -----------------------------------
if predicted_loss < 2_000_000:
    risk = "Low Risk"
elif predicted_loss < 8_000_000:
    risk = "Medium Risk"
else:
    risk = "High Risk"

# -----------------------------------
# 7. Output
# -----------------------------------
print("Predicted Operational Loss: ₹", round(predicted_loss, 2))
print("Risk Level:", risk)