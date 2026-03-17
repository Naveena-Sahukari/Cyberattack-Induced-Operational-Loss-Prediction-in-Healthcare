import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# LOAD DATA
df = pd.read_csv("data/cyber_healthcare_data.csv")

# ENCODING
le1 = LabelEncoder()
le2 = LabelEncoder()
le3 = LabelEncoder()
le4 = LabelEncoder()

df["attack_type"] = le1.fit_transform(df["attack_type"])
df["attack_vector"] = le2.fit_transform(df["attack_vector"])
df["system_affected"] = le3.fit_transform(df["system_affected"])
df["security_level"] = le4.fit_transform(df["security_level"])

# FEATURES
X = df[[
    "attack_type",
    "attack_vector",
    "system_affected",
    "downtime_hours",
    "records_compromised",
    "detection_delay_minutes",
    "security_level"
]]

y = df["operational_loss"]

# TRAIN
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor(
    n_estimators=300,
    max_depth=None,
    random_state=42
)

model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

# SAVE MODEL
joblib.dump(model, "models/loss_prediction_model.pkl")

print("✅ Model saved")