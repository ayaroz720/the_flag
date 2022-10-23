import pygame

import consts

global LOCATION_SOLDIER
global IMG_SOLDIER


def create():
    global LOCATION_SOLDIER
    global IMG_SOLDIER
    LOCATION_SOLDIER = consts.SOLDIER_START_LOCATION
    IMG_SOLDIER = [pygame.image.load(consts.SOLDIER_IMG), pygame.image.load(consts.SOLDIER_NIGHT_IMG)]


def location_soldier_legs(mine_field_matrix):
    location_legs = []
    location_legs.append((LOCATION_SOLDIER[0] + 3, LOCATION_SOLDIER[1] + 1))
    location_legs.append((LOCATION_SOLDIER[0] + 3, LOCATION_SOLDIER[1] + 2))
    return location_legs


def location_soldier_whole_body():
    location_all_body = []
    for row in range(consts.SOLDIER_ROWS):
        for col in range(1,consts.SOLDIER_COLS-1):
            location_all_body.append((LOCATION_SOLDIER[0] + row, LOCATION_SOLDIER[1] + col))
    return location_all_body

    pass


def is_soldier_within_boundries(location, diraction_button):
    if diraction_button == consts.DOWN:
        return location_soldier_legs(location)[0][0] < 24
    elif diraction_button == consts.UP:
        return location[0] > 0
    elif diraction_button == consts.RIGHT:
        return location_soldier_whole_body()[1][1] < 48
    elif diraction_button == consts.LEFT:
        return location[1] > 0
