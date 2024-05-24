import random

global ROW
global COL
global BOARD


def print_introduction():
    print('What is your name?\n')
    name = input()
    print(f'\nHello {name} ... Let\'s have fun !!! You = X | Computer = O')


def game_setup(rows, cols):
    return [["" for i in range(cols)] for j in range(rows)]


def print_board():
    print('\n _ _ _ _ _ _ _ _ _\n', end='')
    for row in BOARD:
        for index, col in enumerate(row):
            # for GUI
            if index == 0:
                print(f'|', end='')
            if len(col) == 0:
                print(f'     ', end='|')
            else:
                print(f'  {col}  ', end='|')

        print('\n|- - -|- - -|- - -|\n', end='')


def user_plays(turn):

    inputInvalid = True

    while inputInvalid:

        print('Enter X,Y coordinates for your move: ')
        move = input()

        coords = move.split(',')

        if len(coords) != 2:
            print(f'invalid Input. Please enter 2 numbers separated by a comma (x,y).')
        elif not coords[0].isdigit() or not coords[1].isdigit():
            # isdigit is only for string but won't matter here because the console input is string
            print(f'Invalid Input. Please enter 2 integers.')
        else:
            # off by one because array
            row = int(coords[0]) - 1
            col = int(coords[1]) - 1

            if row >= ROW or row < 0 or col >= COL or col < 0:
                print(f'Invalid Input. Please enter numbers between 1-{ROW} for row and 1-{COL} for col.')
            elif len(BOARD[row][col]) == 0:
                BOARD[row][col] = turn
                inputInvalid = False
            else:
                print(f'Invalid Input. This square is not empty')

    return BOARD









def who_won(player):
    for row in range(0, 3):
        # empty squares are blank. First check is to ensure the squares are filled
        if len(f'{BOARD[row][0]}{BOARD[row][1]}{BOARD[row][2]}') == 3:
            if BOARD[row][0] == BOARD[row][1] == BOARD[row][2]:
                if BOARD[row][0] == 'X':
                    return 10
                return -10

    # Check the columns
    for col in range(0, 3):
        # empty squares are blank. First check is to ensure the squares are filled
        if len(f'{BOARD[0][col]}{BOARD[1][col]}{BOARD[2][col]}') == 3:
            if BOARD[0][col] == BOARD[1][col] == BOARD[2][col]:
                if BOARD[0][col] == 'X':
                    return 10
                return -10
    #diagonal
    if len(f'{BOARD[0][0]}{BOARD[1][1]}{BOARD[2][2]}') == 3:
        if BOARD[0][0] == BOARD[1][1] == BOARD[2][2]:
            if BOARD[0][0] == 'X':
                return 10
            return -10
    if len(f'{BOARD[0][2]}{BOARD[1][1]}{BOARD[2][0]}') == 3:
        if BOARD[0][2] == BOARD[1][1] == BOARD[2][0]:
            if BOARD[1][1] == 'X':
                return 10
            return -10

    count = 0
    # if the BOARD is filled up
    for row in BOARD:
        for col in row:
            if len(col) != 0:
                count += 1

    if count == 9:
        return 0

    return -1


if __name__ == '__main__':
    ROW = 3
    COL = 3
    
    BOARD = game_setup(ROW, COL)
    # print_introduction()
    print_board()
    continueGame = -1
    user = 'X'
    while continueGame == -1:
        if user == 'X':
            BOARD = user_plays( user)
            user = 'O'
        else:
            BOARD = user_plays(user)
            user = 'X'
        print_board()
        continueGame = who_won(user)

    print(f'The game is {continueGame}')
