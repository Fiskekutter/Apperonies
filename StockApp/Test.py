import requests
import json



def getStockInfo(ticker):
    return requests.get(f"https://api.iextrading.com/1.0/tops?symbols={ticker}").json()

def getStocksJson():
    return requests.get("https://api.iextrading.com/1.0/ref-data/symbols").json()

def getLastPrice(ticker):
    return requests.get(f'https://api.iextrading.com/1.0/tops/last?symbols={ticker}').json()
    
