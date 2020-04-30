import yfinance as yf
from yahoo_fin import stock_info as si
import pandas as pd

#Use either Zengyong's helpers or mine. Try not to mix them though. If you're unsure which to use,
#then use Zengyong's.

#Zengyong's
def gethistoricalprice(tickers):
    return yf.history(tickers, period="max")


def getcurrentprice(tickers):
    return si.get_live_price(tickers)


#Sid's
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