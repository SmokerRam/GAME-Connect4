#Libraries
import os
import random

#Constants
equals = ("==================================")
tittle = ('|------------CONNECT 4-----------|')
data_invalid = ("\n|--- ERROR: The data entered is invalid ---|\n")
#To clear the terminal
clear = lambda: os.system('cls')

def whoWins():
    return False

def whoStart():

    global turn
    who_start = random.randint(0, 3)

    if who_start == 1:
        return 0

    else:
        return 1

def writeBoard(col):
    
    for r in range(rows):
        if board[r][col - 1] == ' ':
            board[r][col - 1] = turn
            break
        else:
            continue

def validColumn(col):

    if col > 0 and col < columns + 1:
        return True

    else:
        return False

def printBoard():

    for c in range(columns):
        print(f" ({c + 1})", end='')

    print("\n")

    for r in range(rows-1, -1, -1):
        print("|", end='')
        for c in range(columns):
            print(f" {board[r][c]} |", end='')
        print()

    print(f"{'-' * ((5 * columns) - 6)}\n")

def buildBoard(r, c):
    global board

    board = [[' ' for _ in range(c)] for _ in range(r)]

def chooseColor(op):

    clear()

    global piece_p1, piece_p2
    boolean = True

    print(equals)
    print('|--------------COLORS------------|')
    print(f"{equals}\n")
    
    color = ['red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'grey']

    colors = {
        'red' : '\033[0;31m',
        'green' : '\033[0;32m',
        'yellow': '\033[0;33m',
        'blue' : '\033[0;34m',
        'purple': '\033[0;35m',
        "cyan": '\033[0;36m',
        'grey': '\033[0;37m'
    }

    colors_bg = {
        'red' : '\033[0;37;41m',
        'green' : '\033[0;30;42m',
        'yellow': '\033[0;30;43m',
        'blue' : '\033[0;37;44m',
        'purple': '\033[0;37;45m',
        "cyan": '\033[0;30;46m',
        'grey': '\033[0;30;47m'
    }

    reset = '\033[0;39m'

    for x in colors_bg:
        print(f"{colors_bg[x] + x.upper() + reset}", end=' ')
    
    print('\n')

    if op == 1:
        while boolean:

            try:
                color_p1 = input(f"{player1}, choose a color for your piece: ").lower()

                if color_p1 in colors:

                    piece_p1 = colors[color_p1] + 'O' + reset
                    boolean = False

                else:
                    print("\n|--- ERROR: the entered color is not available ---|\n")

            except (ValueError, TypeError, IndexError):
                print(data_invalid)

        boolean = True

        while boolean:

            try:
                color_p2 = input(f"{player2}, choose a color for your piece: ").lower()

                if color_p2 == color_p1:
                    print("\n|--- ERROR: the chosen color is already taken, choose another ---|\n")
                
                else:
                    if color_p2 in colors:

                        piece_p2 = colors[color_p2] + 'O' + reset
                        boolean = False

                    else:
                        print("\n|--- ERROR: the entered color is not available ---|\n")

            except (ValueError, TypeError, IndexError):
                print(data_invalid)

    elif op == 2:

        while boolean:

            try:
                color_p1 = input(f"{player1}, choose a color for your piece: ").lower()

                if color_p1 in colors:

                    piece_p1 = colors[color_p1] + 'O' + reset
                    boolean = False

                else:
                    print("\n|--- ERROR: the entered color is not available ---|\n")

            except (ValueError, TypeError, IndexError):
                print(data_invalid)

        color_p2 = color_p1

        while color_p2 == color_p1:
            color_p2 = random.choice(color)
            piece_p2 = colors[color_p2] + 'O' + reset

    clear()
    print(equals)
    print('|--------------COLORS------------|')
    print(f"{equals}\n")

    print(f"\n{player1}, you chose the color: {colors_bg[color_p1] + color_p1.upper() + reset}\n")
    print(f"{player2}, you chose the color: {colors_bg[color_p2] + color_p2.upper() + reset}\n")    

    input('\nPress any key for continue...')
    connectFour(1)

def connectFour(op):
    
    global turn

    clear()

    print(equals)
    print(tittle)
    print(f"{equals}\n")

    if whoStart() == 0:

        turn = piece_p1

        print(f"|{'-' * columns} {player1}: {piece_p1} | {player2}: {piece_p2} {'-' * columns}|\n")

        printBoard()

        column = int(input(f'Please {player1}, select a column: '))

        while validColumn(column) is False:
            column = int(input(f'Please {player1}, select a column: '))

        writeBoard(column)
        turn = piece_p2

    else:

        turn = piece_p2

        print(f"|{'-' * columns} {player1}: {piece_p1} | {player2}: {piece_p2} {'-' * columns}|\n")

        printBoard()

        column = int(input(f'Please {player2}, select a column: '))

        while validColumn(column) is False:
            column = int(input(f'Please {player2}, select a column: '))

        writeBoard(column)
        turn = piece_p1

    while whoWins() is False:

        clear()
        printBoard()

        if turn == piece_p1:

            column = int(input(f'Please {player1}, select a column: '))

            while validColumn(column) is False:
                column = int(input(f'Please {player1}, select a column: '))

            writeBoard(column)
            turn = piece_p2

        else:

            column = int(input(f'Please {player2}, select a column: '))

            while validColumn(column) is False:
                column = int(input(f'Please {player2}, select a column: '))

            writeBoard(column)
            turn = piece_p1

def menuGame(op):

    clear()

    print(equals)
    print(tittle)
    print(f"{equals}\n")

    #Global Constants
    global player1, player2, rows, columns
    #Constant

    boolean = True

    #Player vs Player
    if op == 1:

        while boolean:
            try:
                rows = int(input('Please, enter the number of rows for the board: '))
                columns = int(input('Please, enter the number of columns for the board: ')) 

                if (rows < 6) or (columns < 7):
                    boolean
                    print("\n|--- ERROR: The minimum number of rows and columns is 6x7 ---|\n")

                elif rows == columns:
                    print("\n|--- ERROR: The number of rows and columns cannot be equal ---|\n")

                elif (rows < columns) and ((columns - rows) == 1):
                    buildBoard(rows, columns)
                    boolean = False
                    print()

                else:
                    print('\n|--- ERROR: the number of rows must be one less than the number of columns ---|\n')

            except (ValueError, TypeError, IndexError):
                print(data_invalid)

        #Names of players
        player1 = input("Please, enter player 1 name: ")
        print()
        player2 = input("Please, enter player 2 name: ")

        chooseColor(1)

    #Player vs IA
    elif op == 2:

        while boolean:
            try:
                rows = int(input('Please, enter the number of rows for the board: '))
                columns = int(input('Please, enter the number of columns for the board: ')) 

                if (rows < 6) or (columns < 7):
                    boolean
                    print("\n|--- ERROR: The minimum number of rows and columns is 6x7 ---|\n")

                elif rows == columns:
                    print("\n|--- ERROR: The number of rows and columns cannot be equal ---|\n")

                elif (rows < columns) and ((columns - rows) == 1):
                    buildBoard(rows, columns)
                    boolean = False
                    print()

                else:
                    print('\n|--- ERROR: the number of rows must be one less than the number of columns ---|\n')

            except (ValueError, TypeError, IndexError):
                print(data_invalid)

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
                print(data_invalid)
    
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
            print(data_invalid)

main()