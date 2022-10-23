import random
from turtledemo import clock

import pygame
import consts
import os

import soldier

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

grass_image = pygame.image.load(os.path.join("grass.png"))
flag_image = pygame.image.load(os.path.join("flag.png"))
mine_image = pygame.image.load(os.path.join("mine.png"))


def draw_soldier(location, image):
    flag = pygame.transform.scale(image,
                                  (consts.PIXEL_SIZE * consts.SOLDIER_COLS - 1,
                                   consts.PIXEL_SIZE * consts.SOLDIER_ROWS - 1))
    screen.blit(flag, (consts.PIXEL_SIZE * location[1], consts.PIXEL_SIZE * location[0]))


def init_location_all_grass():
    for i in range(20):
        location = (random.randint(0, 800), random.randint(0, 400))
        consts.LOCATION_ALL_GRASS.append(location)


def draw_all_grass():
    for location in consts.LOCATION_ALL_GRASS:
        draw_grass(location)


def draw_grass(location):
    flag = pygame.transform.scale(grass_image, consts.GRASS_SIZE)
    screen.blit(flag, location)


def draw_all_mine(list_of_mines):
    for location_mine in list_of_mines:
        draw_mine(location_mine)


def draw_mine(location):
    flag = pygame.transform.scale(mine_image,
                                  (consts.PIXEL_SIZE * consts.MINE_COLS - 1, consts.PIXEL_SIZE * consts.MINE_ROWS - 1))
    screen.blit(flag, (consts.PIXEL_SIZE * location[1], consts.PIXEL_SIZE * location[0]))


def draw_flag():
    flag = pygame.transform.scale(flag_image,
                                  (consts.PIXEL_SIZE * consts.FLAG_COLS - 1, consts.PIXEL_SIZE * consts.FLAG_ROWS - 1))
    screen.blit(flag, consts.FLAG_LOCATION)


def draw_hidden_matrix(state):
    for col in range(1, 50):
        pygame.draw.rect(screen, consts.GREEN,
                         pygame.Rect((consts.WINDOW_WIDTH / 50) * col, 0, 1, consts.WINDOW_HEIGHT), )
    for row in range(1, 25):
        pygame.draw.line(screen, consts.GREEN, (0, (consts.WINDOW_HEIGHT / 25) * row),
                         (849, (consts.WINDOW_HEIGHT / 25) * row))


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION_WIDTH, consts.LOSE_LOCATION_HEIGHT)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION_WIDTH, consts.WIN_LOCATION_HEIGHT)


def draw_start_game_message():
    draw_message(consts.MESSAGE_TEXT_START_GAME, consts.START_MESSAGE_FONT_SIZE,
                 consts.START_MESSAGE_COLOR, consts.START_MESSAGE_LOCATION_WIDTH, consts.START_MESSAGE_LOCATION_HEIGHT)


def draw_message(message, font_size, color, location_width, location_height):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = []
    for line in message:
        text_img.append(font.render(line, True, color))
    for line in range(len(text_img)):
        screen.blit(text_img[line], (location_width, location_height + (line * consts.PIXEL_SIZE)))


def draw_game_hidden(state, list_of_location_mine):
    screen.fill(consts.BLACK)
    # pygame.draw.rect(screen, consts.GREEN, pygame.Rect(consts.WINDOW_WIDTH/50, 0,1, consts.WINDOW_HEIGHT), )
    # draw_soldier(state["soldier_location"], "soldiernight.png")
    draw_hidden_matrix(state)
    draw_soldier(state["soldier_location"], soldier.img_soldier[1])
    draw_all_mine(list_of_location_mine)
    pygame.display.set_caption("The Flag")
    pygame.display.flip()
    pygame.time.wait(consts.TIME_WAIT_HIDDEN_SCREEN)


def draw_game(state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_all_grass()
    draw_flag()
    draw_start_game_message()
    draw_soldier(state["soldier_location"], soldier.img_soldier[0])
    pygame.display.set_caption("The Flag")

    if state["state"] == consts.LOSE_STATE:
        draw_lose_message()
        #pygame.time.wait(600)

    elif state["state"] == consts.WIN_STATE:
        draw_win_message()
    pygame.display.flip()

