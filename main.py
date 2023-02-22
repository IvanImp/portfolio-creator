import time
import requests
import pandas as pd
import numpy as np

# Huobi Futures & Swap API Endpoint
huobi_endpoint = 'https://api.hbdm.com'
huobi_swap_kline_api = '/swap-ex/market/history/kline'

ticker_start_date = '2023-01-01 00:00:00'
ticker_end_date = '2023-02-01 23:00:00'

def construct_kline_request_params(symbol, period, start_time, end_time):
    start_time_epoch = int(time.mktime(time.strptime(start_time, '%Y-%m-%d %H:%M:%S')))
    end_time_epoch = int(time.mktime(time.strptime(end_time, '%Y-%m-%d %H:%M:%S')))

    return {'contract_code': symbol, 'period': period, 'from': start_time_epoch, 'to': end_time_epoch}

def retrieve_kline_data(params):
    response = requests.get(huobi_endpoint + huobi_swap_kline_api, params)
    return response

def get_ticker_hourly_close_price(symbol):
    params = construct_kline_request_params(symbol, '60min', ticker_start_date, ticker_end_date)
    response = retrieve_kline_data(params)
    response_json = response.json()
    data_frame = pd.DataFrame(response_json['data'])
    return data_frame['close']

def to_percent(value):
    return str(round(value * 100, 2)) + '%'

df = pd.DataFrame()

df['BTC'] = get_ticker_hourly_close_price('BTC-USD')
df['ETH'] = get_ticker_hourly_close_price('ETH-USD')
df['LTC'] = get_ticker_hourly_close_price('LTC-USD')

weights = np.array([0.3, 0.3, 0.4])

# get hourly return percentage for each ticker
expected_return = df.pct_change()
print("expected return:", expected_return)

# portfolio expected return
portfolio_return = np.sum(expected_return.mean() * weights) * 24 * 30
print("portfolio return:", to_percent(portfolio_return))

portfolio_covariance_matrix = expected_return.cov() * 24 * 30
portfolio_variance = np.dot(weights, np.dot(portfolio_covariance_matrix, weights))
print("portfolio variance:", to_percent(portfolio_variance))

# standard deviation represents risk/volatility
portfolio_standard_deviation = np.sqrt(portfolio_variance)
print("portfolio standard deviation:", to_percent(portfolio_standard_deviation))


#expected_returns = [(close_price_data_frame[i] - close_price_data_frame[i-1]) / close_price_data_frame[i-1] for i in range (1, len(close_price_data_frame))]