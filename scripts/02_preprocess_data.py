import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from pathlib import Path

# ----------------------------------
# 1. Resolve paths safely
# ----------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# FIX: was BASE_DIR / "cyber_healthcare_data.csv"
# The file is saved inside the data/ folder by create_dataset.py
RAW_DATA_PATH       = BASE_DIR / "data" / "cyber_healthcare_data.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed_data" / "processed_cyber_healthcare_data.csv"

# Create processed_data folder if it doesn't exist
PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

# ----------------------------------
# 2. Load dataset
# ----------------------------------
if not RAW_DATA_PATH.exists():
    raise FileNotFoundError(f"Raw dataset not found at: {RAW_DATA_PATH}\nRun create_dataset.py first.")

df = pd.read_csv(RAW_DATA_PATH)

print("Original Data Shape:", df.shape)
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
    print(f"  {col} classes: {le.classes_}")

# ----------------------------------
# 4. Separate features and target
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