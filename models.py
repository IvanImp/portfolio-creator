# modals.py
#
# Functions that are used for analysis and modellings

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns


def get_optimal_weight(df):
    # Efficient Frontier
    mu = expected_returns.mean_historical_return(df)
    S = risk_models.sample_cov(df)
    ef = EfficientFrontier(mu, S)
    return ef.max_sharpe()
