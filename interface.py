# import
import pygame
import constant


def draw_labyrinthe(laby, avatar, screen, delta_x_y):
    '''Manage the view

    Parameters :
        laby -> the Labyrinth object, created in main line 30
        avatar -> the player object, created in main line 28

    Returns :
        View of the labyrinth from the players point of view
    '''

    picture = pygame.image.load(f"{constant.IMG}base.png")
    picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
    screen.blit(picture_redim, (0, 0))

    # if player is moving horizontally
    # facing to the right
    if delta_x_y == (constant.MOVE_RIGHT, constant.MOVE_HORIZONTALY):
        cell_xp2_y0 = laby.get_cell_by_xy(avatar.pos_x + 2, avatar.pos_y) # pourquoi laby ne semble pas être l'objet passé en paramètre ?
        if cell_xp2_y0.sprite != "":
            picture = pygame.image.load(f"{constant.IMG}{cell_xp2_y0.sprite}-3c.png")
            picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
            screen.blit(picture_redim, (0, 0))
        if cell_xp2_y0.deco != "":
            picture = pygame.image.load(f"{constant.IMG}{cell_xp2_y0.deco}-3c.png")
            picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
            screen.blit(picture_redim, (0, 0))

        cell_xp1_yp1 = laby.get_cell_by_xy(avatar.pos_x + 1,
                                          avatar.pos_y + 1)  # pourquoi laby ne semble pas être l'objet passé en paramètre ?
        if cell_xp1_yp1.sprite != "":
            picture = pygame.image.load(f"{constant.IMG}{cell_xp1_yp1.sprite}-3c.png")
            picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
            screen.blit(picture_redim, (0, 0))
        if cell_xp1_yp1.deco != "":
            picture = pygame.image.load(f"{constant.IMG}{cell_xp1_yp1.deco}-3c.png")
            picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
            screen.blit(picture_redim, (0, 0))

        cell_xp1_ym1 = laby.get_cell_by_xy(avatar.pos_x + 1,
                                          avatar.pos_y - 1)  # pourquoi laby ne semble pas être l'objet passé en paramètre ?
        if cell_xp1_ym1.sprite != "":
            picture = pygame.image.load(f"{constant.IMG}{cell_xp1_ym1.sprite}-3c.png")
            picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
            screen.blit(picture_redim, (0, 0))
        if cell_xp1_yp1.deco != "":
            picture = pygame.image.load(f"{constant.IMG}{cell_xp1_ym1.deco}-3c.png")
            picture_redim = pygame.transform.scale(picture, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
            screen.blit(picture_redim, (0, 0))


    """ old version
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
                    screen.blit(picture_redim, (0, 0))"""

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
