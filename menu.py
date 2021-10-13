import pygame
import sys
from pygame.locals import *
from classes import Button
import client

main_clock = pygame.time.Clock()

pygame.init()

width = 500
height = 500

pygame.display.set_caption('Dodgeball')
screen = pygame.display.set_mode((width, height))

click = False

bt_w = 100
bt_h = 50

def main_menu():
    while True:

        screen.fill((0, 0, 0))

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
                        elif btn.text == "Exit":
                            pygame.quit()
                            sys.exit()

        pygame.display.update()
        main_clock.tick(60)

def game():
    running = True
    while running:

        screen.fill((0, 0, 0))

        btns = [Button("Main Menu", round(width/2) - bt_w/2, 20, bt_w, bt_h, (255, 255, 255)),
                Button("Join Room", 20, 150, bt_w, bt_h, (255, 255, 255)),
                Button("Back", 100, 150, bt_w, bt_h, (255, 255, 255))]

        for btn in btns:
            btn.draw(screen)

        click = False

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
                        if btn.text == "Main Menu":
                            main_menu()
                        elif btn.text == "Join Room":
                            client.play(screen)
                        elif btn.text == "Back":
                            running = False

        pygame.display.update()
        main_clock.tick(60)

def options():
    running = True

    while running:

        screen.fill((0, 0, 0))

        btns = [Button("Main Menu", round(width/2) - bt_w/2, 20, bt_w, bt_h, (255, 255, 255)),
                Button("Back", 100, 150, bt_w, bt_h, (255, 255, 255))]

        for btn in btns:
            btn.draw(screen)

        click = False

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
                        if btn.text == "Main Menu":
                            main_menu()
                        elif btn.text == "Back":
                            running = False

        pygame.display.update()
        main_clock.tick(60)


main_menu()
