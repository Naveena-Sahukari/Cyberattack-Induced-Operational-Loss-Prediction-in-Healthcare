---

## 📊 Dataset

Due to privacy restrictions, real healthcare cyberattack datasets are not publicly available. This project uses a **synthetic dataset** generated using realistic ranges and relationships drawn from public cybersecurity reports and healthcare breach statistics.

**Features per scenario:**

| Feature | Description |
|---------|-------------|
| Attack Type | Ransomware, Malware, Phishing, etc. |
| Attack Vector | Email, Network, Physical |
| System Affected | EHR, Billing, Database |
| Security Maturity Level | Low / Medium / High |
| Downtime Duration | Hours of operational downtime |
| Detection Delay | Hours before attack was identified |
| Records Compromised | Number of patient records affected |

---

## 🤖 Machine Learning Model

The project uses a **Random Forest Regressor** to estimate operational loss.

**Why Random Forest?**
- Captures non-linear relationships between attack features
- Robust to noise and outliers in synthetic data
- Handles mixed feature types (categorical + numerical)
- More interpretable than deep learning approaches

---

## 🧠 Explainable AI (SHAP)

The system uses **SHAP (SHapley Additive Explanations)** to make predictions transparent:

- Which features **increased** the predicted loss
- Which features **reduced** the predicted loss
- How much each factor contributes to the final result

This builds trust and helps administrators understand **why** a particular prediction was made.

---

## 📋 Decision Support Framework

| Predicted Loss Level | Recommended Action |
|---------------------|-------------------|
| 🟢 Low | Routine monitoring, standard protocols |
| 🟡 Medium | Resource optimization, heightened monitoring |
| 🔴 High | Immediate intervention, system isolation |

---

## 🔑 Running Locally
```bash
# 1. Clone the repository
git clone https://github.com/Naveena-Sahukari/Cyberattack-Induced-Operational-Loss-Prediction-in-Healthcare.git
cd Cyberattack-Induced-Operational-Loss-Prediction-in-Healthcare

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run ML pipeline (if needed)
python scripts/01_create_dataset.py
python scripts/03_train_model.py

# 4. Start Django server
python manage.py runserver
```

---

## 💡 Key Insights

- **Downtime duration** is the strongest driver of operational loss
- **Detection delay** significantly amplifies financial impact
- **Security maturity level** is the most effective risk reducer
- **Large-scale data breaches** exponentially increase recovery costs

---

## ⚠️ Limitations

- Dataset is synthetic (based on assumed relationships, not real breach data)
- Decision recommendations are rule-based, not adaptive
- No real-time cybersecurity monitoring integration

---

## 🔮 Future Improvements

- Integration with real-time cybersecurity monitoring tools (SIEM, SOC feeds)
- Cloud-native dashboards for hospital administrators
- Time-series prediction of operational costs over incident lifecycle
- Integration with hospital incident response and EHR systems

---

## 👩‍💻 Author

**Naveena Sahukari**  
Machine Learning | Healthcare Analytics  
GitHub: [@Naveena-Sahukari](https://github.com/Naveena-Sahukari)

---

## 📢 Disclaimer

This project uses synthetic data created for academic and educational purposes. It is intended as a prototype decision-support system and is **not** a production healthcare system.
