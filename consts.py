UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

SOLDIER_START_LOCATION = [0, 0]
SOLDIER_MATRIX_START_LOCATION = (0, 0)

SOLDIER_ROWS = 4
SOLDIER_COLS = 2

PIXEL_SIZE = 17

FLAG_ROWS = 4
FLAG_COLS = 4

MINE_ROWS = 1
MINE_COLS = 3

ROWS_MATRIX = 25
COLS_MATRIX = 50

WINDOW_HEIGHT = 424
WINDOW_WIDTH = 849

RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3

GREEN = (138, 201, 38)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = GREEN
GRASS_IMG = "grass.png"
SOLDIER_IMG = "soldier.png"
SOLDIER_NIGHT_IMG = "soldier_nigth.png"
FLAG_IMG = "flag.png"
MINE_IMG = "mine.png"

# in case of lose
LOSE_MESSAGE = ["You Lost!"]
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = BLACK
LOSE_LOCATION_WIDTH = 0.2 * WINDOW_WIDTH
LOSE_LOCATION_HEIGHT = WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2)

# in case of win
WIN_MESSAGE = ["You Won!"]
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION_WIDTH = 0.2 * WINDOW_WIDTH
WIN_LOCATION_HEIGHT = WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2)

START_MESSEGE = ""
START_FONT_SIZE = LOSE_FONT_SIZE
START_COLOR = (255, 255, 255)
START_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))

start_location = (PIXEL_SIZE * SOLDIER_COLS, PIXEL_SIZE)
FLAG_LOCATION = (WINDOW_WIDTH - (PIXEL_SIZE * FLAG_COLS), WINDOW_HEIGHT - (PIXEL_SIZE * FLAG_ROWS))

FONT_NAME = "Calibri"

GRASS_SIZE = (PIXEL_SIZE * 2, PIXEL_SIZE * 3)
LOCATION_ALL_GRASS = []

ENTER = "enter"

EMPTY = "empty"
MINE = "mine"
FLAG = "flag"

MESSAGE_TEXT_START_GAME = ["Welcome to The Flag game.", "Have Fun!"]
START_MESSAGE_FONT_SIZE = 20
START_MESSAGE_COLOR = (255, 255, 255)
START_MESSAGE_LOCATION_WIDTH = SOLDIER_COLS * PIXEL_SIZE
START_MESSAGE_LOCATION_HEIGHT = PIXEL_SIZE

TIME_WAIT_WIN_OR_LOSE = 3
TIME_WAIT_HIDDEN_SCREEN = 1000
