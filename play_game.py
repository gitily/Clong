import pygame
import colors
import game_fonts
import screen

def play_game(mode):

    # GAME LOOP
    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    screen.screen.fill(colors.WHITE)


    pygame.display.flip()
