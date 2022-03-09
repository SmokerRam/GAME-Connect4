#Libraries
import os

#Constants
equals = ("==================================")
tittle = ('|------------CONNECT 4-----------|')
#To clear the terminal
clear = lambda: os.system('cls')

def chooseColor(op):
    return

def buildBoard(r, c):
    return

def whoWins(op):
    return

def connectFour(op):
    return

def menuGame(op):

    clear()

    #Global Constants
    global player1, player2
    #Constant
    boolean = True

    while boolean:
        try:
            rows = int(input('Please, enter the number of rows for the board: '))
            columns = int(input('Please, enter the number of rows for the board: ')) 

            if (rows < 6) or (columns < 7):
                boolean
                print("\n|--- ERROR: The minimum number of rows and columns is 6x7 ---|\n")

            elif rows == columns:
                print("\n|--- ERROR: The number of rows and columns cannot be equal ---|\n")

            elif (rows < columns) and ((columns - rows) == 1):
                buildBoard(row, columns)
                boolean = False
                print()

            else:
                print('\n|--- ERROR: the number of rows must be one less than the number of columns ---|\n')

        except (ValueError, TypeError, IndexError):
            print("\n|--- ERROR: The data entered is invalid ---|\n")

    #Player vs Player
    if op == 1:

        #Names of players
        player1 = input("Please, enter player 1 name: ")
        print()
        player2 = input("Please, enter player 2 name: ")

        chooseColor(1)

    #Player vs IA
    elif op == 2:

        #Names of players
        player1 = input("Please, enter player 1 name: ")
        print()
        player2 = 'IA'

        chooseColor(2)

    elif op == 3:
        
        clear()

        print(equals)
        print("|------------CONTROLS------------|")
        print(f"{equals}\n")

        print('|--- Each column will be listed ---|')
        print('|--- To insert a tab yo must indicate ---|')
        print('|--- in which column you want to release it. ---|\n')

        print(equals)
        print("|------------GOOD LUCK!----------|")
        print(f"{equals}\n")

        input('Press any key to continue...')
        menu(1)

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
            print(f"{equals}\n")

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

        print("Connect 4 of your checkers in a row while preventing")
        print("your opponent from doing the same. But, look out your opponent")
        print("can sneak up on you and win the game!\n")

        print("Remember, you can win in the following ways:\n")

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
        print(f"{equals}\n")

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