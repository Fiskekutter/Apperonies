import Test



class stock():
    def __init__(self, ticker="", name="",price=0):
        self.ticker = ticker
        self.name = name
        self.price = price
        
    def setTicker(self, ticker):
        self.ticker = ticker

    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        self.price = price

    def getTicker(self):
        return self.ticker

    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
