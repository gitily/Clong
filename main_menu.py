import pygame
import screen
import colors
import game_fonts

def main_menu():

    # Text for printing

    single_player_color = colors.GRAY
    multi_player_color = colors.GRAY

    chosen_text = 1

    ## GAME LOOP ##
    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            keydown = pygame.key.get_pressed()

            if keydown[pygame.K_DOWN]:
                chosen_text += 1
                print "Pressed down"
            if keydown[pygame.K_UP]:
                chosen_text -= 1
                print "Pressed Up"

        # Logic goes here
        if (chosen_text == 1):
            single_player_color = colors.WHITE
            multi_player_color = colors.GRAY
        if (chosen_text  == 2):
            multi_player_color = colors.WHITE
            single_player_color = colors.GRAY

        single_player = game_fonts.game_font.render("Single Player", 20, single_player_color)
        multi_player = game_fonts.game_font.render("Multiplayer", 20, multi_player_color)


        # Fill the screen
        screen.screen.fill(colors.BLACK)
        # Drawing should go here, before flip and after fill
        screen.screen.blit(single_player, (100,100))
        screen.screen.blit(multi_player, (100,150))
        # Updates contents of entire display
        pygame.display.flip()

main_menu()