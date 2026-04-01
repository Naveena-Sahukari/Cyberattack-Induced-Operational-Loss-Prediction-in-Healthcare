# Cyberattack-Induced Operational Loss Prediction in Healthcare

## Overview

Cyberattacks in healthcare can severely disrupt hospital operations.
When critical systems such as Electronic Health Records (EHR), billing systems, or patient management platforms are affected, hospitals may experience downtime, delayed treatments, financial losses, and compromised patient data.

Most cybersecurity systems focus only on **detecting attacks**, but hospital administrators need answers to more operational questions such as:

* How severe will the operational impact be?
* What factors are driving the loss?
* What actions should be taken immediately?

This project addresses that gap by developing a **Cyberattack Impact Intelligence System** that predicts operational loss from cyberattack scenarios and explains the prediction using **Explainable AI techniques**.

The system integrates **Machine Learning, Explainable AI, and a Django web application** to transform cyberattack data into **actionable operational insights**.

---

## Problem Statement

Healthcare organizations face increasing cyber threats, including ransomware attacks, malware infections, and data breaches.

While many cybersecurity tools detect attacks, they do not answer critical operational questions such as:

* What will be the financial and operational loss?
* Which factors are contributing most to the impact?
* How should hospital administrators respond?

This project builds a **decision-support system** that estimates operational loss and provides interpretability and guidance for healthcare administrators.

---

## Key Features

* Predicts operational loss caused by healthcare cyberattacks
* Identifies key loss drivers such as downtime and detection delay
* Explains predictions using SHAP (Explainable AI)
* Web-based dashboard built using Django
* Real-time prediction from user inputs
* Provides operational risk recommendations

---

## System Architecture

The system follows a full machine learning deployment pipeline:
```
Login Page
    ↓
User enters cyber attack scenario
    ↓
Django Backend receives data
    ↓
Random Forest Model predicts operational loss
    ↓
SHAP Explainability identifies key factors
    ↓
Result Dashboard displays prediction + analysis + recommendations
```

---

## Dataset

Due to privacy restrictions, real healthcare cyberattack datasets are not publicly available.

Therefore, this project uses a **synthetic dataset** created using realistic ranges and relationships based on public cybersecurity reports and healthcare breach statistics.

Each scenario includes features such as:

* Attack Type (Ransomware, Malware, Phishing, DDoS)
* Attack Vector (Email, Network, USB)
* System Affected (EHR, Billing, PACS)
* Security Maturity Level
* Downtime Duration
* Detection Delay
* Records Compromised

---

## Machine Learning Model

The project uses a **Random Forest Regressor** to estimate operational loss.

### Why Random Forest?

* Captures non-linear relationships
* Robust to noise and outliers
* Handles mixed feature types
* Provides stable performance
* Easier to explain than deep learning models

---

## Explainable AI

To improve transparency and trust in predictions, the system uses **SHAP (SHapley Additive Explanations)**.

SHAP explains:

* Which features increased predicted loss
* Which features reduced predicted loss
* How each factor contributes to the final prediction

This helps healthcare administrators understand **why the model produced a particular result**.

---

## Decision Support Framework

| Predicted Loss | Recommended Action                           |
| -------------- | -------------------------------------------- |
| Low            | Routine monitoring                           |
| Medium         | Resource optimization and monitoring         |
| High           | Immediate intervention and system isolation  |

---

## Technology Stack

**Backend**
* Python
* Django
* NumPy
* Scikit-learn
* SHAP

**Machine Learning**
* Random Forest Regression
* SHAP Explainable AI

**Frontend**
* HTML
* CSS

---

## Project Structure
```
Cyber_Operational_Loss_Prediction/
├── cyberloss_project/
│   ├── settings.py
│   └── urls.py
├── predictor/
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── templates/
│   ├── login.html
│   ├── home.html
│   ├── simulator.html
│   ├── dashboard.html
│   ├── analytics.html
│   └── reports.html
├── scripts/
│   ├── 01_create_dataset.py
│   ├── 02_preprocess_data.py
│   ├── 03_train_model.py
│   ├── 04_model_comparison.py
│   ├── 05_loss_driver_analysis.py
│   ├── 06_shap_explainability.py
│   ├── 07_error_risk_analysis.py
│   ├── predict_loss.py
│   └── visualize_results.py
├── static/
├── data/
├── outputs/
├── manage.py
└── README.md
```

---

## Setup Instructions

After cloning the repository, follow these steps:

**1. Create and activate virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**2. Install dependencies**
```bash
pip install django pandas scikit-learn shap joblib numpy matplotlib
```

**3. Generate dataset and train model**
```bash
python scripts/01_create_dataset.py
python scripts/03_train_model.py
```

**4. Run database migrations**
```bash
python manage.py migrate
python manage.py createsuperuser
```

**5. Start the server**
```bash
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

---

## Key Insights

* Downtime duration is the strongest driver of operational loss
* Detection delay significantly increases financial impact
* Security maturity level reduces overall risk
* Large-scale data breaches increase recovery costs

---

## Limitations

* Dataset is synthetic and based on assumed relationships
* Decision recommendations are rule-based
* Real-time cyber monitoring integration is not included

---

## Future Improvements

* Integration with real-time cybersecurity monitoring tools
* Deployment on cloud infrastructure
* Interactive dashboards for hospital administrators
* Time-series prediction of operational costs

---

## Author

**Naveena Sahukari**
Machine Learning | Healthcare Analytics
GitHub: https://github.com/Naveena-Sahukari

---

## Disclaimer

This project uses synthetic data created for academic and educational purposes.
It is intended as a prototype decision-support system and not a production healthcare system.