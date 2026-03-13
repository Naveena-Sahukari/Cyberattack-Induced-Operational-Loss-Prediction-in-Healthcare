\# Cyberattack-Induced Operational Loss Prediction in Healthcare



\## Overview



Cyberattacks in healthcare can severely disrupt hospital operations.

When critical systems such as Electronic Health Records (EHR), billing systems, or patient management platforms are affected, hospitals may experience downtime, delayed treatments, financial losses, and compromised patient data.



Most cybersecurity systems focus only on \*\*detecting attacks\*\*, but hospital administrators need answers to more operational questions such as:



\* How severe will the operational impact be?

\* What factors are driving the loss?

\* What actions should be taken immediately?



This project addresses that gap by developing a \*\*Cyberattack Impact Intelligence System\*\* that predicts operational loss from cyberattack scenarios and explains the prediction using \*\*Explainable AI techniques\*\*.



The system integrates \*\*Machine Learning, Explainable AI, and a Django web application\*\* to transform cyberattack data into \*\*actionable operational insights\*\*.







\# Problem Statement



Healthcare organizations face increasing cyber threats, including ransomware attacks, malware infections, and data breaches.



While many cybersecurity tools detect attacks, they do not answer critical operational questions such as:



\* What will be the financial and operational loss?

\* Which factors are contributing most to the impact?

\* How should hospital administrators respond?



This project builds a \*\*decision-support system\*\* that estimates operational loss and provides interpretability and guidance for healthcare administrators.







\# Key Features



\* Predicts operational loss caused by healthcare cyberattacks

\* Identifies key loss drivers such as downtime and detection delay

\* Explains predictions using SHAP (Explainable AI)

\* Generates visual analysis graphs

\* Provides operational risk recommendations

<<<<<<< HEAD
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

\* Web-based dashboard built using Django
 76df968 (Added CyberMed Impact Intelligence Platform project)

\* Real-time prediction from user inputs



---



\# System Architecture



The system follows a full machine learning deployment pipeline:





Login Page

&nbsp;    ↓

User enters cyber attack scenario

&nbsp;    ↓

Django Backend receives data

&nbsp;    ↓

Random Forest Model predicts operational loss

&nbsp;    ↓

SHAP Explainability identifies key factors

&nbsp;    ↓

Graphs generated dynamically

&nbsp;    ↓

Result Dashboard displays prediction + analysis + recommendations

```



---



\# Dataset



Due to privacy restrictions, real healthcare cyberattack datasets are not publicly available.



Therefore, this project uses a \*\*synthetic dataset\*\* created using realistic ranges and relationships based on public cybersecurity reports and healthcare breach statistics.



Each scenario includes features such as:



\* Attack Type (Ransomware, Malware, etc.)

\* Attack Vector (Email, Network)

\* System Affected (EHR, Database)

\* Security Maturity Level

\* Downtime Duration

\* Detection Delay

\* Records Compromised



This allows meaningful analysis while maintaining privacy.



---



\# Machine Learning Model



The project uses a \*\*Random Forest Regressor\*\* to estimate operational loss.



\### Why Random Forest?



\* Captures non-linear relationships

\* Robust to noise and outliers

\* Handles mixed feature types

\* Provides stable performance

\* Easier to explain than deep learning models



---



\# Explainable AI



To improve transparency and trust in predictions, the system uses \*\*SHAP (SHapley Additive Explanations)\*\*.



SHAP explains:



\* Which features increased predicted loss

\* Which features reduced predicted loss

\* How each factor contributes to the final prediction



This helps healthcare administrators understand \*\*why the model produced a particular result\*\*.



---



\# Visualization and Analysis



The system generates visual insights including:



\* SHAP Explanation Plot

\* Impact Graph of attack factors

\* Downtime and detection delay influence

\* Records compromised impact



These graphs are generated dynamically during prediction.



---



\# Decision Support Framework



Predicted operational loss is translated into actionable guidance.



| Predicted Loss | Recommended Action                          |

| -------------- | ------------------------------------------- |

| Low            | Routine monitoring                          |

| Medium         | Resource optimization and monitoring        |

| High           | Immediate intervention and system isolation |



This allows hospital administrators to respond quickly during cyber incidents.



---



\# Technology Stack



Backend



\* Python

\* Django

\* NumPy

\* Scikit-learn



Machine Learning



\* Random Forest Regression

\* SHAP Explainable AI



Visualization



\* Matplotlib



Frontend



\* HTML

\* CSS



---



\# Project Structure



```

Cyber\_Operational\_Loss\_Prediction



├── cyberloss\_project

│   ├── settings.py

│   ├── urls.py

│

├── predictor

│   ├── views.py

│   ├── urls.py

│

├── templates

│   ├── login.html

│   ├── home.html

│   ├── output.html

│

├── models

│   └── loss\_prediction\_model.pkl

│

├── static

│   ├── shap

│   └── graphs

│

├── scripts

│   ├── create\_dataset.py

│   ├── preprocess\_data.py

│   ├── train\_model.py

│   ├── shap\_explainability.py

│

├── outputs

│

├── manage.py

└── README.md

```



---



\# Key Insights



Analysis of the dataset reveals:



\* Downtime duration is the strongest driver of operational loss

\* Detection delay significantly increases financial impact

\* Security maturity level reduces overall risk

\* Large-scale data breaches increase recovery costs



These insights align with real-world cybersecurity reports in healthcare.



---



\# Limitations



\* Dataset is synthetic and based on assumed relationships

\* Decision recommendations are rule-based

\* Real-time cyber monitoring integration is not included



These limitations are acceptable for an academic prototype.



---



\# Future Improvements



\* Integration with real-time cybersecurity monitoring tools

\* Deployment on cloud infrastructure

\* Interactive dashboards for hospital administrators

\* Time-series prediction of operational costs

\* Integration with hospital incident response systems



---



\# Author



Naveena Sahukari

Machine Learning | Healthcare Analytics



GitHub

https://github.com/Naveena-Sahukari



---



\# Disclaimer



This project uses synthetic data created for academic and educational purposes.

It is intended as a prototype decision-support system and not a production healthcare system.



