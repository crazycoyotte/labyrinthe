import pygame
import player
import labyrinthe

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre principale
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Labyrinthe")

# instanciation du joueur
avatar = player.Player()

# instanciation du labyrinthe
laby = labyrinthe.Labyrinthe()

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Polices de caractères
font = pygame.font.SysFont(None, 40)


def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def draw_labyrinthe(laby, avatar):
    # Affichage du labyrinthe

    print_row = -1
    for row in range(avatar.pos_y - 1, avatar.pos_y + 2, 1):
        player_line = laby.structure[avatar.pos_y + print_row]
        print_row += 1
        print_col = 0
        for col in range(avatar.pos_x - 1, avatar.pos_x + 2, 1):
            print_col += 1
            if print_row == 1 and print_col == 2:
                draw_text("☺", BLACK, col * 50 + 20, row * 50 + 10)
            elif player_line[col] == "■":
                pygame.draw.rect(screen, BLACK, (col * 50, row * 50, 50, 50))
            elif player_line[col] == "▢":
                pygame.draw.rect(screen, WHITE, (col * 50, row * 50, 50, 50))


def move(x, y):
    avatar.move2(x, y, laby)


# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move(0, -1)
            elif event.key == pygame.K_DOWN:
                move(0, 1)
            elif event.key == pygame.K_LEFT:
                move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                move(1, 0)

    # Effacement de l'écran
    screen.fill(WHITE)

    # Affichage du labyrinthe
    draw_labyrinthe(laby, avatar)

    # Mise à jour de l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
