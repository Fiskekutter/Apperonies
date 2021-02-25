import tkinter as tk
import time
import requests
import Test as stk
import json
import Stock_Class
import numpy as np

class main():
    
    def __init__(self):
        self.SIZE = "800x800"
        self.window = tk.Tk()
        self.window.geometry(self.SIZE)
        self.counter = tk.IntVar()
        self.var = tk.StringVar()
        self.createWidgets()
        self.updateClock()
        self.timer = self.window.title(self.var.get())
        #self.testImport()
        #self.createTable()
        self.window.mainloop()

    def createText(self, event=None):
        self.counter.set(self.counter.get()+1)

    def createWidgets(self):
        self.greeting = tk.Label(self.window, text="Hello world!").pack()
        self.button = tk.Button(self.window, text="Click", width=20, height=2, command=self.createText).pack()
        self.buttonOpenWindow = tk.Button(self.window, text="Open Window!", width=20, height=2, command=self.openBigWindow).pack()
        self.inputText = tk.Label(self.window, textvariable=str(self.counter)).pack()
        self.entry = tk.Entry().pack()
        self.createMarketButtons()

    def updateClock(self):
        now = time.strftime("%H:%M:%S")
        self.var.set(now)
        self.updateTitle()
        self.window.after(1000, self.updateClock)

    def updateTitle(self):
        self.timer = self.window.title(self.var.get())

    def openBigWindow(self):
        self.bigWindow = tk.Toplevel(self.window)
        self.bigWindow.title("Big Window")
        self.bigWindow.geometry(self.SIZE)
        self.createTable(self.bigWindow)
        #self.bigWindowLabel = tk.Label(self.bigWindow, text="Hello New World!").pack()
        
    def testImport(self):
        #stocks = stk.getStocksJson()
        stocks = stk.getStockInfo("FB")
        for e in stocks:
            x = json.dumps(e, indent=4, separators=(". ", " = "))
            p = x.replace("{","").replace("}","").replace("\"","")
            tk.Label(self.window, text=p).pack()

    def createMarketButtons(self): #todo: make function for buttons
        self.americanMarket = tk.Button(self.window, text="American Market", command=self.openAmericanMarketWindow, width=13).place(x=0,y=0)
        self.danishMarket = tk.Button(self.window, text="Danish Market", command=self.openDanishMarketWindow, width=13).place(x=0,y=30)

    def openAmericanMarketWindow(self):
        print("American Button Works!")
        return 0

    def openDanishMarketWindow(self):
        print("Danish Button Works!")
        return 0
        
    def createTxtFile(self):
        print(0)

    def getStock(self, stockTicker):
        js = stk.getStockInfo(stockTicker)
        return Stock_Class.stock(ticker=js[0]["symbol"],name="Facebook",price=js[0]["lastSalePrice"])

    def createTable(self, window):
        bob = self.getStock("fb")
        arr = np.array([("ticker", bob.ticker),
               ("name", bob.name),
               ("price", bob.price)])
        arrShape = arr.shape
        #print(arrShap)
        for i in range(arrShape[0]):
            for j in range(arrShape[1]):
                self.e = tk.Label(window, text = arr[i][j])
                self.e.grid(row=i, column=j)

Main=main()
