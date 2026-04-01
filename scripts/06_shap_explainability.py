import pandas as pd
import shap
import pickle
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------------------------
# Paths
# ----------------------------------
BASE_DIR   = Path(__file__).resolve().parent.parent
DATA_PATH  = BASE_DIR / "data" / "processed_data" / "processed_cyber_healthcare_data.csv"
MODEL_PATH = BASE_DIR / "models" / "loss_prediction_model.pkl"
OUTPUT_DIR = BASE_DIR / "outputs" / "graphs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ----------------------------------
# Load data and model
# ----------------------------------
df = pd.read_csv(DATA_PATH)
X  = df.drop("operational_loss", axis=1)

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# ----------------------------------
# SHAP analysis
# ----------------------------------
explainer   = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# 1. Summary plot (beeswarm) — shows all features ranked by importance
shap.summary_plot(shap_values, X, show=False)
plt.tight_layout()

# FIX: was saving to "loss_vs_downtime.png" — overwrote the downtime scatter plot
# Now correctly saved to its own file
plt.savefig(OUTPUT_DIR / "shap_summary_plot.png", dpi=150, bbox_inches="tight")
plt.close()

# 2. Bar plot — mean absolute SHAP values (cleaner for presentations)
shap.summary_plot(shap_values, X, plot_type="bar", show=False)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "shap_bar_plot.png", dpi=150, bbox_inches="tight")
plt.close()

print("SHAP explainability plots saved:")
print(f"  - {OUTPUT_DIR / 'shap_summary_plot.png'}")
print(f"  - {OUTPUT_DIR / 'shap_bar_plot.png'}")