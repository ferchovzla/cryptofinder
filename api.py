from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from dotenv import load_dotenv
load_dotenv()
import os

class API_TRADING():
   def __init__(self, symbol):
       self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
       self.parameters = {
         'start':'1',
         'limit':'5000',
         'convert':'USD'
       }
       self.headers = {
         'Accepts': 'application/json',
         'X-CMC_PRO_API_KEY': os.getenv('COIN_MARKET_TOKEN'),
       }
       self.symbol = symbol.upper()       
       self.session = Session()
       self.session.headers.update(self.headers)

   def trading(self):
      try:
         response = self.session.get(self.url, params=self.parameters)
         data = json.loads(response.text)
         #print(data)
         dat = {}
         for i in data["data"]:
             #print(i["symbol"])
             if(i["symbol"] == self.symbol):
                 dat["symbol"] = i["symbol"]
                 dat["name"] = i["name"]
                 dat["last_updated"] = i["last_updated"]
                 dat["price"] ="{:.13f}".format(i["quote"]["USD"]["price"])
                 return json.dumps(dat)
             
      except (ConnectionError, Timeout, TooManyRedirects) as e:
         print(e)
 
