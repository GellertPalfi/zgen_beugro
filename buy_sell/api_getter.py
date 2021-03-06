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
    ask_values_okex = [index for index in okex_data['asks']]
    bid_values_okex = [index for index in okex_data['bids']]
    ask_values_binance = [index for index in binance_data['asks']]
    bid_values_binance = [index for index in binance_data['bids']]

    combined_ask_values = ask_values_okex + ask_values_binance
    combined_ask_values.sort()
    combined_bid_values = bid_values_okex + bid_values_binance
    combined_bid_values.sort()
    combined_bid_values.reverse()

    return combined_ask_values, combined_bid_values


merge()

