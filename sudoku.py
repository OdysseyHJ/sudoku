


def sudoku_map_fill_check(sudoku_map, x_pos, y_pos, input):
    # check x axis
    for x in range(9):
        if sudoku_map[x][y_pos] == input:
            return False

    # check y axis
    for y in range(9):
        if sudoku_map[x_pos][y] == input:
            return False

    # check square
    x_start = x_pos - (x_pos % 3)
    y_start = y_pos - (y_pos % 3)
    for x in range(x_start, x_start+3):
        for y in range(y_start, y_start+3):
            if sudoku_map[x][y] == input:
                return False

    return True

def  dfs_fill_sudoku_map(sudoku_map, x_pos, y_pos):
    if y_pos == 9:
        return True

    check_res = False
    if sudoku_map[x_pos][y_pos] != 0:
        if x_pos == 8:
            check_res = dfs_fill_sudoku_map(sudoku_map, 0, y_pos+1)
        else:
            check_res = dfs_fill_sudoku_map(sudoku_map, x_pos+1, y_pos)
    else:
        fill_num = 1
        while fill_num < 10 and check_res == False:
            if sudoku_map_fill_check(sudoku_map, x_pos, y_pos, fill_num):
                sudoku_map[x_pos][y_pos] = fill_num
                # print("fill num: ", fill_num)
                if x_pos == 8:
                    check_res = dfs_fill_sudoku_map(sudoku_map, 0, y_pos + 1)
                else:
                    check_res = dfs_fill_sudoku_map(sudoku_map, x_pos + 1, y_pos)

            fill_num += 1

        if check_res == False:
            # print("revert num: ", sudoku_map[x_pos][y_pos])
            sudoku_map[x_pos][y_pos] = 0

    return check_res

def  print_sudoku_map(sudoku_map):
    for line in sudoku_map:
        print(line)