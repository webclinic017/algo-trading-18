from os import access
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
from config_var import access_key, secret_key


client = Client(access_key, secret_key)
prices = client.get_all_tickers()

if __name__ == '__main__':
    with open('Data/crypto/ticker_list.txt', 'w') as f:
        for coin in prices:
            if 'USDT' in coin['symbol']:
                f.write(coin['symbol'][:-4] + "\n")
