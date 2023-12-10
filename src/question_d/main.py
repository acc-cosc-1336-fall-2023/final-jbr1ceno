from question_d import Stock

stockListView = Stock("MSFT", "Microsoft")

print(stockListView.get_stock_list()) 

def menu():
    print("1- Display stock purchase history ")
    print("2- Exit ")

menu()
option = int(input("Please enter a number: "))

while option != 2:
    if(option == 1):
        returnStockList = stockListView.get_stock_list()
        print(returnStockList)
        exitProgram = input("Type yes to quit. If not type something else: ")
        if(exitProgram.upper() == "YES"):
            break
    else:
        print("Value not valid.")

    print()
    menu()
    option = int(input("Enter your option: "))

print("You have terminated the program. ")
exit()
