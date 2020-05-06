import pygame as pg
import time, sys

# global vaiables
player = "x"
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
dark = (10, 10, 10)
black = (0, 0, 0)
red = (255, 0, 0)

# board set up
ttt = [None] * 3, [None] * 3, [None] * 3

# starting pygame
pg.init()
fps = 30
clock = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")

# image files
x_img = pg.image.load("x.png")
o_img = pg.image.load("o.png")


# find center of given row or column
def center_x(col):
    return (col + 1) * width / 3 - width / 6

def center_y(row):
    return (row + 1) * height / 3 - height / 6
    

def draw_game():
    screen.fill(white)
    # draw vertical lines
    pg.draw.line(screen, dark, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, dark, (2 * width / 3, 0), (2 * width / 3, height), 7)
    # draw horizontal lines
    pg.draw.line(screen, dark, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, dark, (0, 2 * height / 3), (width, 2 * height / 3), 7)

    draw_status()

def draw_status():
    global draw

    screen.fill(black, (0, 400, 500, 100))

    # determine status message
    message = ""

    if winner is None:
        message = player.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"

    if draw:
        message = "Game Draw!"

    status_font = pg.font.Font(None, 30)
    status_text = status_font.render(message, 1, white)
    status_rect = status_text.get_rect(center = (width / 2, height + 50))
    screen.blit(status_text, status_rect)
    pg.display.update()


def check_win():
    global ttt, winner, draw

    # check for winning rows
    for row in range(0, 3):
        if (ttt[row][0] == ttt[row][1] == ttt[row][2]) and ttt[row][0] is not None:
            winner = ttt[row][0]
            pg.draw.line(screen, red, (0, center_y(row)), (width, center_y(row)), 4)
            break

    # check for winning columns
    for col in range(0, 3):
        if (ttt[0][col] == ttt[1][col] == ttt[2][col]) and ttt[0][col] is not None:
            winner = ttt[0][col]
            pg.draw.line(screen, red, (center_x(col), 0), (center_x(col), height), 4)
            break

    # check for winning diagonals
    if ttt[0][0] == ttt[1][1] == ttt[2][2] and ttt[0][0] is not None:
        winner = ttt[0][0]
        pg.draw.line(screen, red, (0, 0), (width, height), 4)
    if ttt[2][0] == ttt[1][1] == ttt[0][2] and ttt[2][0] is not None:
        winner = ttt[2][0]
        pg.draw.line(screen, red, (0, height), (width, 0), 4)

    if all([all(box) for box in ttt]) and winner is None:
        draw = True

    draw_status()


def draw_player(row, col):
    global ttt, player
    player_img = None

    c_x = center_x(col - 1)
    c_y = center_y(row - 1)
    print(c_x, c_y)

    ttt[row - 1][col - 1] = player

    if player == "x":
        player_img = x_img
        player = "o"
    else:
        player_img = o_img
        player = "x"

    player_rect = player_img.get_rect(center = (c_x, c_y))
    screen.blit(player_img, player_rect)
    pg.display.update()


def get_click():
    # get coords from mouse click
    x, y = pg.mouse.get_pos()

    # find row and column mouse was clicked in
    if x < width * 1 / 3:
        col = 1
    elif x < width * 2 / 3:
        col = 2
    elif x < width * 3 / 3:
        col = 3
    else:
        col = None

    if y < height * 1 / 3:
        row = 1
    elif y < height * 2 / 3:
        row = 2
    elif y < height * 3 / 3:
        row = 3
    else:
        row = None
 
    if row and col and ttt[row - 1][col - 1] is None:
        draw_player(row, col)
        check_win()


def reset_game():
    global ttt, winner, player, draw

    time.sleep(3)
    player = "x"
    draw = False
    winner = None
    ttt = [None] * 3, [None] * 3, [None] * 3
    draw_game()


# actual main game
draw_game()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type is pg.MOUSEBUTTONDOWN:
            get_click()
            if winner or draw:
                reset_game()
        pg.display.update()
        clock.tick(fps)