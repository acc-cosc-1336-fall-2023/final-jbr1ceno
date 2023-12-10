#write functions here, don't add input('') statements here!
class Stock:

    __file_name = 'stock_file.dat'

    def __init__(self, symbol, company_name):

        __symbol = symbol
        __company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name

    def get_stock_list(self):
        
        in_file = open(self.__file_name, 'r')

        file_contents = in_file.read()

        '''while(line != ''):
            print(file_contents)
            file_contents = in_file.readline()'''


        in_file.close()

        print(file_contents)



    '''def __init__(self, symbol, company_name): #constructor
        self.__symbol = str(symbol)
        self.__company_name = str(company_name)'''