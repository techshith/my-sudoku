#check if the number is good to put it in this cell
def is_valid(board, number, position):
    row, col = position

    # Check row
    for i in range(9):
        if board[row][i] == number and i != col:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == number and i != row:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == number and (start_row + i, start_col + j) != position:
                return False

    return True


#get the location of the empty cell (with zero)
def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)  # return the location of the empty cell
    return None


# solver function using recursion and backtracking
def solve_sudoku(board):
    # end condition:- getting to the end of the board - the function find_empty return NONE
    find = find_empty(board)
    if find is None:  # if there is no empty cell left - board is solved
        return True
    else:
        row, col = find

    for number in range(1, 10):
        if is_valid(board, number, (row, col)):
            board[row][col] = number
            # TODO: need to show it on the GUI

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # backtrack
            # TODO: delete the number in the GUI

    return False