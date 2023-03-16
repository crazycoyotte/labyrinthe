import pygame
import player
import labyrinthe

# declaration variables
delta_x_y = [1, 0]

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre principale
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Labyrinthe")

# Define click zone
turn_left_zone = pygame.Rect(0, 0, 200, 600)
turn_right_zone = pygame.Rect(600, 0, 200, 600)
go_straight_zone = pygame.Rect(200, 0, 400, 600)

# instanciation du joueur
avatar = player.Player()

# instanciation du labyrinthe
laby = labyrinthe.Labyrinthe()

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Polices de caractères
font = pygame.font.SysFont(None, 40)


def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def draw_labyrinthe(laby, avatar):
    # Affichage du labyrinthe
    global delta_x_y
    actual_line_0 = laby.structure[avatar.pos_y]
    actual_line_m_1 = laby.structure[avatar.pos_y + delta_x_y[1]]
    actual_line_m_2 = laby.structure[avatar.pos_y + 2 * delta_x_y[1]]
    actual_line_p_1 = laby.structure[avatar.pos_y + 1]

    picture = pygame.image.load("img/base.png")
    screen.blit(picture, (0, 0))

    if delta_x_y == [0, 1]:
        for i in range(1, 3, 1):
            if actual_line_m_2[avatar.pos_x] == str(i):
                picture = pygame.image.load(f"img/{i}-3m.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_m_1[avatar.pos_x + 1] == str(i):
                picture = pygame.image.load(f"img/{i}-2g.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_m_1[avatar.pos_x - 1] == str(i):
                picture = pygame.image.load(f"img/{i}-2d.png")
                screen.blit(picture, (0, 0))
            picture = pygame.image.load("img/ombrage2.png.")
            screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_m_1[avatar.pos_x] == str(i):
                picture = pygame.image.load(f"img/{i}-2m.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_0[avatar.pos_x + 1] == str(i):
                picture = pygame.image.load(f"img/{i}-1g.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_0[avatar.pos_x - 1] == str(i):
                picture = pygame.image.load(f"img/{i}-1d.png")
                screen.blit(picture, (0, 0))
        picture = pygame.image.load("img/ombrage1.png")
        screen.blit(picture, (0, 0))

    if delta_x_y == [0, -1]:
        for i in range(1, 3, 1):
            if actual_line_m_2[avatar.pos_x] == str(i):
                picture = pygame.image.load(f"img/{i}-3m.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_m_1[avatar.pos_x - 1] == str(i):
                picture = pygame.image.load(f"img/{i}-2g.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_m_1[avatar.pos_x + 1] == str(i):
                picture = pygame.image.load(f"img/{i}-2d.png")
                screen.blit(picture, (0, 0))
            picture = pygame.image.load("img/ombrage2.png.")
            screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_m_1[avatar.pos_x] == str(i):
                picture = pygame.image.load(f"img/{i}-2m.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_0[avatar.pos_x - 1] == str(i):
                picture = pygame.image.load(f"img/{i}-1g.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_0[avatar.pos_x + 1] == str(i):
                picture = pygame.image.load(f"img/{i}-1d.png")
                screen.blit(picture, (0, 0))
        picture = pygame.image.load("img/ombrage1.png")
        screen.blit(picture, (0, 0))

    actual_line_m_1 = laby.structure[avatar.pos_y - 1]
    actual_line_0 = laby.structure[avatar.pos_y]
    actual_line_p_1 = laby.structure[avatar.pos_y + 1]
    if delta_x_y == [1, 0]:
        for i in range(1, 3, 1):
            if actual_line_0[avatar.pos_x + 2 * delta_x_y[0]] == str(i):
                picture = pygame.image.load(f"img/{i}-3m.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_m_1[avatar.pos_x + delta_x_y[0]] == str(i):
                picture = pygame.image.load(f"img/{i}-2g.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_p_1[avatar.pos_x + delta_x_y[0]] == str(i):
                picture = pygame.image.load(f"img/{i}-2d.png")
                screen.blit(picture, (0, 0))
            picture = pygame.image.load("img/ombrage2.png")
            screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_0[avatar.pos_x + delta_x_y[0]] == str(i):
                picture = pygame.image.load(f"img/{i}-2m.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_m_1[avatar.pos_x] == str(i):
                picture = pygame.image.load(f"img/{i}-1g.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_p_1[avatar.pos_x] == str(i):
                picture = pygame.image.load(f"img/{i}-1d.png")
                screen.blit(picture, (0, 0))
        picture = pygame.image.load("img/ombrage1.png")
        screen.blit(picture, (0, 0))

    if delta_x_y == [-1, 0]:
        for i in range(1, 3, 1):
            if actual_line_0[avatar.pos_x + 2 * delta_x_y[0]] == str(i):
                picture = pygame.image.load(f"img/{i}-3m.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_p_1[avatar.pos_x + delta_x_y[0]] == str(i):
                picture = pygame.image.load(f"img/{i}-2g.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_m_1[avatar.pos_x + delta_x_y[0]] == str(i):
                picture = pygame.image.load(f"img/{i}-2d.png")
                screen.blit(picture, (0, 0))
            picture = pygame.image.load("img/ombrage2.png")
            screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_0[avatar.pos_x + delta_x_y[0]] == str(i):
                picture = pygame.image.load(f"img/{i}-2m.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_p_1[avatar.pos_x] == str(i):
                picture = pygame.image.load(f"img/{i}-1g.png")
                screen.blit(picture, (0, 0))
        for i in range(1, 3, 1):
            if actual_line_m_1[avatar.pos_x] == str(i):
                picture = pygame.image.load(f"img/{i}-1d.png")
                screen.blit(picture, (0, 0))
        picture = pygame.image.load(f"img/ombrage1.png")
        screen.blit(picture, (0, 0))

    if avatar.victory:
        victoire_img = pygame.image.load("img/victoire.jpg")
        victoire_redim = pygame.transform.scale(victoire_img, (800, 600))
        screen.blit(victoire_redim, (0, 0))


def move(delta_x_y):
    avatar.move2(delta_x_y[0], delta_x_y[1], laby)
    pygame.mixer.music.load('sfx/footsteps.mp3')
    pygame.mixer.music.play()


# Boucle de jeu
running = True
# Effacement de l'écran
screen.fill(WHITE)

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
                move(delta_x_y)
            if turn_left_zone.collidepoint(mouse_x, mouse_y):
                if delta_x_y == [1, 0]:
                    delta_x_y = [0, -1]
                elif delta_x_y == [0, -1]:
                    delta_x_y = [-1, 0]
                elif delta_x_y == [-1, 0]:
                    delta_x_y = [0, 1]
                elif delta_x_y == [0, 1]:
                    delta_x_y = [1, 0]
            if turn_right_zone.collidepoint(mouse_x, mouse_y) and left_click:
                if delta_x_y == [1, 0]:
                    delta_x_y = [0, 1]
                elif delta_x_y == [0, 1]:
                    delta_x_y = [-1, 0]
                elif delta_x_y == [-1, 0]:
                    delta_x_y = [0, -1]
                elif delta_x_y == [0, -1]:
                    delta_x_y = [1, 0]
            left_click_pressed = True
        else:
            left_click_pressed = False

            # Effacement de l'écran
            screen.fill(WHITE)

            # Affichage du labyrinthe
            draw_labyrinthe(laby, avatar)

            # Mise à jour de l'affichage
            pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
