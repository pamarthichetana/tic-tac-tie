import random

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

def display_board(board):
    for row in board:
        print(row)

def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != "X" and board[row][col] != "O":
                free.append((row, col))
    return free

def victory_for(board, sign):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def enter_move(board):
    free = make_list_of_free_fields(board)
    while True:
        move = int(input("Enter your move (1-9): "))
        for row, col in free:
            if board[row][col] == move:
                board[row][col] = "O"
                return

def draw_move(board):
    free = make_list_of_free_fields(board)
    row, col = random.choice(free)
    board[row][col] = "X"

# MAIN GAME LOOP
display_board(board)
while True:
    draw_move(board)
    display_board(board)
    if victory_for(board, "X"):
        print("Computer wins!")
        break
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break
    enter_move(board)
    display_board(board)
    if victory_for(board, "O"):
        print("Human wins!")
        break
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break