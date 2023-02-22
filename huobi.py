# huobi.py
#
# Handles huobi-related API calls

import utils
import requests
import pandas as pd
import sys

# Huobi Futures & Swap API Endpoint
huobi_endpoint = 'https://api.hbdm.com'
huobi_swap_kline_api = '/swap-ex/market/history/kline'


def retrieve_kline_data(params):

    try:
        response = requests.get(huobi_endpoint + huobi_swap_kline_api, params)
        return response
    except requests.exceptions.HTTPError as errh:
        utils.exit_program_w_err('HTTP Error:', errh)
    except requests.exceptions.ConnectionError as errc:
        utils.exit_program_w_err('Connection Error:', errc)
    except requests.exceptions.Timeout as errt:
        utils.exit_program_w_err('Timeout:', errt)
    except requests.exceptions.RequestException as err:
        utils.exit_program_w_err('Request Exception:', err)


def get_ticker_close_price(symbol, interval, start_time, end_time):
    start_time_epoch = utils.to_epoch(start_time)
    end_time_epoch = utils.to_epoch(end_time)

    response = retrieve_kline_data(
        {'contract_code': symbol, 'period': interval, 'from': start_time_epoch, 'to': end_time_epoch})

    try:
        response_json = response.json()
    except requests.exceptions.JSONDecodeError as errj:
        utils.exit_program_w_err('JSON Decode Error:', errj)

    data_frame = pd.DataFrame(response_json['data'])
    return data_frame['close']
