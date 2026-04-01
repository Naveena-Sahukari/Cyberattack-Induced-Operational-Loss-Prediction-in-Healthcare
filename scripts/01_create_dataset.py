import pandas as pd
import random

# ----------- possible values -----------

attack_types = ["Ransomware", "Phishing", "DDoS", "Malware"]
attack_vectors = ["Email", "Network", "USB"]
systems_affected = ["EHR", "Billing", "PACS"]
security_levels = ["Low", "Medium", "High"]

# ----------- cost assumptions -----------

COST_PER_HOUR_DOWNTIME = 15000    # was 200000
COST_PER_RECORD        = 50       # was 500
COST_PER_DELAY         = 300      # was 5000

# ----------- weights -----------

attack_weight = {
    "Ransomware": 1.8,
    "Phishing":   1.2,
    "DDoS":       1.4,
    "Malware":    1.3
}

system_weight = {
    "EHR":     2.0,
    "Billing": 1.5,
    "PACS":    1.7
}

security_weight = {
    "Low":    1.6,
    "Medium": 1.2,
    "High":   0.7
}

# ----------- dataset -----------

data = []

for _ in range(3000):

    attack_type   = random.choice(attack_types)
    attack_vector = random.choice(attack_vectors)
    system        = random.choice(systems_affected)
    security      = random.choice(security_levels)

    downtime = random.randint(1, 48)
    records  = random.randint(100, 100000)
    delay    = random.randint(1, 300)

    # ----------- base loss -----------

    base_loss = (
        downtime * COST_PER_HOUR_DOWNTIME +
        records  * COST_PER_RECORD        +
        delay    * COST_PER_DELAY
    )

    # ----------- apply weights -----------

    operational_loss = base_loss \
        * attack_weight[attack_type] \
        * system_weight[system]      \
        * security_weight[security]

    # ----------- add randomness -----------

    noise = random.randint(-50000, 50000)
    operational_loss += noise

    # prevent negative values
    if operational_loss < 0:
        operational_loss = abs(operational_loss)

    data.append([
        attack_type,
        attack_vector,
        system,
        downtime,
        records,
        delay,
        security,
        operational_loss
    ])

# ----------- dataframe -----------

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

# ----------- save -----------

df.to_csv("data/cyber_healthcare_data.csv", index=False)

print("✅ Dataset generated successfully with dynamic behavior")