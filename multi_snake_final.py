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
SNAKE_COLOR1 = (0, 255, 0)  # Vert pour le joueur 1
SNAKE_COLOR2 = (0, 0, 255)  # Bleu pour le joueur 2
FOOD_COLOR = (255, 0, 0)  # Rouge pour la nourriture

# Cadre de l'arène
FRAME_WIDTH = 10

# Vitesse du jeu
FPS = 10
clock = pygame.time.Clock()

# Serpents et direction initiale
snake1 = [(300, 300), (290, 300), (280, 300)]  # Joueur 1
snake2 = [(100, 100), (90, 100), (80, 100)]  # Joueur 2
direction1 = "RIGHT"
direction2 = "RIGHT"

# Scores
score1, score2 = 0, 0
font = pygame.font.Font(None, 36)

# Nourriture
food = (random.randint(1, (WIDTH - 10) // 10) * 10, random.randint(1, (HEIGHT - 10) // 10) * 10)

# Fonctions pour les directions
moves = {
    "UP": (0, -10),
    "DOWN": (0, 10),
    "LEFT": (-10, 0),
    "RIGHT": (10, 0)
}

# Fonction pour dessiner le score
def draw_score():
    score_text1 = font.render(f"Joueur 1: {score1}", True, WHITE)
    score_text2 = font.render(f"Joueur 2: {score2}", True, WHITE)
    SCREEN.blit(score_text1, (10, 10))
    SCREEN.blit(score_text2, (WIDTH - 180, 10))

# Fonction pour dessiner les serpents et la nourriture
def draw_objects():
    # Dessiner les serpents
    for segment in snake1:
        pygame.draw.rect(SCREEN, SNAKE_COLOR1, (*segment, 10, 10))
    for segment in snake2:
        pygame.draw.rect(SCREEN, SNAKE_COLOR2, (*segment, 10, 10))
    # Dessiner la nourriture
    pygame.draw.rect(SCREEN, FOOD_COLOR, (*food, 10, 10))

# Fonction pour gérer les collisions
def check_collision(snake, head):
    # Collision avec les murs
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    # Collision avec le corps du serpent
    if head in snake[1:]:
        return True
    return False

# Boucle principale
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Contrôle Joueur 1 (Flèches directionnelles)
            if event.key == pygame.K_UP and direction1 != "DOWN":
                direction1 = "UP"
            elif event.key == pygame.K_DOWN and direction1 != "UP":
                direction1 = "DOWN"
            elif event.key == pygame.K_LEFT and direction1 != "RIGHT":
                direction1 = "LEFT"
            elif event.key == pygame.K_RIGHT and direction1 != "LEFT":
                direction1 = "RIGHT"

            # Contrôle Joueur 2 (Touches WASD)
            if event.key == pygame.K_w and direction2 != "DOWN":
                direction2 = "UP"
            elif event.key == pygame.K_s and direction2 != "UP":
                direction2 = "DOWN"

            elif event.key == pygame.K_a and direction2 != "RIGHT":
                direction2 = "LEFT"
            elif event.key == pygame.K_d and direction2 != "LEFT":
                direction2 = "RIGHT"

    # Mettre à jour les positions des serpents
    head1_x, head1_y = snake1[0]
    head2_x, head2_y = snake2[0]
    new_head1 = (head1_x + moves[direction1][0], head1_y + moves[direction1][1])
    new_head2 = (head2_x + moves[direction2][0], head2_y + moves[direction2][1])

    # Vérifier les collisions
    if check_collision(snake1, new_head1) or check_collision(snake2, new_head2):
        pygame.quit()
        sys.exit()

    # Ajouter la nouvelle tête
    snake1.insert(0, new_head1)
    snake2.insert(0, new_head2)

    # Vérifier si les serpents mangent la nourriture
    if new_head1 == food:
        score1 += 1
        food = (random.randint(1, (WIDTH - 10) // 10) * 10, random.randint(1, (HEIGHT - 10) // 10) * 10)
    else:
        snake1.pop()  # Supprimer la queue si aucune nourriture n'est mangée

    if new_head2 == food:
        score2 += 1
        food = (random.randint(1, (WIDTH - 10) // 10) * 10, random.randint(1, (HEIGHT - 10) // 10) * 10)
    else:
        snake2.pop()

    # Mise à jour de l'écran
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, WHITE, (0, 0, WIDTH, HEIGHT), FRAME_WIDTH)  # Cadre
    draw_objects()  # Dessiner serpents et nourriture
    draw_score()  # Afficher les scores

    pygame.display.flip()
    clock.tick(FPS)  # Contrôler la vitesse du jeu
