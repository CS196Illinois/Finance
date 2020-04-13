from stocker import Stocker
import quandl

#I was unable to get Stocker to work with my quandl api code. I was able to pull data directly from quandl.


quandl.ApiConfig.api_key = 'xZPyY7B-bVbAvcxUbrw6'
#stock = quandl.get('CHRIS/MGEX_IH1', start_date='2020-02-25', end_date='2020-02-28')
#print(stock.head())
data = quandl.get("WIKI/FB")
print(data.head())

#microsoft = Stocker(ticker='WIKI/FB')
#microsoft.plot_stock(start_date=None, end_date=None, stats=['Adj. Close'], plot_type='basic')
#microsoft.predict_future(days=5)

