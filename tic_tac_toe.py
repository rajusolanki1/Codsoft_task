import math

def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("-" * 9)
    print()

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all(" " not in row for row in board)

def minimax(board, depth, is_max):
    winner = check_winner(board)
    if winner == "O":
        return 10 - depth
    if winner == "X":
        return depth - 10
    if is_full(board):
        return 0
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth+1, False))
                    board[i][j] = " "
        return best
    best = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                best = min(best, minimax(board, depth+1, True))
                board[i][j] = " "
    return best

def ai_move(board):
    best_score = -math.inf
    move = (-1,-1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board,0,False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i,j)
    board[move[0]][move[1]] = "O"

def human_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                board[row][col] = "X"
                break
            print("Invalid move!")
        except ValueError:
            print("Enter valid numbers.")

def play():
    board = [[" "]*3 for _ in range(3)]
    print("Tic-Tac-Toe\nYou = X\nAI = O")
    while True:
        print_board(board)
        human_move(board)
        if check_winner(board) == "X":
            print_board(board); print("You Win!"); break
        if is_full(board):
            print_board(board); print("Match Draw!"); break
        ai_move(board)
        if check_winner(board) == "O":
            print_board(board); print("AI Wins!"); break
        if is_full(board):
            print_board(board); print("Match Draw!"); break

if __name__ == "__main__":
    play()
