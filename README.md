🌟Cyberattack-Induced Operational Loss Prediction in Healthcare

⭐ About the Project:

Cyberattacks in healthcare do not just affect IT systems — they disrupt patient care, delay treatments, and increase operational costs.
Even short periods of downtime can have serious consequences in hospitals.

This project focuses on predicting and explaining the operational loss caused by cyber incidents in healthcare, with the goal of helping organizations make better and faster operational decisions instead of reacting blindly after damage occurs.

The project is designed as a decision-support system, not just a machine learning experiment.

⭐ Problem Statement:

Most cybersecurity solutions answer the question:

“Did an attack happen?”

However, healthcare administrators and operations teams need answers to more practical questions:

How severe will the operational impact be?

What factors are driving the loss?

What action should be taken immediately?

This project addresses that gap by estimating operational loss from cyberattack scenarios and converting predictions into actionable guidance.

⭐ What This Project Does

Predicts operational loss caused by healthcare cyberattacks

Identifies key loss drivers such as downtime and detection delay

Explains predictions using Explainable AI (SHAP)

Maps predictions to clear operational actions

In simple terms, it turns cyberattack data into business and operational insight.

⭐ Dataset

Due to privacy and security constraints, real healthcare cyber incident data is not publicly available.
To handle this, the project uses a synthetic dataset created using realistic ranges and relationships inspired by public healthcare cybersecurity and breach reports.

Each row in the dataset represents a possible cyberattack scenario with features such as:

Attack type and attack vector

System affected (EHR, billing, etc.)

Downtime duration

Number of records compromised

Detection delay

Security maturity level

This approach preserves privacy while still allowing meaningful analysis.

⭐ Approach & Methodology

Data Preparation

Encoded categorical features

Scaled numerical variables

Exploratory Data Analysis

Identified operational loss drivers such as downtime and detection delay

Modeling

Trained a Random Forest regression model

Evaluation

Used MAE, RMSE, and R² metrics

Explainability

Applied SHAP to understand global and individual predictions

Decision Mapping

Converted predicted loss into severity levels and recommended actions

⭐ Why Random Forest?

Random Forest was selected because it provides a strong balance between performance, robustness, and interpretability, which is especially important in healthcare applications.

It:

Captures non-linear relationships in operational loss data

Is robust to noise and outliers

Works well with mixed feature types

Is easier to justify than deep learning models in sensitive domains

Linear models tend to underfit this problem, while deep learning models require larger real-world datasets and offer limited transparency.

⭐ Decision Framework

Predictions are translated into operational actions using a simple framework:

Predicted Loss	Recommended Action
Low	Routine monitoring
Medium	Resource optimization
High	Immediate intervention and system isolation

This ensures model outputs can be directly used for decision-making.

⭐ Project Structure
Cyber-Operational-Loss-Prediction/
├── data/
│   ├── raw/
│   └── processed/
├── models/
│   └── loss_prediction_model.pkl
├── scripts/
│   ├── 01_create_dataset.py
│   ├── 02_preprocess_data.py
│   ├── 03_train_model.py
│   ├── 04_model_comparison.py
│   ├── 05_loss_driver_analysis.py
│   ├── 06_shap_explainability.py
│   └── 07_error_risk_analysis.py
|   |__predict_loss
|   |--visualize_results
├── outputs/
│   ├── graphs/
│   └── reports/
├── README.md

⭐ Key Results & Insights:

Downtime duration and detection delay are the strongest contributors to operational loss

Underestimating high-loss incidents is riskier than conservative overestimation

Explainability results align well with healthcare domain expectations

⭐ Limitations

Dataset is synthetic and based on assumptions from public reports

Decision guidance is rule-based

Real-time system integration is not included

These limitations are acceptable for an academic and early industry prototype.

⭐ Future Improvements

Integration with real-time cybersecurity monitoring systems

Cost-sensitive threshold tuning

Explainable dashboards for hospital administrators

Time-series forecasting of hospital operational costs

Cloud-based deployment for multi-hospital use

⭐ Tech Stack

Python

Pandas, NumPy

Scikit-learn

SHAP

Matplotlib

⭐ Disclaimer

This project uses synthetic data created for academic and learning purposes to respect healthcare data privacy.
It is intended as a decision-support prototype, not a production healthcare system.

⭐ Author

Naveena Sahukari
Machine Learning | Healthcare Analytics
GitHub: https://github.com/Naveena-Sahukari
