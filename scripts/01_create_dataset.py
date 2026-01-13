import pandas as pd
import random

# -----------------------------
# 1. Define possible values
# -----------------------------
attack_types = ["Ransomware", "Phishing", "DDoS", "Malware"]
attack_vectors = ["Email", "Network", "USB"]
systems_affected = ["EHR", "Billing", "PACS"]
security_levels = ["Low", "Medium", "High"]

# -----------------------------
# 2. Cost assumptions (document this)
# -----------------------------
COST_PER_HOUR_DOWNTIME = 200000      # ₹ per hour
COST_PER_RECORD = 500               # ₹ per record

# -----------------------------
# 3. Generate synthetic data
# -----------------------------
data = []

for _ in range(100):  # generate 100 incidents
    attack_type = random.choice(attack_types)
    attack_vector = random.choice(attack_vectors)
    system = random.choice(systems_affected)
    
    downtime = random.randint(1, 12)                  # hours
    records = random.randint(0, 30000)                 # records
    detection_delay = random.randint(10, 120)          # minutes
    security = random.choice(security_levels)

    # Operational loss calculation
    operational_loss = (downtime * COST_PER_HOUR_DOWNTIME) + \
                       (records * COST_PER_RECORD)

    data.append([
        attack_type,
        attack_vector,
        system,
        downtime,
        records,
        detection_delay,
        security,
        operational_loss
    ])

# -----------------------------
# 4. Create DataFrame & save
# -----------------------------
columns = [
    "attack_type",
    "attack_vector",
    "system_affected",
    "downtime_hours",
    "records_compromised",
    "detection_delay_minutes",
    "security_level",
    "operational_loss"
]

df = pd.DataFrame(data, columns=columns)
df.to_csv(
    r"C:\Users\sahukari naveena\OneDrive\Desktop\MINI_PROJECT\Cyber_Operational_Loss_Prediction\data\raw_data\cyber_healthcare_data.csv",
    index=False
)


print("Dataset created successfully: cyber_healthcare_data.csv")
