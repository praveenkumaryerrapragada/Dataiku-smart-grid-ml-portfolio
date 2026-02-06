import numpy as np
import pandas as pd
from hmmlearn import hmm

# Load sample data
data = pd.read_csv("../data/power_demand_temperature.csv")

# Encode temperature levels
temp_mapping = {"Low": 0, "Medium": 1, "High": 2}
data["Temp_Encoded"] = data["Temperature_Level"].map(temp_mapping)

# Observation: Power Demand
observations = data["Power_Demand_MW"].values.reshape(-1, 1)

# Hidden Markov Model
model = hmm.GaussianHMM(
    n_components=3,
    covariance_type="diag",
    n_iter=100
)

# Train model
model.fit(observations)

# Predict hidden states
hidden_states = model.predict(observations)

data["Predicted_State"] = hidden_states

print(data)
