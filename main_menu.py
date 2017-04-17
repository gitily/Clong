import pygame
import screen
import colors
import game_fonts
import play_game



def main_menu():

    # MODES
    # 1 - Main Menu
    # 2 - Single Player

    chosen_text = 1
    mode = 1

    ## GAME LOOP ##
    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            keydown = pygame.key.get_pressed()

            if keydown[pygame.K_DOWN]:
                if chosen_text < 5:
                    chosen_text += 1
                elif chosen_text == 5:
                    chosen_text = 1

            if keydown[pygame.K_UP]:
                if chosen_text > 1:
                    chosen_text -= 1
                elif chosen_text == 1:
                    chosen_text = 5

            if keydown[pygame.K_RETURN]:
                if chosen_text == 1:
                    mode = 2

        if mode == 1:

        # Logic goes here
            single_player_color = colors.GRAY
            multi_player_color = colors.GRAY
            high_scores_color = colors.GRAY
            credits_color = colors.GRAY
            exit_color = colors.GRAY
            colors_list = []
            colors_list.append(single_player_color)
            colors_list.append(multi_player_color)

            if chosen_text == 1:
                single_player_color = colors.WHITE
            elif chosen_text == 2:
                multi_player_color = colors.WHITE
            elif chosen_text == 4:
                credits_color = colors.WHITE
            elif chosen_text == 3:
                high_scores_color = colors.WHITE
            elif chosen_text == 5:
                exit_color = colors.WHITE

            single_player = game_fonts.game_font.render("Single Player", 20, single_player_color)
            multi_player = game_fonts.game_font.render("Multiplayer", 20, multi_player_color)
            high_scores = game_fonts.game_font.render("High Scores", 20, high_scores_color)
            credits = game_fonts.game_font.render("Credits", 20, credits_color)
            exit = game_fonts.game_font.render("Exit ", 20, exit_color)

            # Fill the screen
            screen.screen.fill(colors.BLACK)
            # Drawing should go here, before flip and after fill
            screen.screen.blit(single_player, (100, 100))
            screen.screen.blit(multi_player, (100, 150))
            screen.screen.blit(high_scores, (100, 200))
            screen.screen.blit(credits, (100, 250))
            screen.screen.blit(exit, (100, 300))

            # Updates contents of entire display
            pygame.display.flip()


        elif mode == 2:

            screen.screen.fill(colors.WHITE)
            credits = game_fonts.game_font_2.render("SINGLE PLAYER", 20, colors.BLACK)

            screen.screen.blit(credits, (20,480))
            pygame.display.flip()



main_menu()