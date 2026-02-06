# Model Explanation – Smart Grid Forecasting

## Hidden Markov Model (HMM)
Hidden Markov Models were used to represent hidden grid stress states
such as Low, Medium, and High demand conditions.

### Why HMM?
- Grid stress is not directly observable
- Demand patterns depend on latent system states
- HMM captures transitions between different demand regimes

### Observations
- Power demand values (MW)
- Temperature-driven demand variations

### Hidden States
- Low demand stress
- Medium demand stress
- High demand stress

## System Dynamics Model
System dynamics modeling was used to simulate long-term demand behavior
based on environmental factors like temperature.

This helped visualize:
- Seasonal demand variations
- Feedback loops between temperature and consumption
- Long-term stability of the grid system
