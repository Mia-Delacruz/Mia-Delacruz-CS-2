'''
*/
mia_delacruz 
Function: for each function user gets to see the frequency of words in the play macbeth besides fill in words listed belwo 
bugs: were a lot of syntax and indentation that at first would not run my code 
Log 1.0 M
'''

import random

def print_board(board):
    '''
    Args:
        vairable(type): Description of variable. prints board set up for user to play inclduing vertical and horizantal lines 
    Returns:
        variable(type): returns the board set up for users to play 
    Raises:
        Error: none 
    Description: returns board to play TTT 
    '''
    print(f'''  1   2   3
1 {board[0][0]} | {board[0][1]} | {board[0][2]}   
  ---------
2 {board[1][0]} | {board[1][1]} | {board[1][2]}
  ---------
3 {board[2][0]} | {board[2][1]} | {board[2][2]}
          ''')

def make_move(board, player): 
    '''
    Args:
        vairable(type): Description of variable. asks user to pick a spot on the board from print board that is between the row and column of 0-3
    Returns:
        variable(type):  returns "x" or "o" on specific spot that user picks 
    Raises:
        Error: if user does not enter an integer board resets and user must try again 
    Description: allows user to pick a spot on the board by entering their chosen row or column 
    '''
    while True:
        try:
            row = int(input('Enter row: ')) - 1
            column = int(input('Enter column: ')) - 1 

            if row >= 0 and row < 3 and column >= 0 and column < 3 and board[row][column] == ' ':
                board[row][column] = player
                break
        except ValueError:
            print('Please enter an integer')
                                                                    

def check_winner(board, player):
    '''
    Args:
        vairable(type): Description of variable. uses elif to list the different win combinations 
    Returns:
        variable(type): returns wins and the possible win outcomes from the board 
    Raises:
        Error:
    Description: returns the wins to player 
    '''
    wins = [
            
    ]
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  
        return True
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player: 
        return True
    elif board [0][0] == player and board [0][1] == player and board [0][2] == player: 
        return True 
    elif board [1][0] == player and board [1][1] == player and board [1][2] == player: 
        return True 
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:  
        return True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player: 
        return True
    elif board [0][1] == player and board [1][1] == player and board [2][1] == player: 
        return True 
    elif board [0][2] == player and board [1][2] == player and board [2][2] == player: 
        return True 

    
    
def is_draw(board):
    '''
    Args: 
        vairable(type): if row and collum are taken draw is needed then returns true to user 
    Returns: 
        variable(type): returns draw after all empty spaces are taken 
    Raises:
        Error: 
    Description: if all spaces are taken displays equals a draw to user 
    '''

    space_counter = 0
    status = False

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                space_counter = space_counter + 1

    print("the space counter is: " + str(space_counter))
    if space_counter == 0:
        print("Tie")
        status = True
    return status


def main():
    '''
    Args: 
        vairable(type): Description of variable. displays the empty spaces and the welcome to the user, also allows user to play again 
    Returns:
        variable(type): ask user to play again 
    Raises:
        Error: none 
    Description: under a loop prints board and moves also gives user the option to play game again if not break and code ends 

    '''
    while True: 

        board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

        ttt = ['x', 'o']
        print('Hello player! welcome to Tic Tac Toe!?')

        while True:
            p1_ttt = input('choose x or o: ')

            if p1_ttt == 'x':
                p2_ttt = 'o'
                break
            elif p1_ttt == 'o':
                p2_ttt = 'x'
                break
            else:
                print('Try again')
        
        print_board(board)

        while True:

            make_move(board, p1_ttt)
            print_board(board)

            if is_draw(board):
                
                break
            
            if check_winner(board, p1_ttt):
                print(f'Player {p1_ttt} wins!')
                break

            #player

            make_move(board, p2_ttt)
            print_board(board)
            if is_draw(board):
                print("Tie")
                break
    
            if check_winner(board, p2_ttt):
                print(f'Player {p2_ttt} wins!')
                break

        play_again = input('Do you want to play again?').lower()

        if play_again == 'no':
            break 

        
main()