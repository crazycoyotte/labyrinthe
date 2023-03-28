import pygame
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


def draw_labyrinthe(laby, avatar):
    '''Manage the view

    Parameters :
        laby -> the Labyrinth object
        avatar -> the player object

    Returns :
        View of the labyrinth from the players point of view
    '''

    picture = pygame.image.load(f"{constant.IMG}base.png")
    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
    screen.blit(picture_redim, (0, 0))

    # Loading the lines over and above the player
    line_0y = laby.structure[avatar.pos_y]
    line_m1y = laby.structure[avatar.pos_y - 1]
    line_p1y = laby.structure[avatar.pos_y + 1]
    line_m2y = laby.structure[avatar.pos_y - 2]
    line_p2y = laby.structure[avatar.pos_y + 2]

    # If player is looking up
    if delta_x_y == [constant.MOVE_VERTICALY, constant.MOVE_DOWN]:

        case_p2y_0 = line_p2y[avatar.pos_x]
        for element in case_p2y_0:
            if element != '':
                if element == '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-3c.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))
                else:
                    picture = pygame.image.load(f"{constant.IMG}{element}-3m.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_p1y_m1x = line_p1y[avatar.pos_x - 1]
        for element in case_p1y_m1x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-2d.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_p1y_p1x = line_p1y[avatar.pos_x + 1]
        for element in case_p1y_p1x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-2g.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        # picture = pygame.image.load(f"{constant.IMG}ombrage1.png")
        # screen.blit(picture, (0, constant.MOVE_HORIZONTALY))

        case_p1y_0x = line_p1y[avatar.pos_x]
        for element in case_p1y_0x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-2m.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_0y_p1x = line_0y[avatar.pos_x + 1]
        for element in case_0y_p1x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-1g.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_0y_m1x = line_0y[avatar.pos_x - 1]
        for element in case_0y_m1x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-1d.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

    # If player is looking down
    if delta_x_y == [constant.MOVE_VERTICALY, constant.MOVE_UP]:

        case_m2y_0 = line_m2y[avatar.pos_x]
        for element in case_m2y_0:
            if element != '':
                if element == '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-3c.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))
                else:
                    picture = pygame.image.load(f"{constant.IMG}{element}-3m.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_m1y_m1x = line_m1y[avatar.pos_x + 1]
        for element in case_m1y_m1x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-2d.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_m1y_p1x = line_m1y[avatar.pos_x - 1]
        for element in case_m1y_p1x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-2g.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        # picture = pygame.image.load(f"{constant.IMG}ombrage1.png")
        # screen.blit(picture, (0, constant.MOVE_HORIZONTALY))

        case_m1y_0x = line_m1y[avatar.pos_x]
        for element in case_m1y_0x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-2m.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_0y_p1x = line_0y[avatar.pos_x - 1]
        for element in case_0y_p1x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-1g.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_0y_m1x = line_0y[avatar.pos_x + 1]
        for element in case_0y_m1x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-1d.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

    # If player is looking right
    if delta_x_y == [constant.MOVE_RIGHT, constant.MOVE_HORIZONTALY]:

        case_0y_p2x = line_0y[avatar.pos_x + 2 * delta_x_y[0]]
        for element in case_0y_p2x:
            if element != '':
                if element == '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-3c.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))
                else:
                    picture = pygame.image.load(f"{constant.IMG}{element}-3m.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_m1y_p1x = line_m1y[avatar.pos_x + delta_x_y[0]]
        for element in case_m1y_p1x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-2g.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_p1y_p1x = line_p1y[avatar.pos_x + delta_x_y[0]]
        for element in case_p1y_p1x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-2d.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_0y_p2x = line_0y[avatar.pos_x + delta_x_y[0]]
        for element in case_0y_p2x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-2m.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_m1y_x = line_m1y[avatar.pos_x]
        for element in case_m1y_x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-1g.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_p1y_x = line_p1y[avatar.pos_x]
        for element in case_p1y_x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-1d.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

    # If player is looking left
    if delta_x_y == [constant.MOVE_LEFT, constant.MOVE_HORIZONTALY]:

        case_0y_p2x = line_0y[avatar.pos_x + 2 * delta_x_y[0]]
        for element in case_0y_p2x:
            if element != '':
                if element == '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-3c.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))
                else:
                    picture = pygame.image.load(f"{constant.IMG}{element}-3m.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_m1y_p1x = line_m1y[avatar.pos_x + delta_x_y[0]]
        for element in case_m1y_p1x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-2d.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_p1y_p1x = line_p1y[avatar.pos_x + delta_x_y[0]]
        for element in case_p1y_p1x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-2g.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_0y_p2x = line_0y[avatar.pos_x + delta_x_y[0]]
        for element in case_0y_p2x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-2m.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_m1y_x = line_m1y[avatar.pos_x]
        for element in case_m1y_x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-1d.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

        case_p1y_x = line_p1y[avatar.pos_x]
        for element in case_p1y_x:
            if element != '':
                if element != '0':
                    picture = pygame.image.load(f"{constant.IMG}{element}-1g.png")
                    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
                    screen.blit(picture_redim, (0, 0))

    picture = pygame.image.load(f"{constant.IMG}ombrage1.png")
    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
    screen.blit(picture_redim, (0, 0))

    # Moving arrows
    arrow = pygame.image.load(f"{constant.IMG}arrow-straight.png")
    screen.blit(arrow, ((constant.SCREEN_WIDTH / 2) - (constant.ARROW_WIDTH / 2), (4 * constant.SCREEN_HEIGHT / 5)))
    arrow = pygame.image.load(f"{constant.IMG}arrow-left.png")
    screen.blit(arrow, (((constant.SCREEN_WIDTH / 2) - (constant.ARROW_WIDTH / 2)) - constant.ARROW_WIDTH,
                        (4 * constant.SCREEN_HEIGHT / 5)))
    arrow = pygame.image.load(f"{constant.IMG}arrow-right.png")
    screen.blit(arrow, (((constant.SCREEN_WIDTH / 2) - (constant.ARROW_WIDTH / 2)) + constant.ARROW_WIDTH,
                        (4 * constant.SCREEN_HEIGHT / 5)))

    if avatar.victory:
        victoire_img = pygame.image.load(f"{constant.IMG}victoire.jpg")
        victoire_redim = pygame.transform.scale(victoire_img, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
        screen.blit(victoire_redim, (0, 0))


# Boucle de jeu
running = True
# Effacement de l'écran
screen.fill(constant.WHITE)

# Affichage du labyrinthe
draw_labyrinthe(laby, avatar)

# Mise à jour de l'affichage
pygame.display.flip()
draw_labyrinthe(laby, avatar)
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
            draw_labyrinthe(laby, avatar)

            # Mise à jour de l'affichage
            pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
