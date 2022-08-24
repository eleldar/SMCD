#!/usr/bin/env python3
from statistics import quantiles
from random import randint
import csv
from datetime import datetime, timedelta


def get_dicts_list(string):
    '''list of dicts from vosk recogtition'''
    try:
        return eval(string)['result']
    except KeyError:
        return None 


def target_format(data):
    '''Target format string'''
    return " ".join(i['word'] for i in data)


