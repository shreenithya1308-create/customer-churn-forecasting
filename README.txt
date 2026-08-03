# Batch Prediction for Customer Churn Forecasting

A cloud-based machine learning application for automated customer churn prediction using **Google Cloud Vertex AI**, **BigQuery**, and **Google Cloud Storage**. The project implements an end-to-end batch prediction pipeline that enables organizations to identify customers likely to churn through scalable cloud-native machine learning.

---

## Project Overview

Customer churn prediction plays a vital role in helping businesses retain valuable customers by identifying users who are likely to discontinue a service. Traditional approaches often require significant manual effort and struggle to scale with growing datasets.

This project addresses these challenges by developing a fully automated batch prediction pipeline using Google Cloud services. The system automates data processing, model deployment, batch inference, and result visualization, providing an efficient and scalable solution for customer churn analysis.

---

## Objectives

- Predict customer churn using machine learning
- Build an automated batch prediction pipeline
- Integrate Google Cloud services for scalable deployment
- Store and analyze prediction results using BigQuery
- Visualize predictions through an interactive Streamlit dashboard
- Reduce manual intervention using cloud-native automation

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application Development |
| Streamlit | Interactive Web Application |
| Google Cloud Vertex AI | AutoML Model Training & Batch Prediction |
| Google Cloud Storage | Dataset Storage |
| BigQuery | Prediction Storage & Analytics |
| AutoML Tabular | Machine Learning Model |
| Pandas | Data Processing |
| Git & GitHub | Version Control |

---

# Dataset

**Source:** Kaggle Telecom Customer Churn Dataset

The dataset contains customer information including:

- Customer demographics
- Account information
- Service usage
- Contract details
- Customer support interactions
- Payment methods
- Churn status

Target Variable:

- **Churn = 1** → Customer left the service
- **Churn = 0** → Customer retained

---

# System Features

## Automated Batch Prediction

- Upload customer datasets
- Trigger Vertex AI batch prediction jobs
- Process large datasets automatically

## Cloud-Based Architecture

- Google Cloud Storage for dataset management
- Vertex AI for model deployment
- BigQuery for prediction storage
- Scalable cloud-native workflow

## Interactive Dashboard

Displays:

- Batch prediction results
- Churn probability
- Prediction summary
- Customer-level insights

## Large-Scale Processing

Supports automated prediction on large customer datasets without manual intervention.

---

# Machine Learning Pipeline

The application follows the workflow below:

1. Upload customer dataset
2. Store dataset in Google Cloud Storage
3. Train AutoML model using Vertex AI
4. Deploy trained model
5. Execute batch prediction
6. Store predictions in BigQuery
7. Visualize results using Streamlit

---

# Model Performance

The trained model achieved the following evaluation metrics:

| Metric | Score |
|---------|--------|
| ROC-AUC | **0.961** |
| PR-AUC | **0.954** |
| F1-Score | **0.93** |
| Precision | **92.88%** |
| Recall | **93.14%** |

These results demonstrate strong predictive performance for identifying customers at risk of churn.

---

# Dashboard Modules

### Customer Dataset Upload

Upload CSV datasets for batch prediction.

### Batch Prediction

Runs automated prediction jobs using Google Cloud Vertex AI.

### Prediction Results

Displays:

- Customer ID
- Predicted Label
- Churn Probability

### Prediction Summary

Visualizes overall churn distribution using charts.

---

# Project Architecture

```
Customer Dataset
        │
        ▼
Google Cloud Storage
        │
        ▼
Vertex AI AutoML
        │
        ▼
Batch Prediction
        │
        ▼
BigQuery
        │
        ▼
Streamlit Dashboard
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/shreenithya1308-create/customer-churn-forecasting.git
```

## Navigate to Project

```bash
cd customer-churn-forecasting
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

---

# Project Structure

```
customer-churn-forecasting/
│
├── app.py
├── requirements.txt
├── README.md
├── dataset/
├── model/
├── prediction/
├── utils/
├── scripts/
└── assets/
```

---

# Key Highlights

- End-to-end cloud-based machine learning pipeline
- Automated batch prediction using Google Cloud Vertex AI
- Interactive Streamlit dashboard
- Scalable BigQuery integration
- Large-scale customer churn prediction
- Cloud-native deployment architecture
- High predictive performance with ROC-AUC of 0.961

---

# Future Enhancements

- Real-time prediction endpoints
- Explainable AI using SHAP values
- Cloud Scheduler for automated daily predictions
- Multi-domain churn prediction
- Advanced dashboard analytics
- Customer segmentation insights
- Deployment using Docker and Cloud Run

---

# Research Publication

This project is associated with the research paper:

**Batch Prediction for Customer Churn Forecasting**

The work presents a scalable cloud-native machine learning pipeline using Google Cloud Vertex AI for automated customer churn prediction.

---

# Author

**Nithya Shree M**

B.Tech – Computer Science and Engineering (AI & ML)

SRM Institute of Science and Technology

GitHub: https://github.com/shreenithya1308-create

LinkedIn: https://linkedin.com/in/nithyashree13

---

# License

This project is developed for academic and educational purposes.
