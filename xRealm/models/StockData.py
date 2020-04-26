import yfinance as yf
import pandas as pd

class StockData:
    @staticmethod
    def getCurrentPrice(ticker):
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")["Close"][0]
        return price

    @staticmethod
    def getHistoricalPrices(ticker, time_interval=None):
        per = "1mo"
        if time_interval is None:
            time_interval = "1d"
        elif time_interval is "5m":
            per = "1d"
        elif time_interval is "60m" or time_interval is "1h":
            per = "5d"
        elif time_interval is "1d":
            per = "1mo"
        else:
            per = "max"
        stock = yf.Ticker(ticker)
        price = stock.history(interval=time_interval, period=per)["Close"].to_dict()
        return price
