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
SNAKE_COLOR = (0, 255, 0)

# Cadre de l'arène
FRAME_WIDTH = 10

# Initialisation du serpent
snake = [(300, 300), (290, 300), (280, 300)]
direction = "RIGHT"

# Horloge pour gérer la vitesse
clock = pygame.time.Clock()
FPS = 10

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mettre à jour la position du serpent
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
    snake.pop()

    # Vérifier la collision avec les murs
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        print("Collision avec un mur ! Fin du jeu.")
        pygame.quit()
        sys.exit()

    # Vérifier la collision avec le corps
    if new_head in snake[1:]:
        print("Collision avec le corps ! Fin du jeu.")
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

    # Contrôler la vitesse
    clock.tick(FPS)
