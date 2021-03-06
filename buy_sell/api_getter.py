import requests
import json
from buy_sell.buy_sell_urls import *


def get_okex_data():
    okex_data = requests.get(OKEX_ETH_DATA)
    okex_data_dict = json.loads(okex_data.text)
    return okex_data_dict


def get_binance_data():
    binance_data = requests.get(BINANCE_ETH_DATA, params=BINANCE_ETH_SYMBOL_DICT)
    binance_data_dict = json.loads(binance_data.text)
    return binance_data_dict


def merge():
    okex_data = get_okex_data()
    binance_data = get_binance_data()
    ask_values_okex_raw = [index for index in okex_data['asks']]
    bid_values_okex_raw = [index for index in okex_data['bids']]
    ask_values_binance_raw = [index for index in binance_data['asks']]
    bid_values_binance_raw = [index for index in binance_data['bids']]

    combined_ask_values_raw = ask_values_okex_raw + ask_values_binance_raw
    combined_ask_values_raw.sort()
    combined_bid_values_raw = bid_values_okex_raw + bid_values_binance_raw
    combined_bid_values_raw.sort()
    combined_bid_values_raw.reverse()

    return combined_ask_values_raw, combined_bid_values_raw


def clean_data():
    ask_values_raw, bid_values_raw = merge()
    ask_values = []
    bid_values = []
    """
    since the okex api pulls more data, problems could happen if merging the two loops
    because of different list sizes
    """
    for index in ask_values_raw:
        ask_values_sublist = []
        for i in index:
            ask_values_sublist.append(i.rstrip(".0"))
        ask_values.append(ask_values_sublist)

    for index in bid_values_raw:
        bid_values_sublist = []
        for i in index:
            bid_values_sublist.append(i.rstrip(".0"))
        bid_values.append(bid_values_sublist)

    return ask_values, bid_values

