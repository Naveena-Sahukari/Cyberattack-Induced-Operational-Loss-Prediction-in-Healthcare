import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.model_selection import train_test_split
from pathlib import Path

# -----------------------------------
# 0. Define paths safely
# -----------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed_data" / "processed_cyber_healthcare_data.csv"
MODEL_PATH = BASE_DIR / "models" / "loss_prediction_model.pkl"
OUTPUT_DIR = BASE_DIR / "outputs" / "graphs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------------
# 1. Load processed data
# -----------------------------------
if not DATA_PATH.exists():
    raise FileNotFoundError(f"Dataset not found at: {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

X = df.drop("operational_loss", axis=1)
y = df["operational_loss"]

# -----------------------------------
# 2. Load trained model
# -----------------------------------
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# -----------------------------------
# 3. Train-test split (same as training)
# -----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

y_pred = model.predict(X_test)

# -----------------------------------
# 4. Plot 1: Actual vs Predicted Loss
# -----------------------------------
plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Operational Loss")
plt.ylabel("Predicted Operational Loss")
plt.title("Actual vs Predicted Operational Loss")
plt.savefig(OUTPUT_DIR / "actual_vs_predicted.png")
plt.close()

# -----------------------------------
# 5. Plot 2: Loss vs Downtime
# -----------------------------------
plt.figure()
plt.scatter(df["downtime_hours"], df["operational_loss"])
plt.xlabel("Downtime (hours)")
plt.ylabel("Operational Loss")
plt.title("Operational Loss vs Downtime")
plt.savefig(OUTPUT_DIR / "loss_vs_downtime.png")
plt.close()

# -----------------------------------
# 6. Plot 3: Attack Type Distribution
# -----------------------------------
attack_counts = df["attack_type"].value_counts()

plt.figure()
attack_counts.plot(kind="bar")
plt.xlabel("Attack Type (Encoded)")
plt.ylabel("Frequency")
plt.title("Attack Type Distribution")
plt.savefig(OUTPUT_DIR / "attack_distribution.png")
plt.close()

print("Graphs saved successfully in outputs/graphs/")
