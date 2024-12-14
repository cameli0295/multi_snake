import pygame
import sys
import random

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multi-Snake - Score")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SNAKE1_COLOR = (0, 255, 0)  # Vert pour le joueur 1
SNAKE2_COLOR = (0, 0, 255)  # Bleu pour le joueur 2
FOOD_COLOR = (255, 0, 0)    # Rouge pour la nourriture

# Cadence du jeu
clock = pygame.time.Clock()
FPS = 10

# Serpents et nourriture
snake1 = [(300, 300)]
snake2 = [(100, 100)]
food = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)

# Directions initiales
dir1, dir2 = "RIGHT", "DOWN"

# Scores
score1 = 0
score2 = 0

# Police d'écriture pour les scores
font = pygame.font.Font(None, 36)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Contrôles joueur 1 (flèches)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dir1 != "DOWN":
                dir1 = "UP"
            elif event.key == pygame.K_DOWN and dir1 != "UP":
                dir1 = "DOWN"
            elif event.key == pygame.K_LEFT and dir1 != "RIGHT":
                dir1 = "LEFT"
            elif event.key == pygame.K_RIGHT and dir1 != "LEFT":
                dir1 = "RIGHT"
            
            # Contrôles joueur 2 (WASD)
            if event.key == pygame.K_w and dir2 != "DOWN":
                dir2 = "UP"
            elif event.key == pygame.K_s and dir2 != "UP":
                dir2 = "DOWN"
            elif event.key == pygame.K_a and dir2 != "RIGHT":
                dir2 = "LEFT"
            elif event.key == pygame.K_d and dir2 != "LEFT":
                dir2 = "RIGHT"

    # Mouvements des serpents
    moves = {"UP": (0, -10), "DOWN": (0, 10), "LEFT": (-10, 0), "RIGHT": (10, 0)}
    snake1.insert(0, (snake1[0][0] + moves[dir1][0], snake1[0][1] + moves[dir1][1]))
    snake2.insert(0, (snake2[0][0] + moves[dir2][0], snake2[0][1] + moves[dir2][1]))

    # Vérification si les serpents mangent la nourriture
    if snake1[0] == food:
        score1 += 1
        food = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)
    else:
        snake1.pop()

    if snake2[0] == food:
        score2 += 1
        food = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)
    else:
        snake2.pop()

    # Vérification des collisions avec les bords
    for snake in [snake1, snake2]:
        if snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT:
            pygame.quit()
            sys.exit()

    # Dessin des éléments
    SCREEN.fill(BLACK)

    # Dessin des serpents
    for segment in snake1:
        pygame.draw.rect(SCREEN, SNAKE1_COLOR, (*segment, 10, 10))
    for segment in snake2:
        pygame.draw.rect(SCREEN, SNAKE2_COLOR, (*segment, 10, 10))

    # Dessin de la nourriture
    pygame.draw.rect(SCREEN, FOOD_COLOR, (*food, 10, 10))

    # Affichage des scores
    score_text1 = font.render(f"Joueur 1: {score1}", True, WHITE)
    score_text2 = font.render(f"Joueur 2: {score2}", True, WHITE)
    SCREEN.blit(score_text1, (10, 10))
    SCREEN.blit(score_text2, (WIDTH - 180, 10))

    # Mise à jour de l'affichage
    pygame.display.flip()
    clock.tick(FPS)
