# utils.py
#
# Utilities to reduce boilerplate codes

import time


def to_percent(value):
    return str(round(value * 100, 2)) + '%'


def to_epoch(value):
    return int(time.mktime(
        time.strptime(value, '%Y-%m-%d %H:%M:%S')))
