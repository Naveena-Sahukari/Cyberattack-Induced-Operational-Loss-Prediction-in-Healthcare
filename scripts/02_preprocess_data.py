import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from pathlib import Path

# ----------------------------------
# 1. Resolve paths safely (FIXES VS CODE ISSUE)
# ----------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = BASE_DIR / "raw_data" / "cyber_healthcare_data.csv"
PROCESSED_DATA_PATH = BASE_DIR / "processed_data" / "processed_cyber_healthcare_data.csv"

# ----------------------------------
# 2. Load dataset
# ----------------------------------
df = pd.read_csv(RAW_DATA_PATH)

print("Original Data:")
print(df.head())

# ----------------------------------
# 3. Encode categorical columns
# ----------------------------------
categorical_cols = [
    "attack_type",
    "attack_vector",
    "system_affected",
    "security_level"
]

label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# ----------------------------------
# 4. Separate input (X) and output (y)
# ----------------------------------
X = df.drop("operational_loss", axis=1)
y = df["operational_loss"]

# ----------------------------------
# 5. Scale features
# ----------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ----------------------------------
# 6. Save processed data
# ----------------------------------
processed_df = pd.DataFrame(X_scaled, columns=X.columns)
processed_df["operational_loss"] = y.values

processed_df.to_csv(PROCESSED_DATA_PATH, index=False)

print("\nPreprocessing completed successfully.")
print(f"Processed file saved at: {PROCESSED_DATA_PATH}")
