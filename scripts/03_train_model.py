import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# -----------------------------------
# 1. Load processed dataset
# -----------------------------------
df = pd.read_csv(
    r"C:\Users\sahukari naveena\OneDrive\Desktop\Cyber_Operational_Loss_Prediction\data\processed_data\processed_cyber_healthcare_data.csv"
)

# -----------------------------------
# 2. Separate input and target
# -----------------------------------
X = df.drop("operational_loss", axis=1)
y = df["operational_loss"]

# -----------------------------------
# 3. Train-test split
# -----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------------
# 4. Train Linear Regression (baseline)
# -----------------------------------
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

print("Linear Regression Results")
print("MAE:", mean_absolute_error(y_test, lr_pred))
print("RMSE:", (mean_squared_error(y_test, lr_pred)) ** 0.5)
print("R2:", r2_score(y_test, lr_pred))

print("-" * 40)

# -----------------------------------
# 5. Train Random Forest (final model)
# -----------------------------------
rf_model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)
rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

print("Random Forest Results")
print("MAE:", mean_absolute_error(y_test, rf_pred))
print("RMSE:", (mean_squared_error(y_test, rf_pred)) ** 0.5)
print("R2:", r2_score(y_test, rf_pred))

# -----------------------------------
# 6. Save the trained model
# -----------------------------------
with open(
    r"C:\Users\sahukari naveena\OneDrive\Desktop\Cyber_Operational_Loss_Prediction\models\loss_prediction_model.pkl",
    "wb"
) as f:
    pickle.dump(rf_model, f)

print("\nModel saved as models/loss_prediction_model.pkl")
