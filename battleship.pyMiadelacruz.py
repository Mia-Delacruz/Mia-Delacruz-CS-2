'''
*/
mia_delacruz 
Function: 
bugs: indentation that at first would not run my code 
Log 1.0 M
'''

import os
import random           #import os and time because import random is not being used 
import time


def print_board(board):
    '''
    Args:
        variable(type): Description of variable. prints board set up for user to play inclduing vertical and horizantal lines 
    Returns:
        variable(type): returns the board set up for users to play 
    Raises:
        Error: none 
    Description: displays board for battleship players 
'''    

    print('   1    2    3    4    5')
    print(f'1 {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]}')                   #prints the board set up with vertical and horizntal lines for players to use and play battle ship on 
    print(f'2 {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} | {board[1][4]}')
    print(f'3 {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]}')
    print(f'4 {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]}')
    print(f'5 {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]}')


def get_space(board): 
    '''
    Args:
        variable(type): Description of variable. prints board set up for user to play inclduing vertical and horizantal lines 
    Returns:
        variable(type): returns the board set up for users to play 
    Raises:
        Error: none 
    Description: returns board to play TTT 
    '''
    while True:
        try:
            row = int(input('Enter row: ')) - 1
            column = int(input('Enter column: ')) - 1 

            if row >= 0 and row < 5 and column >= 0 and column < 5 and board[row][column] == '⚓':       #use wave when board spot is empty and available for ship 
                return row, column
                
        except ValueError: 
            print('Please enter an integer')        #if number not used tell user to use enter an integer 


def place_ships(board):
    '''
    Args:
        variable(type): Description of variable. places ships on selected rows and colums that users pick also uses different emojis to place ships on empty spaces 
    Returns:
        variable(type): places ship emoji on empty wave emoji and when hit returns a spark emoji 
    Raises:
        Error: none 
    Description: places ships on selected spot on board 
    '''
    for i in range(4):
        print_board(board)
        row, column = get_space(board)
        board[row][column] = '🚢'         #print ship emoji on given row and column that user picks 
    print_board(board)


def take_shot(board, hidden_board, hits):
    print_board(board)
    row, column = get_space(board)

    if hidden_board[row][column] == '🚢':
        print('You got a hit!')
        hits += 1
        board[row][column] = '💥'          #print spark emoji on given row and column when user hits another ship 
    else:
        print('You missed!')
        board[row][column] = '⚓'        #print anchor emoji on given row and column when empty 
    print_board(board)
    return hits


def main():
    '''
    Args:
        variable(type): Description of variable. prints board set up for user to play as well as printed statements 
    Raises:
        Error: none 
    Description: displays all hidden and player boards/ also displays text for user to follow instructions 
    '''
    while True:
        p1_board = [['⚓', '⚓', '⚓', '⚓', '⚓'],                                 #print all 4 guesses and hidden boards that players use 
                    ['⚓', '⚓', '⚓', '⚓', '⚓'], 
                    ['⚓', '⚓', '⚓', '⚓', '⚓'], 
                    ['⚓', '⚓', '⚓', '⚓', '⚓'], 
                    ['⚓', '⚓', '⚓', '⚓', '⚓']]
        p2_board = [['⚓', '⚓', '⚓', '⚓', '⚓'], 
                    ['⚓', '⚓', '⚓', '⚓', '⚓'], 
                    ['⚓', '⚓', '⚓', '⚓', '⚓'], 
                    ['⚓', '⚓', '⚓', '⚓', '⚓'], 
                    ['⚓', '⚓', '⚓', '⚓', '⚓']]
        p1_hidden_board = [['⚓', '⚓', '⚓', '⚓', '⚓'], 
                            ['⚓', '⚓', '⚓', '⚓', '⚓'], 
                            ['⚓', '⚓', '⚓', '⚓', '⚓'], 
                            ['⚓', '⚓', '⚓', '⚓', '⚓'], 
                            ['⚓', '⚓', '⚓', '⚓', '⚓']]
        p2_hidden_board = [['⚓', '⚓', '⚓', '⚓', '⚓'], 
                            ['⚓', '⚓', '⚓', '⚓', '⚓'], 
                            ['⚓', '⚓', '⚓', '⚓', '⚓'], 
                            ['⚓', '⚓', '⚓', '⚓', '⚓'], 
                            ['⚓', '⚓', '⚓', '⚓', '⚓']]

        answer = input("Hello friend! Want to play Battle Ship!? Type 'yes' to continue ").lower()

        if answer == 'n':
            print("bye")
            break

        print('Placing ships for player 1...')
        time.sleep(1)                                   #pauses the function for however many seconds are in parenthesis in this case (1)
        place_ships(p1_hidden_board)
        time.sleep(2)
        os.system('cls')
        print('Placing ships for player 2...')
        time.sleep(1)
        place_ships(p2_hidden_board)
        time.sleep(2)
        os.system('cls')

        p1_hits = 0                             #keeping track of number of shots players take 
        p2_hits = 0

        while True:
            print('Player 1, take a shot!')
            time.sleep(1)
            p1_hits = take_shot(p2_board, p2_hidden_board, p1_hits)

            if p1_hits == 4:
                print('Player 1 wins!')
                break

            print('Player 2, take a shot!')
            time.sleep(1)
            p2_hits = take_shot(p1_board, p1_hidden_board, p2_hits)

            if p2_hits == 4:
                print('Player 2 wins!')
                break
main ()
