import pygame

pygame.init()

# Définir la taille de la fenêtre
window_width = 300
window_height = 300
window = pygame.display.set_mode((window_width, window_height))

# Créer une surface
surface_width = 100
surface_height = 100
surface = pygame.Surface((surface_width, surface_height))

# Définir les coordonnées de la surface
surface_x = 200
surface_y = 200

# Créer un rectangle avec les coordonnées de la surface
surface_rect = pygame.Rect(surface_x, surface_y, surface_width, surface_height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Obtenir les coordonnées de la souris
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Obtenir l'état des boutons de la souris
        left_click, middle_click, right_click = pygame.mouse.get_pressed()

        # Vérifier si les coordonnées de la souris se trouvent dans le rectangle de la surface
        if surface_rect.collidepoint(mouse_x, mouse_y) and left_click:
            print("Clic détecté dans la surface !")

    # Dessiner la surface sur la fenêtre
    window.blit(surface, (surface_x, surface_y))

    # Rafraîchir la fenêtre
    pygame.display.update()