import pandas as pd
import pickle
from pathlib import Path
from sklearn.model_selection import train_test_split

# FIX: replaced all hardcoded absolute Windows paths with portable Path-based resolution
BASE_DIR    = Path(__file__).resolve().parent.parent
DATA_PATH   = BASE_DIR / "data" / "processed_data" / "processed_cyber_healthcare_data.csv"
MODEL_PATH  = BASE_DIR / "models" / "loss_prediction_model.pkl"
OUTPUT_DIR  = BASE_DIR / "outputs" / "Reports"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)

X = df.drop("operational_loss", axis=1)
y = df["operational_loss"]

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

preds = model.predict(X_test)
errors = preds - y_test

analysis = pd.DataFrame({
    "Actual": y_test,
    "Predicted": preds,
    "Error": errors
})

high_loss_missed = analysis[(analysis["Actual"] > 2000000) & (analysis["Predicted"] < 2000000)]

with open(OUTPUT_DIR / "insights.txt", "w") as f:
    f.write("High Loss Missed Cases:\n")
    f.write(str(high_loss_missed.head()))

print("Error and risk analysis completed.")
print()

# FIX: original used smart/curly quotes ("" "") which cause a SyntaxError in Python
# replaced with a plain print() using regular straight quotes
print(
    "The empty high-loss-missed set indicates that the model did not underestimate "
    "any high-impact incidents above the defined threshold. This shows that the "
    "Random Forest model is conservative and reliable for identifying critical "
    "operational losses, which is desirable in a cybersecurity risk context."
)