import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Time Series Data Management with Pandas")
print("=" * 60)

# 1. Creating Time Series Data
print("\n1. Creating Time Series Data")
print("-" * 40)

# Create date range
dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
print(f"Date range: {len(dates)} days")

# Create sample time series data
np.random.seed(42)
data = {
    'temperature': np.random.normal(20, 5, len(dates)) + 10 * np.sin(np.linspace(0, 4*np.pi, len(dates))),
    'humidity': np.random.normal(60, 15, len(dates)),
    'sales': np.random.poisson(50, len(dates)) + np.random.randint(0, 30, len(dates)),
    'website_visits': np.random.poisson(1000, len(dates)) * (1 + 0.3 * np.sin(np.linspace(0, 2*np.pi, len(dates))))
}
