class ItemDetails(object):
    
    def __init__(self):
        self.name = None
        self.url = None
        self.quantity = None
        self.price = None

    def getName(self):
        return self.name
    
    def getUrl(self):
        return self.url
    
    def getQuantity(self):
        return self.quantity
    
    def getPrice(self):
        return self.price
    
    def setName(self, name):
        self.name = name
    
    def setUrl(self, url):
        self.url = url
        
    def setQuantity(self, quan):
        self.quantity = quan
        
    def setPrice(self, price):
        self.price = price