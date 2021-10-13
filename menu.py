import pygame, sys
from pygame.locals import *

main_clock = pygame.time.Clock()

pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 20)

width = 500
height = 500

pygame.display.set_caption('Game Base')
screen = pygame.display.set_mode((width, height))


click = False

class Button:
    def __init__(self, text, x, y, width, height, color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        text = font.render(self.text, 1, (0, 0, 0))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2),
                 self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        # check if coordinates (pos) of mouse are actually on our button
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


def main_menu():
    while True:

        screen.fill((0, 0, 0))

        bt_w = 100
        bt_h = 50

        btns = [Button("Main Menu", round(width/2) - bt_w/2, 20, bt_w, bt_h, (255, 255, 255)),
                Button("Game", 20, 150, bt_w, bt_h, (255, 255, 255)),
                Button("Options", 100, 150, bt_w, bt_h, (255, 255, 255)),
                Button("Exit", 180, 150, bt_w, bt_h, (255, 255, 255))]

        for btn in btns:
            btn.draw(screen)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(mouse_pos):
                        if btn.text == "Game":
                            game()
                        elif btn.text == "Options":
                            options()

        pygame.display.update()
        main_clock.tick(60)

def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        # draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        main_clock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0, 0, 0))

        # draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        main_clock.tick(60)


main_menu()