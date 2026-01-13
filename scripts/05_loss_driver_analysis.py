import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\sahukari naveena\OneDrive\Desktop\MINI_PROJECT\Cyber_Operational_Loss_Prediction\data\processed_data\processed_cyber_healthcare_data.csv")

# 1. Loss vs Downtime
plt.figure()
plt.scatter(df["downtime_hours"], df["operational_loss"])
plt.xlabel("Downtime (hours)")
plt.ylabel("Operational Loss")
plt.title("Operational Loss vs Downtime")
plt.savefig(r"C:\Users\sahukari naveena\OneDrive\Desktop\MINI_PROJECT\Cyber_Operational_Loss_Prediction\outputs\graphs\loss_vs_downtime.png")
plt.close()

# 2. Loss vs Detection Delay
plt.figure()
plt.scatter(df["detection_delay_minutes"], df["operational_loss"])
plt.xlabel("Detection Delay (minutes)")
plt.ylabel("Operational Loss")
plt.title("Loss vs Detection Delay")
plt.savefig(r"C:\Users\sahukari naveena\OneDrive\Desktop\MINI_PROJECT\Cyber_Operational_Loss_Prediction\outputs\graphs\loss_vs_detection_delay.png")
plt.close()

# 3. Loss by System Affected
plt.figure()
df.groupby("system_affected")["operational_loss"].mean().plot(kind="bar")
plt.xlabel("System Affected")
plt.ylabel("Average Operational Loss")
plt.title("Loss by System Affected")
plt.savefig(r"C:\Users\sahukari naveena\OneDrive\Desktop\MINI_PROJECT\Cyber_Operational_Loss_Prediction\outputs\graphs\loss_by_system.png")
plt.close()

print("Loss driver analysis plots generated.")
