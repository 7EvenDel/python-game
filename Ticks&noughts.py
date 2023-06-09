def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def is_winner(board, player):
    # Перевірка горизонтальних ліній
    for row in board:
        if row.count(player) == 3:
            return True

    # Перевірка вертикальних ліній
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Перевірка діагоналей
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board(board)
        row = int(input('Enter the row (0-2): '))
        col = int(input('Enter the column (0-2): '))

        if board[row][col] == ' ':
            board[row][col] = current_player
            if is_winner(board, current_player):
                print_board(board)
                print(f'Player {current_player} wins!')
                game_over = True
            elif is_board_full(board):
                print_board(board)
                print('It\'s a tie!')
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Invalid move. Try again.')

play_game()
