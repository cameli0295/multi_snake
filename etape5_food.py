import pygame
import sys
import random

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
SNAKE_COLOR = (0, 255, 0)  # Vert pour le serpent
FOOD_COLOR = (255, 0, 0)   # Rouge pour la nourriture

# Cadre de l'arène
FRAME_WIDTH = 10

# Initialisation du serpent
snake = [(300, 300), (290, 300), (280, 300)]
direction = "RIGHT"

# Initialisation de la nourriture
food = (random.randint(1, (WIDTH - 10) // 10) * 10, random.randint(1, (HEIGHT - 10) // 10) * 10)

# Horloge pour gérer la vitesse
clock = pygame.time.Clock()
FPS = 10

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mise à jour de la position du serpent
    head_x, head_y = snake[0]
    if direction == "RIGHT":
        new_head = (head_x + 10, head_y)
    elif direction == "LEFT":
        new_head = (head_x - 10, head_y)
    elif direction == "UP":
        new_head = (head_x, head_y - 10)
    elif direction == "DOWN":
        new_head = (head_x, head_y + 10)

    # Ajouter la nouvelle tête
    snake.insert(0, new_head)

    # Vérifier si le serpent mange la nourriture
    if snake[0] == food:
        # Générer une nouvelle nourriture
        food = (random.randint(1, (WIDTH - 10) // 10) * 10, random.randint(1, (HEIGHT - 10) // 10) * 10)
    else:
        # Supprimer la queue si aucune nourriture n'est mangée
        snake.pop()

    # Remplir l'écran avec une couleur de fond
    SCREEN.fill(BLACK)

    # Dessiner un cadre autour de l'arène
    pygame.draw.rect(SCREEN, WHITE, (0, 0, WIDTH, HEIGHT), FRAME_WIDTH)

    # Dessiner le serpent
    for segment in snake:
        pygame.draw.rect(SCREEN, SNAKE_COLOR, (*segment, 10, 10))

    # Dessiner la nourriture
    pygame.draw.rect(SCREEN, FOOD_COLOR, (*food, 10, 10))

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Contrôler la vitesse
    clock.tick(FPS)
