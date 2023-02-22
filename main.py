import time
import requests

# Huobi Futures & Swap API Endpoint
huobi_endpoint = 'https://api.hbdm.com'
huobi_swap_kline_api = '/swap-ex/market/history/kline'

def construct_kline_request_params(symbol, period, start_time, end_time):
    start_time_epoch = int(time.mktime(time.strptime(start_time, '%Y-%m-%d %H:%M:%S')))
    end_time_epoch = int(time.mktime(time.strptime(end_time, '%Y-%m-%d %H:%M:%S')))

    return {'contract_code': symbol, 'period': period, 'from': start_time_epoch, 'to': end_time_epoch}

def retrieve_kline_data(params):
    response = requests.get(huobi_endpoint + huobi_swap_kline_api, params)
    return response

params = construct_kline_request_params('LTC-USD', '60min', '2023-01-01 00:00:00', '2023-02-01 23:00:00')
response = retrieve_kline_data(params)

print(response)
print(response.json())