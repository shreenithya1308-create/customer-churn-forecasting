# Batch Prediction for Customer Churn Forecasting

A cloud-based machine learning application for automated customer churn prediction using Google Cloud Vertex AI, BigQuery, and Google Cloud Storage.

This project implements an end-to-end batch prediction pipeline that enables organizations to identify customers who are likely to churn through a scalable, automated, and cloud-native machine learning solution.

## Project Overview

Customer churn prediction plays an important role in helping businesses retain valuable customers by identifying users who are likely to discontinue their services.

Traditional churn prediction approaches often require significant manual effort and may face scalability challenges when processing large datasets.

This project addresses these challenges by developing a fully automated batch prediction pipeline using Google Cloud services.

The system automates:

- Data processing
- Dataset storage
- Machine learning model training
- Model deployment
- Batch inference
- Prediction storage
- Result visualization

The final predictions are stored in BigQuery and presented through an interactive Streamlit dashboard for easier analysis.

## Objectives

The main objectives of this project are:

- Predict customer churn using machine learning
- Build an automated batch prediction pipeline
- Integrate Google Cloud services for scalable machine learning deployment
- Store and analyze prediction results using BigQuery
- Visualize customer churn predictions through an interactive dashboard
- Reduce manual intervention using cloud-native automation
- Enable scalable prediction on large customer datasets

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application development and data processing |
| Streamlit | Interactive web dashboard |
| Google Cloud Vertex AI | AutoML model training and batch prediction |
| Google Cloud Storage | Dataset and file storage |
| BigQuery | Prediction storage and analytics |
| AutoML Tabular | Machine learning model |
| Pandas | Data processing and analysis |
| Git & GitHub | Version control and project management |

## Dataset

The project uses the Kaggle Telecom Customer Churn Dataset.

The dataset contains customer-related information including:

- Customer demographics
- Account information
- Service usage
- Contract details
- Customer support interactions
- Payment methods
- Churn status

### Target Variable

| Value | Meaning |
|------:|---------|
| 1 | Customer churned or left the service |
| 0 | Customer retained the service |

## System Features

### Automated Batch Prediction

The application provides an automated batch prediction workflow that allows users to:

- Upload customer datasets
- Store datasets in Google Cloud Storage
- Trigger Vertex AI batch prediction jobs
- Process large datasets automatically
- Generate customer-level churn predictions

### Cloud-Based Architecture

The project uses multiple Google Cloud services to provide a scalable machine learning workflow:

- Google Cloud Storage for dataset management
- Vertex AI for model training and batch inference
- BigQuery for prediction storage and analytics
- Streamlit for prediction visualization

### Interactive Dashboard

The Streamlit dashboard provides:

- Batch prediction results
- Customer-level predictions
- Churn probabilities
- Prediction summaries
- Churn distribution visualizations

### Large-Scale Processing

The batch prediction architecture allows the application to process large customer datasets without requiring manual prediction for individual customers.

## Machine Learning Pipeline

The application follows an end-to-end cloud-based workflow:

Customer Dataset | v Google Cloud Storage | v Vertex AI AutoML | v Model Training | v Batch Prediction | v BigQuery | v Streamlit Dashboard


### Pipeline Steps

#### 1. Upload Customer Dataset

The user uploads a customer dataset through the Streamlit application.

#### 2. Store Dataset

The uploaded dataset is stored in Google Cloud Storage.

#### 3. Train Machine Learning Model

The dataset is used to train an AutoML Tabular model using Vertex AI.

#### 4. Deploy Model

The trained model is made available through Vertex AI for inference.

#### 5. Execute Batch Prediction

Vertex AI performs batch prediction on the uploaded customer dataset.

#### 6. Store Predictions

The prediction results are stored in BigQuery for further analysis.

#### 7. Visualize Results

The Streamlit dashboard retrieves and displays the prediction results interactively.

## Model Performance

The trained model achieved the following evaluation results:

Metric	Score
ROC-AUC	0.961
PR-AUC	0.954
F1-Score	0.93
Precision	92.88%
Recall	93.14%
These results demonstrate strong predictive performance in identifying customers who are at risk of churn.

Dashboard Modules
Customer Dataset Upload
Allows users to upload customer CSV datasets that can be processed for batch prediction.

Batch Prediction
Initiates automated prediction using the trained Google Cloud Vertex AI model.

Prediction Results
Displays customer-level prediction information, including:

Customer ID
Predicted Label
Churn Probability
Prediction Summary
Provides visual summaries of prediction results, including the overall distribution of customers predicted to churn and customers predicted to remain.

Project Architecture
                    +---------------------+
                    |   Customer Dataset  |
                    +----------+----------+
                               |
                               v
                    +---------------------+
                    | Google Cloud Storage |
                    +----------+----------+
                               |
                               v
                    +---------------------+
                    | Vertex AI AutoML    |
                    | Model Training      |
                    +----------+----------+
                               |
                               v
                    +---------------------+
                    | Batch Prediction    |
                    +----------+----------+
                               |
                               v
                    +---------------------+
                    | BigQuery            |
                    | Prediction Storage  |
                    +----------+----------+
                               |
                               v
                    +---------------------+
                    | Streamlit Dashboard |
                    +---------------------+
Installation
Clone the Repository
git clone https://github.com/shreenithya1308-create/customer-churn-forecasting.git
Navigate to the Project Directory
cd customer-churn-forecasting
Install Dependencies
pip install -r requirements.txt
Run the Application
streamlit run app.py
Project Structure
customer-churn-forecasting/
|
├── app.py
├── requirements.txt
├── README.md
|
├── dataset/
├── model/
├── prediction/
├── utils/
├── scripts/
└── assets/
Key Highlights
End-to-end cloud-based machine learning pipeline
Automated batch prediction using Google Cloud Vertex AI
AutoML Tabular model for customer churn prediction
Interactive Streamlit dashboard
BigQuery integration for prediction storage and analytics
Google Cloud Storage integration
Scalable batch processing
Customer-level churn probability analysis
High predictive performance
ROC-AUC score of 0.961
Cloud-native machine learning architecture
Future Enhancements
The project can be further extended with:

Real-time prediction endpoints
Explainable AI using SHAP values
Automated daily predictions using Cloud Scheduler
Multi-domain churn prediction
Advanced dashboard analytics
Customer segmentation and profiling
Customer retention recommendations
Docker-based deployment
Deployment using Google Cloud Run
Model monitoring and performance tracking
Research Publication
This project is associated with the research paper:

Batch Prediction for Customer Churn Forecasting

The research presents a scalable, cloud-native machine learning pipeline using Google Cloud Vertex AI for automated customer churn prediction and batch inference.

Author
Nithya Shree M
B.Tech – Computer Science and Engineering (AI & ML)

SRM Institute of Science and Technology

GitHub: https://github.com/shreenithya1308-create

LinkedIn: https://linkedin.com/in/nithyashree13

License
This project is developed for academic and educational purposes.
