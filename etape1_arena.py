import pygame
import sys

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Titre de la fenêtre
pygame.display.set_caption("Multi-Snake")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Cadre de l'arène
FRAME_WIDTH = 10

# Boucle principale pour afficher l'arène
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Remplir l'écran avec une couleur de fond
    SCREEN.fill(BLACK)

    # Dessiner un cadre autour de l'arène
    pygame.draw.rect(SCREEN, WHITE, (0, 0, WIDTH, HEIGHT), FRAME_WIDTH)

    # Mettre à jour l'affichage
    pygame.display.flip()
