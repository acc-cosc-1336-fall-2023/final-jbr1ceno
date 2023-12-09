#add import
from question_b import Stock

def stock_purchase_history():
        Apl = Stock("APPL", "Apple Inc")
        Cat = Stock("CAT", "Caterpillar")
        Ek = Stock("EK", "Eastman Kodak")
        Goog = Stock("GOOG", "Google")
        Msft = Stock("MSFT", "Microsoft")

        Stock_list = {Apl.symbol():Apl.company_name(), Cat.symbol():Cat.company_name(),
                       Ek.symbol():Ek.company_name(), Goog.symbol():Goog.company_name(), Msft.symbol():Msft.company_name()} #dictionary
        #print(Stock_list)
        for key in Stock_list:
             print(key, Stock_list[key])



def menu():
    print("1 - Display Stock Purchase History")
    print("2 - Exit")


menu()
option = int(input("Please enter a number: "))


while option != 2:
    if(option == 1):
        result = stock_purchase_history()
        exitProgram = input("If you want to quit, type yes. If not type something else: ")
        if(exitProgram.upper() == "YES"):
            break
    else:
        print("Value not valid.")

    print()
    menu()
    option = int(input("Enter your option: "))

print("You have exited the program. ")