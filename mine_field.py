import math
import random
import consts
import soldier

global MINE_FIELD


def create():
    global MINE_FIELD
    MINE_FIELD = []
    for i in range(consts.ROWS_MATRIX):
        MINE_FIELD.append([])
        for j in range(consts.COLS_MATRIX):
            MINE_FIELD[i].append(consts.EMPTY)
    put_mines_randomly_in_matrix()
    define_flag_in_matrix()


def give_random_mine_location():
    mine_row = random.randint(0, consts.ROWS_MATRIX - consts.MINE_ROWS)
    mine_col = random.randint(0, consts.COLS_MATRIX - consts.MINE_COLS)
    mine_matrix_location = (mine_row, mine_col)
    return mine_matrix_location


def check_if_mine_can_be_put(mine_location):
    global MINE_FIELD
    for i in range(consts.MINE_COLS):
        if MINE_FIELD[mine_location[0]][mine_location[1] + i] != consts.EMPTY:
            return False
    return True


def put_mines_randomly_in_matrix():
    global MINE_FIELD
    for i in range(consts.AMOUNT_OF_MINE):
        mine_location = give_random_mine_location()
        while not check_if_mine_can_be_put(mine_location):
            mine_location = give_random_mine_location()
        for k in range(consts.MINE_COLS):
            MINE_FIELD[mine_location[0]][mine_location[1] + k] = consts.MINE

def define_flag_in_matrix():
    global MINE_FIELD
    for i in range(consts.ROWS_MATRIX - consts.FLAG_ROWS, consts.ROWS_MATRIX - 1):
        for j in range(consts.COLS_MATRIX - consts.FLAG_COLS, consts.COLS_MATRIX):
            MINE_FIELD[i][j] = consts.FLAG


def create_mine_location_list():
    mine_locations_list = []
    last_location = [100, 100]
    for row in range(consts.ROWS_MATRIX):
        for col in range(consts.COLS_MATRIX):
            if MINE_FIELD[row][col] == consts.MINE:
                if not col - 1 == last_location[1] and not col - 2 == last_location[1]:
                    mine_locations_list.append((row, col))
                    last_location = [row, col]
    return mine_locations_list


def do_legs_touch_mine():
    global MINE_FIELD
    soldier_legs_location = soldier.location_soldier_legs(MINE_FIELD)
    for leg_location in soldier_legs_location:
        if not MINE_FIELD[leg_location[0]][leg_location[1]] == consts.MINE:
            return False
    return True


def is_lose():
    return do_legs_touch_mine()


def do_body_touch_flag():
    global MINE_FIELD
    soldier_body = soldier.location_soldier_whole_body()
    for cube in range(len(soldier_body) - 4):
        if not MINE_FIELD[soldier_body[cube][0]][soldier_body[cube][1]] == consts.FLAG:
            return False
    return True


def is_win():
    return do_body_touch_flag()
