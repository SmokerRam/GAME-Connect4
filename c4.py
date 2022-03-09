#Libraries
import os

#Constants
equals = ("==================================")
tittle = ('|------------CONNECT 4-----------|')
#To clear the terminal
clear = lambda: os.system('cls')

def whoWins(op):
    return
    
def connectFour(op):
    return

def menuGame(op):

    if op == 1:
        return
    
    elif op == 2:
        return

    elif op == 3:
        return

    elif op == 4:
        main()

def menu(op):
    
    #Play
    if op == 1:
        
        clear()

        #True until they choose a valid option
        while True:
            print(equals)
            print(tittle)
            print(f"{equals}\n\n")

            try:
                print("1. Player vs Player")
                print("2. Player vs IA")
                print("3. Controls")
                print("4. Back")

                mode = int(input("\nPlease, choose a mode to continue: "))

                if mode < 1 or mode > 4:
                    print("\n|--- ERROR: The option entered is invalid ---|\n")

                else:
                    menuGame(mode)

            except (ValueError, TypeError, IndexError):
                print("\n|--- ERROR: The data entered is invalid ---|\n")
    
    #Instruccions
    elif op == 2:
        
        clear()

        print(equals)
        print("|-----------INSTRUCCIONS---------|")
        print(f"{equals}\n\n")



        print(equals)
        print("|-----------GOOD LUCK!----------|")
        print(f"{equals}\n")

        input('Press any key to continue...')
        menu(1)

    #Exit
    elif op == 3:
            
        clear()

        print("\n|---- Thanks for playing :D ---|\n\n")
        quit()

def main():
    
    clear()

    #True until they choose a valid option
    while True:  
          
        print(equals)
        print("|---- Welcome to 'Connect 4' ----|")
        print(f"{equals}\n\n")

        try:
            print("1. Play")
            print("2. Instruccions")
            print("3. Exit")

            option = int(input("\nPlease choose a option to continue: "))

            if option < 1 or option > 3:
                print("\n|--- ERROR: The option entered is invalid ---|\n")
            
            else:
                menu(option)

        except (ValueError, TypeError, IndexError):
            print("\n|--- ERROR: The data entered is invalid ---|\n")

main()