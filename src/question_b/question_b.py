#write functions here, don't add input('') statements here!
class Stock:


    def __init__(self, symbol, company_name): #constructor
        self.__symbol = str(symbol)
        self.__company_name = str(company_name)
        

    def symbol(self): #return symbol
        return self.__symbol

    def company_name(self): #returns company name
        return self.__company_name
    
    