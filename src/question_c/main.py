import question_c

#used as tests
#dnaString1 = "asdfffasdf"
#dnaString2 = "asdf"
#dnaString1 = "GAAATATGATAT"
#dnaString2 = "ATAT"

def menu():
    print("Enter 1 to make run DNA program")
    print("Enter 2 to quit program ")


menu()
option = int(input("Please enter a number: "))
print(option)


def mainProgram(option):
    while option != 2:
        if(option == 1):
            print("\nKeep in mind both strands have to be case sensitive. (If one is caps, the other is caps as well)")
            dnaString1 = str(input("Please enter a DNA strand that is greater than 8 characters but less than or equal to 16: "))
            dnaString2 = str(input("Please enter a DNA strand that is exactly 4 characters long: "))
            dnaLen1 = len(dnaString1)
            dnaLen2 = len(dnaString2)
            exitProgram = ""

            if(dnaLen1 > 8 and dnaLen1 <= 16 and dnaLen2 == 4):
                result = question_c.get_most_likely_ancestor_consensus(dnaString1.upper(), dnaString2.upper())
                print(result)
                exitProgram = input("If you want to quit, type yes. If not type something else: ")
                if(exitProgram.upper() == "YES"):
                    break
                else:
                    mainProgram(option)
            else:
                print("PLEASE WRITE YOUR DNA STRAND CORRECTLY.")
                mainProgram(option)
        else:
            print("Value not valid.")
        
        print()
        menu()
        option = int(input("Enter your option: "))
    
    print("\nYou have terminated the program. ")
    exit()



mainProgram(option)