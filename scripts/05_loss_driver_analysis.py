import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# FIX: replaced all hardcoded absolute Windows paths with portable Path-based resolution
BASE_DIR   = Path(__file__).resolve().parent.parent
DATA_PATH  = BASE_DIR / "data" / "processed_data" / "processed_cyber_healthcare_data.csv"
OUTPUT_DIR = BASE_DIR / "outputs" / "graphs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)

# 1. Loss vs Downtime
plt.figure()
plt.scatter(df["downtime_hours"], df["operational_loss"])
plt.xlabel("Downtime (hours)")
plt.ylabel("Operational Loss")
plt.title("Operational Loss vs Downtime")
plt.savefig(OUTPUT_DIR / "loss_vs_downtime.png")
plt.close()

# 2. Loss vs Detection Delay
plt.figure()
plt.scatter(df["detection_delay_minutes"], df["operational_loss"])
plt.xlabel("Detection Delay (minutes)")
plt.ylabel("Operational Loss")
plt.title("Loss vs Detection Delay")
plt.savefig(OUTPUT_DIR / "loss_vs_detection_delay.png")
plt.close()

# 3. Loss by System Affected
plt.figure()
df.groupby("system_affected")["operational_loss"].mean().plot(kind="bar")
plt.xlabel("System Affected")
plt.ylabel("Average Operational Loss")
plt.title("Loss by System Affected")
plt.savefig(OUTPUT_DIR / "loss_by_system.png")
plt.close()

print("Loss driver analysis plots generated.")