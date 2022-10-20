import mine_field
import screen
import soldier
import consts
import pygame
state = {
    "state":consts.RUNNING_STATE,
    "soldier_location":"",
    "is_enter":"",
    "is_window_open": True,
    "direction_button" : ""
}


def is_lose():
    pass


def is_win():
    pass

def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.MOUSEMOTION:
            state["direction_button"]=consts.UP

        elif event.type == pygame.MOUSEBUTTONDOWN:

            screen.draw_game_min()




def update_location_soldier(direction_button, soldier_location ):
    # חריגה מגבולות המסך
    pass


def main():
    pygame.init()
    mine_field.create()
    soldier.create(state["soldier_location"])

    screen.draw_game(state)
    while state["is_window_open"]:
        handle_user_events()

        state["soldier_location"]=update_location_soldier(state["direction_button"], state["soldier_location"])

        if mine_field.is_lose(state["soldier_location"]):
            state["state"] = consts.LOSE_STATE
        # TODO: is_win
        elif mine_field.is_win(state["soldier_location"]):
            state["state"] = consts.WIN_STATE
        screen.draw_game(state)



if __name__ == '__main__':
    main()