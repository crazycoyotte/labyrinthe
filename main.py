import pygame
import interface
import player
import labyrinthe
import constant

# declaration variables
delta_x_y = [constant.MOVE_RIGHT, constant.MOVE_HORIZONTALY]

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre principale
window_size = (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Labyrinthe")

# Define click zone
turn_left_zone = pygame.Rect(((constant.SCREEN_WIDTH / 2) - (constant.ARROW_WIDTH / 2)) - constant.ARROW_WIDTH,
                             (4 * constant.SCREEN_HEIGHT / 5), constant.ARROW_WIDTH, constant.ARROW_HEIGHT)
turn_right_zone = pygame.Rect(((constant.SCREEN_WIDTH / 2) - (constant.ARROW_WIDTH / 2)) + constant.ARROW_WIDTH,
                              (4 * constant.SCREEN_HEIGHT / 5), constant.ARROW_WIDTH, constant.ARROW_HEIGHT)
go_straight_zone = pygame.Rect(((constant.SCREEN_WIDTH / 2) - (constant.ARROW_WIDTH / 2)),
                               (4 * constant.SCREEN_HEIGHT / 5), constant.ARROW_WIDTH, constant.ARROW_HEIGHT)

# instanciation du joueur et du labyrinthe
avatar = player.Player()
laby = labyrinthe.Labyrinthe()

# Polices de caractères
font = pygame.font.SysFont(None, 40)

# Son d'ambiance
pygame.mixer.Channel(0).play(pygame.mixer.Sound(f'{constant.SOUND}Cave.mp3'))

# Boucle de jeu
running = True
# Effacement de l'écran
screen.fill(constant.WHITE)

# Affichage du labyrinthe
interface.draw_labyrinthe(laby, avatar, screen, delta_x_y)

# Mise à jour de l'affichage
pygame.display.flip()

left_click_pressed = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Get mouse coordonates
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Get left click
        left_click, middle_click, right_click = pygame.mouse.get_pressed()
        if left_click and left_click_pressed == False:
            if go_straight_zone.collidepoint(mouse_x, mouse_y):
                avatar.move2(delta_x_y[0], delta_x_y[1], laby)
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(f'{constant.SOUND}footsteps.mp3'))
            if turn_left_zone.collidepoint(mouse_x, mouse_y):
                if delta_x_y == [constant.MOVE_LEFT, constant.MOVE_HORIZONTALY]:
                    delta_x_y = [constant.MOVE_VERTICALY, constant.MOVE_DOWN]
                elif delta_x_y == [constant.MOVE_VERTICALY, constant.MOVE_DOWN]:
                    delta_x_y = [constant.MOVE_RIGHT, constant.MOVE_HORIZONTALY]
                elif delta_x_y == [constant.MOVE_RIGHT, constant.MOVE_HORIZONTALY]:
                    delta_x_y = [constant.MOVE_VERTICALY, constant.MOVE_UP]
                elif delta_x_y == [constant.MOVE_VERTICALY, constant.MOVE_UP]:
                    delta_x_y = [constant.MOVE_LEFT, constant.MOVE_HORIZONTALY]
            if turn_right_zone.collidepoint(mouse_x, mouse_y):
                if delta_x_y == [constant.MOVE_LEFT, constant.MOVE_HORIZONTALY]:
                    delta_x_y = [constant.MOVE_VERTICALY, constant.MOVE_UP]
                elif delta_x_y == [constant.MOVE_VERTICALY, constant.MOVE_UP]:
                    delta_x_y = [constant.MOVE_RIGHT, constant.MOVE_HORIZONTALY]
                elif delta_x_y == [constant.MOVE_RIGHT, constant.MOVE_HORIZONTALY]:
                    delta_x_y = [constant.MOVE_VERTICALY, constant.MOVE_DOWN]
                elif delta_x_y == [constant.MOVE_VERTICALY, constant.MOVE_DOWN]:
                    delta_x_y = [constant.MOVE_LEFT, constant.MOVE_HORIZONTALY]
            left_click_pressed = True
        else:
            left_click_pressed = False

        # Effacement de l'écran
        screen.fill(constant.WHITE)

        # Affichage du labyrinthe
        interface.draw_labyrinthe(laby, avatar, screen, delta_x_y)

        # Mise à jour de l'affichage
        pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
