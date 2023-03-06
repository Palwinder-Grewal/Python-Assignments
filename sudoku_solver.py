import numpy as np

def csv_to_sudoku(file_path):
    sudoku = np.loadtxt(file_path , delimiter = ',').astype(int)
    return sudoku


def print_sudoku(sudoku):
    for row in range (0, 9):
        for col in range (0, 9):
            if col %3 == 0:
                print(end = ' ')
            print(sudoku[row][col], end = ' ')
        if (row+1) %3 == 0:
            print()
        print()


def present_in_row(value, sudoku, row):
    value_present = False
    for i in range(0, 9):
        if sudoku[row][i] == value:
            value_present = True
            return value_present
    return value_present

def present_in_col(value, sudoku, col):
    value_present = False
    for i in range (0, 9):
        if sudoku[i][col] == value:
            value_present = True
            return value_present
    return value_present

def present_in_grid(value, sudoku, row, col):
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    value_present = False
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[row_start + i][col_start + j] == value:
                value_present = True
                return value_present
    return value_present

def is_safe(value, sudoku, row, col):
    box_safe = True
    if present_in_row(value, sudoku, row) or present_in_col(value, sudoku, col) or present_in_grid(value, sudoku, row, col):
        box_safe = False
    return box_safe


def possible_boxes(value, sudoku):
    for i in range (0, 9):
        for j in range(0, 9):
            if is_safe(value, sudoku, i, j):
                print(f'row: {i} col: {j}')


def puzzle_valid(value, sudoku, row, col):    
    for i in range(0, 9):
        if sudoku[row][i] == value and i != col:
            return False
        if sudoku[i][col] == value and i != row:
            return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[row_start + i][col_start + j] == value and (row_start + i != row or col_start + j != col):
                return False
    return True

def validate_puzzle(sudoku):
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] == 0:
                continue
            elif not puzzle_valid(sudoku[i][j], sudoku, i, j):
                return False
    return True

#       UPTO THIS LINE CODE IS WRITTEN WITHOUT ANY HELP OF INTERNET OR ANY OTHER SOURCES


def solve_sudoku(sudoku):       # algorithm of this function is taken from Internet
    if not validate_puzzle(sudoku):
        print('Puzzle not valid')
        return False
    for row in range(0, 9):
        for col in range(0, 9):
            if sudoku[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(num, sudoku, row, col):
                        sudoku[row][col] = num
                        if solve_sudoku(sudoku):
                            return True
                        sudoku[row][col] = 0
                return False
    return True
