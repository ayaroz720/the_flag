import consts
import soldier

global location_snake
global side
global count


def create_snake():
    global location_snake
    global side
    global count
    location_snake = [10, 0]
    side = consts.RIGHT
    count = 15


def update_side():
    global side
    global location_snake
    if side == consts.RIGHT and location_snake[1] >= 48:
        side = consts.LEFT
    elif side == consts.LEFT and location_snake[1] <= 0:
        side = consts.RIGHT


def update_location():
    global side
    global location_snake
    if side == consts.RIGHT:
        location_snake[1] += 1
    else:
        location_snake[1] -= 1

def location_snake_body():
    location_all_body = []
    for row in range(consts.SNAKE_ROWS):
        for col in range(consts.SNAKE_COLS):
            location_all_body.append((location_snake[0] + row, location_snake[1] + col))
    return location_all_body

def snake_kills_soldier():
    location_snake=location_snake_body()
    location_soldier=soldier.location_soldier_whole_body()

    for location in location_soldier:
        if not location in location_snake:
            return False
    return True