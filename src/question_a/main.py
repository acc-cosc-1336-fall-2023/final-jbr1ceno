import question_a

def menu():
    print("Enter 1 to make a Multiplication Table")
    print("Enter 2 to quit program ")


menu()
option = int(input("Please enter a number: "))


while option != 2:
    if(option == 1):
        num1 = input("Enter the operand: ")
        num2 = 10
        result = question_a.display_multiplication_table(question_a.create_multiplication_table(int(num1),int(num2)))
        #print("The multiplication table for ", num1, "is: ", result)
        exitProgram = input("If you want to quit, type yes. If not type something else: ")
        if(exitProgram.upper() == "YES"):
            break
    else:
        print("Value not valid.")

    print()
    menu()
    option = int(input("Enter your option: "))

print("You have terminated the program. ")