import yfinance as yf
from yahoo_fin import stock_info as si
import pandas as pd


def gethistoricalprice(tickers):
    return yf.history(tickers, period="max")


def getcurrentprice(tickers):
    return si.get_live_price(tickers)


# print(getcurrentprice('AMZN'))