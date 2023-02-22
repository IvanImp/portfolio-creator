# main.py
#
# main program

import pandas as pd
import numpy as np
import huobi
import utils
import models

contracts = ['BTC-USD', 'ETH-USD', 'LTC-USD']
interval = '60min'
start_time = '2023-01-01 00:00:00'
end_time = '2023-02-01 23:00:00'

# Construct close price DataFrame
df = pd.DataFrame()
for c in contracts:
    df[c] = huobi.get_ticker_close_price(
        c, interval, start_time, end_time)


# Sharpe ratio for optimal weights
weights = models.get_optimal_weight(df)
print(weights)
weights = np.array(list(weights.values()))

# portfolio expected return
hourly_return = df.pct_change()
portfolio_return = np.sum(hourly_return.mean() * weights) * 24 * 30
print("portfolio monthly expected return:", utils.to_percent(portfolio_return))

# portfolio variance
portfolio_covariance_matrix = hourly_return.cov() * 24 * 30
portfolio_variance = np.dot(weights, np.dot(
    portfolio_covariance_matrix, weights))
print("portfolio monthly variance:", utils.to_percent(portfolio_variance))

# standard deviation: represents risk/volatility
portfolio_standard_deviation = np.sqrt(portfolio_variance)
print("portfolio monthly standard deviation:",
      utils.to_percent(portfolio_standard_deviation))
