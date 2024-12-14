import pygame
import sys
import random

# Initialisation
pygame.init()
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multi-Snake")

# Couleurs
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
SNAKE1_COLOR, SNAKE2_COLOR, FOOD_COLOR = (0, 255, 0), (0, 0, 255), (255, 0, 0)

# Serpents et nourriture
snake1 = [(300, 300)]
snake2 = [(100, 100)]
food = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)
dir1, dir2 = "RIGHT", "DOWN"

clock = pygame.time.Clock()
FPS = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Contrôles joueur 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: dir1 = "UP"
            elif event.key == pygame.K_DOWN: dir1 = "DOWN"
            elif event.key == pygame.K_LEFT: dir1 = "LEFT"
            elif event.key == pygame.K_RIGHT: dir1 = "RIGHT"
            # Contrôles joueur 2
            if event.key == pygame.K_w: dir2 = "UP"
            elif event.key == pygame.K_s: dir2 = "DOWN"
            elif event.key == pygame.K_a: dir2 = "LEFT"
            elif event.key == pygame.K_d: dir2 = "RIGHT"

    # Mise à jour positions
    moves = {"UP": (0, -10), "DOWN": (0, 10), "LEFT": (-10, 0), "RIGHT": (10, 0)}
    snake1.insert(0, (snake1[0][0] + moves[dir1][0], snake1[0][1] + moves[dir1][1]))
    snake2.insert(0, (snake2[0][0] + moves[dir2][0], snake2[0][1] + moves[dir2][1]))

    # Gestion de la nourriture
    for snake in [snake1, snake2]:
        if snake[0] == food:
            food = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)
        else:
            snake.pop()

    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, FOOD_COLOR, (*food, 10, 10))
    for seg in snake1: pygame.draw.rect(SCREEN, SNAKE1_COLOR, (*seg, 10, 10))
    for seg in snake2: pygame.draw.rect(SCREEN, SNAKE2_COLOR, (*seg, 10, 10))

    pygame.display.flip()
    clock.tick(FPS)
