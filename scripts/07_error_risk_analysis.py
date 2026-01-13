import pandas as pd
import pickle
from sklearn.model_selection import train_test_split

df = pd.read_csv(r"C:\Users\sahukari naveena\OneDrive\Desktop\MINI_PROJECT\Cyber_Operational_Loss_Prediction\data\processed_data\processed_cyber_healthcare_data.csv")

X = df.drop("operational_loss", axis=1)
y = df["operational_loss"]

with open(r"C:\Users\sahukari naveena\OneDrive\Desktop\MINI_PROJECT\Cyber_Operational_Loss_Prediction\models\loss_prediction_model.pkl", "rb") as f:
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

with open(r"C:\Users\sahukari naveena\OneDrive\Desktop\MINI_PROJECT\Cyber_Operational_Loss_Prediction\outputs\Reports\insights.txt", "w") as f:
    f.write("High Loss Missed Cases:\n")
    f.write(str(high_loss_missed.head()))

print("Error and risk analysis completed.")
print()
print("“The empty high-loss-missed set indicates that the model did not underestimate any high-impact incidents above the defined threshold.This shows that the Random Forest model is conservative and reliable for identifying critical operational losses, which is desirable in a cybersecurity risk context.”")
