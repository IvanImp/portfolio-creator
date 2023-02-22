# utils.py
#
# Utilities to reduce boilerplate codes

import time
import sys
import os

record_dir_path = "./records"


def to_percent(value):
    return str(round(value * 100, 2)) + '%'


def to_epoch(value):
    return int(time.mktime(
        time.strptime(value, '%Y-%m-%d %H:%M:%S')))


def create_record(r):
    if not os.path.exists(record_dir_path):
        os.makedirs(record_dir_path)

    record_name = 'record__' + str(time.time())

    with open(os.path.join(record_dir_path, record_name), 'w') as file:
        file.write(r)


def exit_program_w_err(err_msg, err):
    print(err_msg, err)
    sys.exit("Program exited due to exception")
