import pygame
from network import Network
from classes import Player

client_number = 0

def read_pos(str):  # "45,46" -> (45,46)
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):  # (45,46) -> "45,46"
    return str(tup[0]) + "," + str(tup[1])

# redraw the complete window with new position, layout, display, etc.
def redraw_window(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def play(win):
    running = True

    win.fill((0, 0, 0))

    n = Network()
    start_pos = read_pos(n.get_pos())
    p = Player(start_pos[0], start_pos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (255, 0, 0))
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)

        p2_pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2_pos[0]
        p2.y = p2_pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redraw_window(win, p, p2)
