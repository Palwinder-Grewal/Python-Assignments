from sudoku_solver import *

my_sudoku = csv_to_sudoku('my_sudoku.csv')
print('Unsolved: ')
print_sudoku(my_sudoku)

solved = solve_sudoku(my_sudoku)
print('Solved: ')
print_sudoku(my_sudoku)