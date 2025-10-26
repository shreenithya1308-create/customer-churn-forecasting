import os
import streamlit as st
import pandas as pd
import json
from google.cloud import aiplatform, bigquery
from dotenv import load_dotenv

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()  # Load from .env locally
# GOOGLE_APPLICATION_CREDENTIALS should point to your JSON key
# e.g., export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service_account.json"

# -----------------------------
# Load config (safe, non-secret info)
# -----------------------------
with open('config.json') as f:
    config = json.load(f)

# -----------------------------
# Streamlit page settings
# -----------------------------
st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

# Gradient background
st.markdown(f"""
<style>
body {{
    background: linear-gradient(135deg, {config['colors'][0]}, {config['colors'][1]}, {config['colors'][2]});
    color: lightblue;
}}
</style>
""", unsafe_allow_html=True)

st.title("Customer Churn Prediction")

# -----------------------------
# CSV Upload
# -----------------------------
uploaded_file = st.file_uploader("Upload CSV for batch prediction", type="csv")
if uploaded_file:
    try:
        # Read CSV
        data = pd.read_csv(uploaded_file)
        st.subheader("Input data preview")
        st.dataframe(data.head())

        # -----------------------------
        # Column type handling
        # -----------------------------
        string_columns = [
            'AccountWeeks', 'ContractRenewal', 'DataPlan',
            'CustServCalls', 'DayCalls', 'MaritalStatus'
        ]
        numeric_columns = [
            'DataUsage', 'RoamMins', 'MonthlyCharge', 'OverageFee'
        ]

        for col in string_columns:
            if col in data.columns:
                data[col] = data[col].astype(str)

        for col in numeric_columns:
            if col in data.columns:
                data[col] = pd.to_numeric(data[col], errors='raise')

        # -----------------------------
        # Vertex AI prediction
        # -----------------------------
        # Credentials are picked automatically from environment
        aiplatform.init(
            project=config['project_id'],
            location=config['region']
        )
        endpoint = aiplatform.Endpoint(config['endpoint_id'])

        raw_predictions = endpoint.predict(
            instances=data.to_dict(orient='records')
        ).predictions

        # -----------------------------
        # Map predictions to "Churn"/"No Churn"
        # -----------------------------
        def map_prediction(pred):
            try:
                max_index = pred['scores'].index(max(pred['scores']))
                predicted_class = pred['classes'][max_index]
                return "Churn" if predicted_class == "1" else "No Churn"
            except:
                return "Unknown"

        data['prediction'] = [map_prediction(p) for p in raw_predictions]

        # -----------------------------
        # Display results
        # -----------------------------
        st.subheader("Predictions per row")
        st.dataframe(data)

        st.subheader("Prediction summary")
        summary = data['prediction'].value_counts(normalize=True) * 100
        summary_df = pd.DataFrame({
            'Category': summary.index,
            'Percentage': summary.values
        })
        st.dataframe(summary_df)
        st.bar_chart(summary_df.set_index('Category')['Percentage'])

        # -----------------------------
        # Store results to BigQuery
        # -----------------------------
        bq_client = bigquery.Client(project=config['project_id'])
        table_id = f"{config['project_id']}.churn_dataset.predictions_table"
        data['prediction_time'] = pd.Timestamp.now()
        job = bq_client.load_table_from_dataframe(data, table_id)
        job.result()

    except Exception as e:
        st.error(f"Prediction request failed: {e}")
