import pygame
import sys
from pygame.locals import *
from network import Network
from classes import Player, Button

client_number = 0

bt_w = 100
bt_h = 50

def read_pos(str):  # "45,46" -> (45,46)
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):  # (45,46) -> "45,46"
    return str(tup[0]) + "," + str(tup[1])

# redraw the complete window with new position, layout, display, etc.
def redraw_window(win, player, player2, btns):
    win.fill((0, 0, 0))
    player.draw(win)
    player2.draw(win)
    for btn in btns:
        btn.draw(win)
    pygame.display.update()

def play(win, width, height):
    running = True

    n = Network()
    start_pos = read_pos(n.get_pos())
    p = Player(start_pos[0], start_pos[1], 50, 50, (0, 255, 0))
    p2 = Player(0, 0, 50, 50, (255, 0, 0))
    clock = pygame.time.Clock()

    btns = [Button("Exit", round(width-20) - bt_w/2, 20, bt_w/2, bt_h/2, (255, 255, 255))]

    click = False

    while running:
        clock.tick(60)

        p2_pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2_pos[0]
        p2.y = p2_pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(mouse_pos):
                        if btn.text == "Exit":
                            running = False

        p.move()
        redraw_window(win, p, p2, btns)
