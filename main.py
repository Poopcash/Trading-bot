

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load historical price data for an asset
prices = pd.read_csv('historical_prices.csv')

# Calculate the asset's moving average over a specified period
moving_avg = prices['Close'].rolling(window=20).mean()

# Calculate the asset's standard deviation over the same period
std_dev = prices['Close'].rolling(window=20).std()

# Calculate the upper and lower Bollinger Bands based on the moving average and standard deviation
upper_band = moving_avg + 2 * std_dev
lower_band = moving_avg - 2 * std_dev

# Determine whether the asset's price is currently above or below the upper or lower Bollinger Bands
is_above_upper_band = prices['Close'] > upper_band
is_below_lower_band = prices['Close'] < lower_band

# Buy the asset if its price is below the lower Bollinger Band
# Sell the asset if its price is above the upper Bollinger Band
# Otherwise, hold the asset
positions = np.zeros(len(prices))
for i in range(len(prices)):
    if is_below_lower_band[i]:
        positions[i] = 1
    elif is_above_upper_band[i]:
        positions[i] = -1

# Calculate the daily returns of the strategy
daily_returns = positions * (prices['Close'].pct_change())

# Calculate the cumulative returns of the strategy
cumulative_returns = np.cumprod(1 + daily_returns) - 1

# Plot the cumulative returns of the strategy
plt.plot(cumulative_returns)
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.title('Mean Reversion Trading Strategy')
plt.show()