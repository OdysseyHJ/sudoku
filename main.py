# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sudoku




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    sudoku_map = [
        [0, 0, 2, 0, 0, 0, 5, 0, 1, ],
        [9, 0, 5, 2, 0, 0, 0, 0, 0, ],
        [0, 6, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 9, 0, 2, 0, 0, 3, ],
        [0, 4, 0, 0, 0, 8, 0, 0, 0, ],
        [0, 0, 6, 0, 7, 0, 2, 0, 0, ],
        [0, 0, 0, 0, 5, 0, 4, 3, 0, ],
        [7, 0, 0, 0, 0, 0, 0, 8, 6, ],
        [0, 9, 0, 3, 0, 6, 0, 0, 0, ],
    ]

    sudoku.dfs_fill_sudoku_map(sudoku_map, 0, 0)
    sudoku.print_sudoku_map(sudoku_map)

