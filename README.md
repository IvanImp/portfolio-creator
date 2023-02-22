# portfolio-creator

A Python program that creates optimal portfolio using historical data from Huobi.com

## Installation
    
- [Python 3.7+](https://www.python.org/downloads/release/python-370/)

## Getting Started

In portfolio-creator directory:

1. run command below to install all necessary libraries

```linux
    pipenv install -r requirements.txt
            
```

2. run command below to run the program
   
```linux
    pipenv run python main.py
```

## Files Structure
- main.py
- huobi.py
- models.py
- utils.py
- README.md
- requirements.txt
- .gitignore
- records/
  - records_xxxxxxxxx.xxxxxx

## Files

### main.py

**Main program**

contracts, interval, start_time, end_time can be tweaked according to need.

``` python
contracts = ['BTC-USD', 'ETH-USD', 'LTC-USD']
interval = '60min'
start_time = '2023-01-01 00:00:00'
end_time = '2023-02-01 23:00:00'

```

### huobi.py

**Handles huobi-related API calls**

- retrieve kline data from huobi
  
    _retrieve_kline_data(params)_

```python
    retrieve_kline_data({'contract_code': 'BTC-USD', 'period': '60min', 'from': 1677073951, 'to': 1677073966})
```

- get ticker's close price in dataframe format
  
    _get_ticker_close_price(symbol, interval, start_time, end_time)_

```python
    get_ticker_hourly_close_price('BTC-USD', '60min', '2023-01-01 00:00:00', '2023-02-01 23:00:00')
```

### models.py

**Functions that are used for analysis and modellings**

- get optimal weights using sharpe ratio from efficient frontier on given dataframe
  
    _get_optimal_weight(dataframe)_

### utils.py

**Utitlies to reduce boilerplate codes**

- convert value to percent
  
    _to_percent(value)_

```python
    to_percent(0.11273)
```

- convert date time (YYYY-MM-DD HH:MM:SS) to epoch
  
    _to_epoch(value)_

```python
    to_epoch("2023-01-01 00:00:00")
```

- create record 

    _create_record(r)_

```python
    create_record("This is a sample record")
```

- exit program with error message

    _exit_program_w_err(err_msg, err)_

## Folder

### records

**records folder** contains all the generated output.
Once the program is run, a record with the name of record__<timestamp> will be created in records directory (will be created if directory does not exist)