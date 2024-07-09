import heuristic

def play():
    board = create_board()
    human = 'X'
    ai = 'O'
    current_player = 'X'

    while True:
        print_board(board)
        if current_player == human:
            print("\nYOUR MOVE:")
            while True:
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))
                    if is_valid_move(board, row, col):
                        board[row][col] = human
                        break
                    else:
                        print("Space already filled or wrong move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number (0-2).")
        else:
            print("\nAI is making a move...")
            move = next_move(board, depth_limit=3)  
            board[move[0]][move[1]] = ai

        if check_winner(board, current_player):
            print_board(board)
            if current_player == human:
                print("\nYOU WIN!")
            else:
                print("\nAI WINS!")
            break
        elif check_draw(board):
            print_board(board)
            print("\nIT'S A DRAW!")
            break
        current_player = ai if current_player == human else human

x = 1
while x == 1:
    play()
    try:
        x = int(input("\nChoose '0' to exit or '1' for new game: "))
    except ValueError:
        print("Invalid input. Exiting the game.")
        break

print("\nGOOD GAME! HOPE TO PLAY AGAIN SOON...")
