# 🏥 CyberMed Insight — Cyberattack-Induced Operational Loss Prediction in Healthcare

> A Machine Learning + Explainable AI web platform that predicts and explains operational losses caused by cyberattacks in healthcare environments.

🔗 **Live Demo:** [https://cybermedinsight.up.railway.app](https://cybermedinsight.up.railway.app)

---

## 📌 Overview

Cyberattacks in healthcare can severely disrupt hospital operations. When critical systems such as Electronic Health Records (EHR), billing systems, or patient management platforms are affected, hospitals face downtime, delayed treatments, financial losses, and compromised patient data.

Most cybersecurity tools focus only on **detecting attacks** — but hospital administrators need answers to operational questions:

- How severe will the operational impact be?
- What factors are driving the loss?
- What immediate actions should be taken?

**CyberMed Insight** addresses this gap by developing a **Cyberattack Impact Intelligence System** that:
- **Predicts** operational loss from cyberattack scenarios
- **Explains** predictions using Explainable AI (SHAP)
- **Guides** administrators with actionable risk recommendations

---

## 🚀 Live Deployment

| Platform | URL |
|----------|-----|
| Railway | [https://cybermedinsight.up.railway.app](https://cybermedinsight.up.railway.app) |

The application is fully deployed and accessible. Log in with a hospital name and password to access the prediction dashboard.

---

## ✨ Key Features

- 🔐 **Secure Login** — Hospital-specific authentication
- 🤖 **ML-Powered Prediction** — Random Forest Regressor estimates operational loss
- 🧠 **Explainable AI** — SHAP values identify which factors drive the predicted loss
- 📊 **Dynamic Visualizations** — Auto-generated SHAP and impact graphs per prediction
- 📋 **Decision Support** — Rule-based action recommendations (Low / Medium / High risk)
- 🔍 **What-If Analysis** — Explore different cyberattack scenarios instantly

---

## 🏗️ System Architecture

```
Login Page
    ↓
User enters cyberattack scenario
    ↓
Django Backend receives input
    ↓
Random Forest Model → predicts operational loss
    ↓
SHAP Explainability → identifies key contributing factors
    ↓
Graphs generated dynamically
    ↓
Result Dashboard → prediction + analysis + recommendations
```

---

## 🧰 Technology Stack

| Layer | Technologies |
|-------|-------------|
| **Backend** | Python, Django |
| **Machine Learning** | Scikit-learn (Random Forest Regressor) |
| **Explainable AI** | SHAP (SHapley Additive Explanations) |
| **Visualization** | Matplotlib |
| **Frontend** | HTML, CSS |
| **Deployment** | Railway |

---

## 📂 Project Structure

```
Cyberattack-Induced-Operational-Loss-Prediction-in-Healthcare/
│
├── cyberloss_project/        # Django project settings & URLs
│   ├── settings.py
│   └── urls.py
│
├── predictor/                # Core app: views, URLs, ML logic
│   ├── views.py
│   └── urls.py
│
├── templates/                # HTML templates
│   ├── login.html
│   ├── home.html
│   └── output.html
│
├── static/                   # Static assets (SHAP plots, graphs)
│   ├── shap/
│   └── graphs/
│
├── scripts/                  # ML pipeline scripts
│   ├── 01_create_dataset.py
│   ├── 02_preprocess_data.py
│   ├── 03_train_model.py
│   ├── 04_model_comparison.py
│   ├── 05_loss_driver_analysis.py
│   ├── 06_shap_explainability.py
│   └── 07_error_risk_analysis.py
│
├── data/                     # Raw and processed datasets
│   ├── raw/
│   └── processed/
│
├── outputs/                  # Generated graphs and reports
│
├── manage.py
└── README.md
```

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
