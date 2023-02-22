# huobi.py
#
# Handles huobi-related API calls

import utils
import requests
import pandas as pd

# Huobi Futures & Swap API Endpoint
huobi_endpoint = 'https://api.hbdm.com'
huobi_swap_kline_api = '/swap-ex/market/history/kline'


def retrieve_kline_data(params):
    response = requests.get(huobi_endpoint + huobi_swap_kline_api, params)
    return response


def get_ticker_close_price(symbol, interval, start_time, end_time):
    start_time_epoch = utils.to_epoch(start_time)
    end_time_epoch = utils.to_epoch(end_time)

    response = retrieve_kline_data(
        {'contract_code': symbol, 'period': interval, 'from': start_time_epoch, 'to': end_time_epoch})
    response_json = response.json()

    data_frame = pd.DataFrame(response_json['data'])
    return data_frame['close']
