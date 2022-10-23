import time

import Database
import mine_field
import screen
import soldier
import consts
import pygame

global LIST_OF_LOCATION_MINE
state = {
    "state": consts.RUNNING_STATE,
    "soldier_location": None,
    "is_enter": False,
    "is_window_open": True,
    "direction_button": "",
    "number_parse":0
}


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False
            print("close")

        if event.type == pygame.KEYDOWN:
            which_direction_chosen(event.key)


def which_direction_chosen(event):
    global LIST_OF_LOCATION_MINE
    if event == pygame.K_UP:
        state["direction_button"] = consts.UP
    elif event == pygame.K_DOWN:
        state["direction_button"] = consts.DOWN
    elif event == pygame.K_RIGHT:
        state["direction_button"] = consts.RIGHT
    elif event == pygame.K_LEFT:
        state["direction_button"] = consts.LEFT
    elif event == pygame.K_RETURN:
        state["is_enter"] = True
    elif event == pygame.K_1:
        state["number_parse"] = 1
    elif event == pygame.K_2:
        state["number_parse"] = 2
    elif event == pygame.K_3:
        state["number_parse"] = 3
    elif event == pygame.K_4:
        state["number_parse"] = 4
    elif event == pygame.K_5:
        state["number_parse"] = 5
    elif event == pygame.K_6:
        state["number_parse"] = 6
    elif event == pygame.K_7:
        state["number_parse"] = 7
    elif event == pygame.K_8:
        state["number_parse"] = 8
    elif event == pygame.K_9:
        state["number_parse"] = 9


def update_location_soldier(direction_button):
    if soldier.is_soldier_within_boundries(state["soldier_location"], direction_button):
        if direction_button == consts.UP:
            state["soldier_location"][0] -= consts.STEP
        elif direction_button == consts.DOWN:
            state["soldier_location"][0] += consts.STEP
        elif direction_button == consts.RIGHT:
            state["soldier_location"][1] += consts.STEP
        elif direction_button == consts.LEFT:
            state["soldier_location"][1] -= consts.STEP


def final_screen_lose_win(state_game):
    state["state"] = state_game
    state["is_window_open"] = False
    screen.draw_game(state)
    time.sleep(consts.TIME_WAIT_WIN_OR_LOSE)


def main():
    global LIST_OF_LOCATION_MINE
    mine_field.create()
    soldier.create()
    state["soldier_location"] = soldier.LOCATION_SOLDIER

    LIST_OF_LOCATION_MINE = mine_field.create_mine_location_list()
    pygame.init()
    screen.init_location_all_grass()
    screen.draw_game(state)

    while state["is_window_open"]:
        handle_user_events()

        update_location_soldier(state["direction_button"])
        soldier.LOCATION_SOLDIER = state["soldier_location"]

        if state["is_enter"]:
            screen.draw_game_hidden(state, LIST_OF_LOCATION_MINE)
            state["is_enter"] = False

        if state["number_parse"] != 0:
            Database.handle_number(state)

        if mine_field.is_win():
            final_screen_lose_win(consts.WIN_STATE)

        elif mine_field.is_lose():
            final_screen_lose_win(consts.LOSE_STATE)

        else:
            screen.draw_game(state)
        state["number_parse"]=0
        state["direction_button"] = ""

    pygame.quit()


if __name__ == '__main__':
    main()
