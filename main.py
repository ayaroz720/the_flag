import random
import time

import Database
import Guard
import mine_field
import screen
import soldier
import consts
import pygame
import ast

global time_down
global time_up

global LIST_OF_LOCATION_MINE
state = {
    "state": consts.RUNNING_STATE,
    "soldier_location": None,
    "is_enter": False,
    "is_window_open": True,
    "direction_button": "",
    "number_press": 0,
    "mine_location": None,
    "grass_location": None,
    "longer_than_second": False,
    "up": False,
    "count_while":0
}


def create_list_of_grass_location():
    state["grass_location"] = []
    for i in range(consts.AMOUNT_OF_GRASS):
        location = (random.randint(0, consts.WINDOW_WIDTH - consts.GRASS_SIZE[1]),
                    random.randint(0, consts.WINDOW_HEIGHT - consts.GRASS_SIZE[0]))
        state["grass_location"].append(location)


def handle_user_events():
    global time_down
    global time_up
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False
            state["up"] = False

        if event.type == pygame.KEYDOWN:
            time_down = pygame.time.get_ticks()
            which_direction_chosen(event.key)
            state["up"] = False
        if event.type == pygame.KEYUP:
            time_up = pygame.time.get_ticks()

            if state["number_press"] != 0:
                if time_up - time_down > 1000:
                    state["longer_than_second"] = True
                state["up"] = True


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
        state["number_press"] = 1
    elif event == pygame.K_2:
        state["number_press"] = 2
    elif event == pygame.K_3:
        state["number_press"] = 3
    elif event == pygame.K_4:
        state["number_press"] = 4
    elif event == pygame.K_5:
        state["number_press"] = 5
    elif event == pygame.K_6:
        state["number_press"] = 6
    elif event == pygame.K_7:
        state["number_press"] = 7
    elif event == pygame.K_8:
        state["number_press"] = 8
    elif event == pygame.K_9:
        state["number_press"] = 9


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
    Guard.create_snake()
    mine_field.create()
    soldier.create()
    state["soldier_location"] = soldier.LOCATION_SOLDIER
    LIST_OF_LOCATION_MINE = mine_field.create_mine_location_list()
    state["mine_location"] = LIST_OF_LOCATION_MINE
    state["grass_location"] = consts.LOCATION_ALL_GRASS
    pygame.init()
    create_list_of_grass_location()

    screen.draw_game(state)
    Database.create_database()

    while state["is_window_open"]:
        handle_user_events()

        update_location_soldier(state["direction_button"])
        soldier.LOCATION_SOLDIER = state["soldier_location"]
        if state["up"]:
            if state["number_press"] != 0:
                if state["longer_than_second"]:
                    Database.save_data(state)
                    state["longer_than_second"] = False
                else:
                    update_state = Database.return_previous_game(state)
                    if len(update_state) != 0:
                        state["soldier_location"], state["mine_location"], state["grass_location"] = update_state[
                                                                                                         "location_soldier"], \
                                                                                                     update_state[
                                                                                                         "location_mine"], \
                                                                                                     update_state[
                                                                           "location_grass"]
                        state["soldier_location"] =ast.literal_eval(state["soldier_location"])
                        state["mine_location"] = ast.literal_eval(state["mine_location"])
                        state["grass_location"] = ast.literal_eval(state["grass_location"])

                        mine_field.update_matrix(state["mine_location"])

            state["number_press"] = 0
            state["up"] = False
        state["count_while"] += 1

        if state["count_while"]==Guard.count:
            Guard.update_side()
            Guard.update_location()
            state["count_while"] =0

        if state["is_enter"]:
            screen.draw_game_hidden(state, state["mine_location"])
            state["is_enter"] = False

        if mine_field.is_win():
            final_screen_lose_win(consts.WIN_STATE)

        elif mine_field.is_lose() or Guard.snake_kills_soldier():
            final_screen_lose_win(consts.LOSE_STATE)

        else:
            screen.draw_game(state)
        state["direction_button"] = ""

    pygame.quit()


if __name__ == '__main__':
    main()
