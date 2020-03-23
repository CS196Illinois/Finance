import pandas as pd
import yfinance as yf
# using pandas and yfinance api

# in yfinance, tickers is the function to get the price change of stock each day
tickers = ["TSLA", "AAPL", "GE", "AMZN"]

# the range of data can be adjusted by changing start and the end
yf.download(tickers, start = "2015-01-01", end = "2020-01-01")

# or set name of the stocks in a tuple
# access the tuple by using dot notation

tickers = yf.Tickers('ge goog spce ccl')
tickers.goog.history(period = "2mo")

#other info can be acquired using

# # get stock info
# msft.info
#
# # get historical market data
# hist = msft.history(period="max")
#
# # show actions (dividends, splits)
# msft.actions
#
# # show dividends
# msft.dividends
#
# # show splits
# msft.splits
#
# # show financials
# msft.financials
# msft.quarterly_financials
#
# # show major holders
# stock.major_holders
#
# # show institutional holders
# stock.institutional_holders
#
# # show balance heet
# msft.balance_sheet
# msft.quarterly_balance_sheet
#
# # show cashflow
# msft.cashflow
# msft.quarterly_cashflow
#
# # show earnings
# msft.earnings
# msft.quarterly_earnings
#
# # show sustainability
# msft.sustainability
#
# # show analysts recommendations
# msft.recommendations
#
# # show next event (earnings, etc)
# msft.calendar
#
# # show ISIN code - *experimental*
# # ISIN = International Securities Identification Number
# msft.isin
#
# # show options expirations
# msft.options
#
# # get option chain for specific expiration
# opt = msft.option_chain('YYYY-MM-DD')
# # data available via: opt.calls, opt.puts


