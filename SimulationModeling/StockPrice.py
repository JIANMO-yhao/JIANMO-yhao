import numpy as np
from dataclasses import dataclass

# Define "Financial Model Class" + "Simulation Class"
@dataclass
class ModelParams:              # Financial Model Class
    S0:float                    # Initial stock price
    muS:float                   # Average annualized return
    sigma:float                 # Annualized volatility
    lambda_:float               # Annualized number of jumps
    probJplus:float             # Annualized positive jump probability
    beta:float                  # Average annualized positive jump intensity
    alpha:float                 # Average annualized negative jump intensity relative multiple
@dataclass
class SimulationParams:         # Simulation Class
    T:float                     # Duration in years (e.g. 1.00)
    N:int                       # Total steps per year (e.g. 365)
    num_paths:int               # Simulation times (e.g. 1)
    seed:int | None = None      # Random Seed (e.g. 88)

# Define input parameters
model = ModelParams(            # Financial Model Class
    S0=100,
    muS=0.12,
    sigma=0.15,
    probJplus=0.3,
    muJ=0.05,
    alpha=1.5,
    lambda_=100
)
simulation = SimulationParams(  # Simulation Class
    T=1,
    N=365,
    num_paths=1,
    seed=88
)

# Define a stock price simulation function
def stock_price_simulation(model, simulation):
    dt = simulation.T / simulation.N                # Unit step length represents the time per year
    print(model.S0)
    return dt

print(stock_price_simulation(model, simulation))    # Simulation test
