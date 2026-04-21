def print_board(board):
    print('  1     2     3     4     5  ')
    print(f'1 {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]}')
    print('  ------------------------')
    print(f'2 {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][2]} | {board[1][3]}')
    print('  ------------------------')
    print(f'3 {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]}')
    print('  ------------------------')
    print(f'4 {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]}')
    print('  ------------------------')
    print(f'5 {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]}')


def place_ships(board):
    while True:
        try: 
            row = int(input('Enter ship row: ')) - 1
            column = int(input('Enter ship column: ')) - 1

            if row > 4 or row < 0 or column > 4 or column < 0:
                print('Please enter a valid number')
            elif board[row][column] != '⚓':
                print('Please enter an available spot')
            else:
                board[row][column] = '🚢'
                break
        except ValueError:
            print('Enter integers only')


def take_shot(real_board, display_board, shots):
    while True:
        try: 
            row = int(input('Enter shot row: ')) - 1
            column = int(input('Enter shot column: ')) - 1

            if row > 4 or row < 0 or column > 4 or column < 0:
                print('Please enter a valid number')
            else:
                break
        except ValueError:
            print('Enter integers only')

    if real_board[row][column] == '🚢':
        display_board[row][column] = '🔥'
    else:
        display_board[row][column] = '✖️'
    shots.append((row, column))


def check_winner():
    ''''''
    return False


def main():
    print("INSIDE MAIN GO ")
    
    while True:
        real_board_player1 = [
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5 ]
        
        real_board_player2 = [
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5 ]
        
        display_board_player1 = [
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5 ]
        
        display_board_player2 = [
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5,
            ['⚓']*5 ]

        for i in range(4):
            print(f'Player 1, place ship #{i+1}')
            place_ships(real_board_player1)
            print_board(real_board_player1)

        for i in range(4):
            print(f'Player 2, place ship #{i+1}')
            place_ships(real_board_player2)
            print_board(real_board_player2)
        
        print('Time to take shots!')

        while True:
            print_board(display_board_player2)
            take_shot(real_board_player2, display_board_player2)

            if check_winner():
                print(f'Player player 1 wins!')
                break

            print_board(display_board_player1)
            take_shot(real_board_player1, display_board_player1)

            if check_winner():
                print(f'Player player 2 wins!')
                break
       
main()