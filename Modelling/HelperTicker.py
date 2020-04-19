import yFinance as yf
import pandas as pd

tickers = ['TSLA']
# edit the tickers to get specific historical prices
startDate = ["2020-04-16"]
todayDate = ["2020-04-18"]
# modify date to get specific price


def getHistoricalPrice():
    return yf.history(period = "max")


def getCurrentPrice():
    return yf.download(tickers, start = startDate, end = todayDate)
