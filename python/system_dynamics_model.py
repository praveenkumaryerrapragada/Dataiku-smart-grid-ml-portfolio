import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 30)

# Temperature impact on demand
temperature_factor = np.sin(time / 5) + 1.5

# Power demand dynamics
base_demand = 800
demand = base_demand * temperature_factor

plt.plot(time, demand)
plt.title("System Dynamics: Power Demand vs Time")
plt.xlabel("Time (Days)")
plt.ylabel("Power Demand (MW)")
plt.show()
