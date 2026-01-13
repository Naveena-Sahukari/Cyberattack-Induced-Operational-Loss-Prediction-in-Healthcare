import pandas as pd
import shap
import pickle
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\sahukari naveena\OneDrive\Desktop\MINI_PROJECT\Cyber_Operational_Loss_Prediction\data\processed_data\processed_cyber_healthcare_data.csv")


X = df.drop("operational_loss", axis=1)

with open("models/loss_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

shap.summary_plot(shap_values, X, show=False)
plt.savefig(r"C:\Users\sahukari naveena\OneDrive\Desktop\MINI_PROJECT\Cyber_Operational_Loss_Prediction\outputs\graphs\loss_vs_downtime.png")
plt.close()

print("SHAP explainability plot generated.")
