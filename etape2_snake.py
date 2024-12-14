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
SNAKE_COLOR = (0, 255, 0)  # Couleur verte pour le serpent

# Cadre de l'arène
FRAME_WIDTH = 10

# Initialisation du serpent
snake = [(300, 300), (290, 300), (280, 300)]  # Liste des segments du serpent

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Remplir l'écran avec une couleur de fond
    SCREEN.fill(BLACK)

    # Dessiner un cadre autour de l'arène
    pygame.draw.rect(SCREEN, WHITE, (0, 0, WIDTH, HEIGHT), FRAME_WIDTH)

    # Dessiner le serpent
    for segment in snake:
        pygame.draw.rect(SCREEN, SNAKE_COLOR, (*segment, 10, 10))

    # Mettre à jour l'affichage
    pygame.display.flip()
