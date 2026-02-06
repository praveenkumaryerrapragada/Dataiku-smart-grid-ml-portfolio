# Dataiku DSS Flow – Smart Grid Forecasting & Anomaly Detection

This document explains the end-to-end Dataiku DSS flow designed for
smart grid power demand forecasting and anomaly detection using sample data.

## 1. Data Sources
The project integrates multiple sample data sources representing:
- Power demand readings
- Temperature conditions (Low / Medium / High)
- Grid sensor measurements (voltage, frequency)
- Simulated outage and maintenance logs

All datasets are dummy/sample data created for demonstration purposes.

## 2. Data Preparation (Dataiku Prepare Recipe)
- Cleaned missing and inconsistent values
- Standardized date and time formats
- Created derived features such as:
  - Demand change percentage
  - Temperature stress indicators
- Prepared time-series ready datasets for modeling

## 3. Feature Engineering
- Encoded temperature levels for ML models
- Aggregated demand data at daily/hourly granularity
- Generated lag features for forecasting use cases

## 4. Machine Learning Models
The following models were evaluated:
- Hidden Markov Model (HMM) for latent grid state detection
- Random Forest for demand pattern learning
- XGBoost for improved forecasting accuracy
- LSTM (conceptual) for time-series behavior modeling

Custom Python code was integrated into Dataiku using code environments.

## 5. Anomaly Detection Logic
- Predicted normal demand behavior
- Flagged anomalies when actual values deviated beyond thresholds
- Identified transitions between normal and high-stress grid states

## 6. Output & Visualization
- Model outputs were written back to Dataiku datasets
- Results were visualized using Power BI dashboards
- Real-time alerting logic was simulated using anomaly flags

## 7. Business Outcome
- Early identification of abnormal demand patterns
- Improved operational visibility
- Simulated 10–15% reduction in unplanned outages through proactive insights
