def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
def check_win(board, player):
    # Check rows, columns and diagonals for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    
    return False
def check_draw(board):
    for row in board:
        if any([spot == " " for spot in row]):
            return False
    return True
def minimax(board, depth, is_maximizing, alpha=-float('inf'), beta=float('inf')):
    if check_win(board, "O"):
        return 1
    if check_win(board, "X"):
        return -1
    if check_draw(board):
        return 0
    
    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval
def best_move(board):
    best_val = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human_player = "X"
    ai_player = "O"
    current_player = human_player
    
    while True:
        print_board(board)
        
        if current_player == human_player:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] != " ":
                print("Invalid move, try again.")
                continue
        else:
            move = best_move(board)
            row, col = move
            print(f"AI chose move: ({row}, {col})")
        
        board[row][col] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = ai_player if current_player == human_player else human_player

if __name__ == "__main__":
    main()
