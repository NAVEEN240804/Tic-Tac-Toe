import priorityqueue

def create_board():
    return [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def print_board(board):
    for row in board:
        print(row)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def evaluate(board, player):
    if check_winner(board, player):
        return 1 if player == 'O' else -1
    return 0

def get_possible_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

def heuristic(board, player):
    if check_winner(board, player):
        return 10 if player == 'O' else -10
    if check_winner(board, 'X' if player == 'O' else 'O'):
        return -10 if player == 'O' else 10
    return 0

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def a_star(board, player, depth_limit):
    pq = PriorityQueue()
    pq.put((0, board, (), 0))
    visited = set()

    while not pq.empty():
        _, current_board, move, depth = pq.get()
        board_tuple = tuple(map(tuple, current_board))

        if board_tuple in visited or depth > depth_limit:
            continue
        visited.add(board_tuple)

        if check_winner(current_board, 'O'):
            return move
        if check_winner(current_board, 'X'):
            return move

        for next_move in get_possible_moves(current_board):
            new_board = [row[:] for row in current_board]
            new_board[next_move[0]][next_move[1]] = player

            if player == 'O':
                next_player = 'X'
            else:
                next_player = 'O'

            g_cost = evaluate(new_board, player)
            h_cost = heuristic(new_board, next_player)
            f_cost = g_cost + h_cost

            pq.put((f_cost, new_board, next_move, depth + 1))

    return None

def next_move(board, depth_limit):
    # First priority: Take the center if it's free
    if board[1][1] == ' ':
        return (1, 1)
    
    # Second priority: Block the opponent's winning move
    for move in get_possible_moves(board):
        temp_board = [row[:] for row in board]
        temp_board[move[0]][move[1]] = 'X'  # Assume opponent's move
        if check_winner(temp_board, 'X'):
            return move  # Block this move

    move = a_star(board, 'O', depth_limit)
    return move if move else (0, 0)


                print("\nAI WINS!")
            break
        elif check_draw(board):
            print_board(board)
            print("\nIT'S A DRAW!")
            break
        current_player = ai if current_player == human else human

