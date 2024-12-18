Compte Rendu : Projet Multi-Snake
1. Objectifs du projet
L'objectif principal de ce projet est d'implémenter une version multi-joueur du jeu classique Snake en Python tout en respectant les règles spécifiées :
1. Maîtriser les concepts de base de la programmation Python.
2. Utiliser le module pygame pour les graphiques et les interactions.
3. Permettre à plusieurs joueurs de participer au jeu.
4. Gérer les fonctionnalités telles que :
   - Les collisions avec les murs ou les autres serpents.
   - L'apparition aléatoire de la nourriture.
   - Le calcul et l'affichage des scores

2. Description détaillée étape par étape
Étape 1 : Création de l'arène

 



Objectif : Créer une fenêtre de jeu avec une arène délimitée par des murs blancs.
Fonctionnalités : La fenêtre mesure 600x600 pixels et l’arène est entourée d’un cadre blanc de 10 pixels.
Code :
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
FRAME_WIDTH = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, WHITE, (0, 0, WIDTH, HEIGHT), FRAME_WIDTH)
    pygame.display.flip()
Étape 2 : Implémentation du serpent
 

Objectif : Afficher un serpent statique constitué de plusieurs segments.
Fonctionnalités : Le serpent est représenté par une liste de coordonnées. Chaque segment est dessiné comme un rectangle vert de 10x10 pixels.
Code :
snake = [(300, 300), (290, 300), (280, 300)]
SNAKE_COLOR = (0, 255, 0)

for segment in snake:
    pygame.draw.rect(SCREEN, SNAKE_COLOR, (*segment, 10, 10))
Étape 3 : Mouvement du serpent
 
Objectif : Déplacer le serpent dans une direction choisie par le joueur.
Fonctionnalités : Le serpent avance dans une direction à chaque itération. Les touches fléchées permettent de changer sa direction.
Code :
direction = "RIGHT"
moves = {"UP": (0, -10), "DOWN": (0, 10), "LEFT": (-10, 0), "RIGHT": (10, 0)}

head_x, head_y = snake[0]
new_head = (head_x + moves[direction][0], head_y + moves[direction][1])
snake.insert(0, new_head)
snake.pop()
Étape 4 : Gestion des collisions
 

Objectif : Détecter les collisions avec les murs et le corps du serpent.
Fonctionnalités : Si le serpent touche un mur ou son propre corps, le jeu se termine.
Code :
if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
    pygame.quit()
    sys.exit()

if new_head in snake[1:]:
    pygame.quit()
    sys.exit()
Étape 5 : Ajout de la nourriture
 
Objectif : Générer une nourriture aléatoire qui permet au serpent de grandir.
Fonctionnalités : La nourriture est représentée par un carré rouge. Lorsqu'elle est mangée, le serpent grandit.
Code :
food = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)
FOOD_COLOR = (255, 0, 0)

pygame.draw.rect(SCREEN, FOOD_COLOR, (*food, 10, 10))

if snake[0] == food:
    food = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)
else:
    snake.pop()



Étape 6 : Mode multijoueur 
 

Objectif : Permettre à deux joueurs de contrôler deux serpents distincts simultanément.
Fonctionnalités :
- Le joueur 1 contrôle son serpent avec les flèches directionnelles.
- Le joueur 2 contrôle son serpent avec les touches WASD.
Chaque serpent avance indépendamment et suit ses propres mouvements.
Code :
snake1 = [(300, 300), (290, 300), (280, 300)]
snake2 = [(100, 100), (90, 100), (80, 100)]
dir1, dir2 = "RIGHT", "RIGHT"

keys1 = {"UP": (0, -10), "DOWN": (0, 10), "LEFT": (-10, 0), "RIGHT": (10, 0)}
keys2 = {"W": (0, -10), "S": (0, 10), "A": (-10, 0), "D": (10, 0)}

# Gestion des directions pour les deux joueurs
if event.key == pygame.K_UP and dir1 != "DOWN":
    dir1 = "UP"
if event.key == pygame.K_w and dir2 != "S":
    dir2 = "W"

Étape 7 : Ajout du score
 
Objectif : Ajouter un système de score pour chaque joueur en fonction de la nourriture consommée.
Fonctionnalités :
- Chaque joueur possède un score individuel.
- Le score augmente de 1 à chaque fois qu'un serpent mange la nourriture.
- Les scores sont affichés en haut de l’écran.
Code :
 score1, score2 = 0, 0
 font = pygame.font.Font(None, 36)

# Afficher les scores
SCREEN.blit(font.render(f"Joueur 1: {score1}", True, WHITE), (10, 10))
SCREEN.blit(font.render(f"Joueur 2: {score2}", True, WHITE), (WIDTH - 180, 10))

# Mettre à jour le score lors de la consommation de nourriture
if snake1[0] == food:
    score1 += 1
if snake2[0] == food:
    score2 += 1
3. Conclusion

Le projet Multi-Snake respecte les spécifications demandées, offrant une expérience multijoueur complète avec un système de score dynamique.
Chaque étape a été implémentée en respectant les principes de la programmation modulaire en Python.
Le jeu propose les fonctionnalités suivantes :
- Mode multijoueur avec deux joueurs.
- Contrôle indépendant des serpents.
- Gestion des collisions avec murs et serpents.
- Apparition aléatoire de nourriture et système de score.

Le lien GitHub :
cameli0295/multi_snake: camelia
https://github.com/cameli0295/multi_snake
Compte Rendu : Projet Multi-Snake
1. Objectifs du projet
L'objectif principal de ce projet est d'implémenter une version multi-joueur du jeu classique Snake en Python tout en respectant les règles spécifiées :
1. Maîtriser les concepts de base de la programmation Python.
2. Utiliser le module pygame pour les graphiques et les interactions.
3. Permettre à plusieurs joueurs de participer au jeu.
4. Gérer les fonctionnalités telles que :
   - Les collisions avec les murs ou les autres serpents.
   - L'apparition aléatoire de la nourriture.
   - Le calcul et l'affichage des scores

2. Description détaillée étape par étape
Étape 1 : Création de l'arène

 



Objectif : Créer une fenêtre de jeu avec une arène délimitée par des murs blancs.
Fonctionnalités : La fenêtre mesure 600x600 pixels et l’arène est entourée d’un cadre blanc de 10 pixels.
Code :
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
FRAME_WIDTH = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, WHITE, (0, 0, WIDTH, HEIGHT), FRAME_WIDTH)
    pygame.display.flip()
Étape 2 : Implémentation du serpent
 

Objectif : Afficher un serpent statique constitué de plusieurs segments.
Fonctionnalités : Le serpent est représenté par une liste de coordonnées. Chaque segment est dessiné comme un rectangle vert de 10x10 pixels.
Code :
snake = [(300, 300), (290, 300), (280, 300)]
SNAKE_COLOR = (0, 255, 0)

for segment in snake:
    pygame.draw.rect(SCREEN, SNAKE_COLOR, (*segment, 10, 10))
Étape 3 : Mouvement du serpent
 
Objectif : Déplacer le serpent dans une direction choisie par le joueur.
Fonctionnalités : Le serpent avance dans une direction à chaque itération. Les touches fléchées permettent de changer sa direction.
Code :
direction = "RIGHT"
moves = {"UP": (0, -10), "DOWN": (0, 10), "LEFT": (-10, 0), "RIGHT": (10, 0)}

head_x, head_y = snake[0]
new_head = (head_x + moves[direction][0], head_y + moves[direction][1])
snake.insert(0, new_head)
snake.pop()
Étape 4 : Gestion des collisions
 

Objectif : Détecter les collisions avec les murs et le corps du serpent.
Fonctionnalités : Si le serpent touche un mur ou son propre corps, le jeu se termine.
Code :
if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
    pygame.quit()
    sys.exit()

if new_head in snake[1:]:
    pygame.quit()
    sys.exit()
Étape 5 : Ajout de la nourriture
 
Objectif : Générer une nourriture aléatoire qui permet au serpent de grandir.
Fonctionnalités : La nourriture est représentée par un carré rouge. Lorsqu'elle est mangée, le serpent grandit.
Code :
food = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)
FOOD_COLOR = (255, 0, 0)

pygame.draw.rect(SCREEN, FOOD_COLOR, (*food, 10, 10))

if snake[0] == food:
    food = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)
else:
    snake.pop()



Étape 6 : Mode multijoueur 
 

Objectif : Permettre à deux joueurs de contrôler deux serpents distincts simultanément.
Fonctionnalités :
- Le joueur 1 contrôle son serpent avec les flèches directionnelles.
- Le joueur 2 contrôle son serpent avec les touches WASD.
Chaque serpent avance indépendamment et suit ses propres mouvements.
Code :
snake1 = [(300, 300), (290, 300), (280, 300)]
snake2 = [(100, 100), (90, 100), (80, 100)]
dir1, dir2 = "RIGHT", "RIGHT"

keys1 = {"UP": (0, -10), "DOWN": (0, 10), "LEFT": (-10, 0), "RIGHT": (10, 0)}
keys2 = {"W": (0, -10), "S": (0, 10), "A": (-10, 0), "D": (10, 0)}

# Gestion des directions pour les deux joueurs
if event.key == pygame.K_UP and dir1 != "DOWN":
    dir1 = "UP"
if event.key == pygame.K_w and dir2 != "S":
    dir2 = "W"

Étape 7 : Ajout du score
 
Objectif : Ajouter un système de score pour chaque joueur en fonction de la nourriture consommée.
Fonctionnalités :
- Chaque joueur possède un score individuel.
- Le score augmente de 1 à chaque fois qu'un serpent mange la nourriture.
- Les scores sont affichés en haut de l’écran.
Code :
 score1, score2 = 0, 0
 font = pygame.font.Font(None, 36)

# Afficher les scores
SCREEN.blit(font.render(f"Joueur 1: {score1}", True, WHITE), (10, 10))
SCREEN.blit(font.render(f"Joueur 2: {score2}", True, WHITE), (WIDTH - 180, 10))

# Mettre à jour le score lors de la consommation de nourriture
if snake1[0] == food:
    score1 += 1
if snake2[0] == food:
    score2 += 1
3. Conclusion

Le projet Multi-Snake respecte les spécifications demandées, offrant une expérience multijoueur complète avec un système de score dynamique.
Chaque étape a été implémentée en respectant les principes de la programmation modulaire en Python.
Le jeu propose les fonctionnalités suivantes :
- Mode multijoueur avec deux joueurs.
- Contrôle indépendant des serpents.
- Gestion des collisions avec murs et serpents.
- Apparition aléatoire de nourriture et système de score.

Le lien GitHub :
cameli0295/multi_snake: camelia
https://github.com/cameli0295/multi_snake
Compte Rendu : Projet Multi-Snake
1. Objectifs du projet
L'objectif principal de ce projet est d'implémenter une version multi-joueur du jeu classique Snake en Python tout en respectant les règles spécifiées :
1. Maîtriser les concepts de base de la programmation Python.
2. Utiliser le module pygame pour les graphiques et les interactions.
3. Permettre à plusieurs joueurs de participer au jeu.
4. Gérer les fonctionnalités telles que :
   - Les collisions avec les murs ou les autres serpents.
   - L'apparition aléatoire de la nourriture.
   - Le calcul et l'affichage des scores

2. Description détaillée étape par étape
Étape 1 : Création de l'arène

 



Objectif : Créer une fenêtre de jeu avec une arène délimitée par des murs blancs.
Fonctionnalités : La fenêtre mesure 600x600 pixels et l’arène est entourée d’un cadre blanc de 10 pixels.
Code :
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
FRAME_WIDTH = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, WHITE, (0, 0, WIDTH, HEIGHT), FRAME_WIDTH)
    pygame.display.flip()
Étape 2 : Implémentation du serpent
 

Objectif : Afficher un serpent statique constitué de plusieurs segments.
Fonctionnalités : Le serpent est représenté par une liste de coordonnées. Chaque segment est dessiné comme un rectangle vert de 10x10 pixels.
Code :
snake = [(300, 300), (290, 300), (280, 300)]
SNAKE_COLOR = (0, 255, 0)

for segment in snake:
    pygame.draw.rect(SCREEN, SNAKE_COLOR, (*segment, 10, 10))
Étape 3 : Mouvement du serpent
 
Objectif : Déplacer le serpent dans une direction choisie par le joueur.
Fonctionnalités : Le serpent avance dans une direction à chaque itération. Les touches fléchées permettent de changer sa direction.
Code :
direction = "RIGHT"
moves = {"UP": (0, -10), "DOWN": (0, 10), "LEFT": (-10, 0), "RIGHT": (10, 0)}

head_x, head_y = snake[0]
new_head = (head_x + moves[direction][0], head_y + moves[direction][1])
snake.insert(0, new_head)
snake.pop()
Étape 4 : Gestion des collisions
 

Objectif : Détecter les collisions avec les murs et le corps du serpent.
Fonctionnalités : Si le serpent touche un mur ou son propre corps, le jeu se termine.
Code :
if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
    pygame.quit()
    sys.exit()

if new_head in snake[1:]:
    pygame.quit()
    sys.exit()
Étape 5 : Ajout de la nourriture
 
Objectif : Générer une nourriture aléatoire qui permet au serpent de grandir.
Fonctionnalités : La nourriture est représentée par un carré rouge. Lorsqu'elle est mangée, le serpent grandit.
Code :
food = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)
FOOD_COLOR = (255, 0, 0)

pygame.draw.rect(SCREEN, FOOD_COLOR, (*food, 10, 10))

if snake[0] == food:
    food = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)
else:
    snake.pop()



Étape 6 : Mode multijoueur 
 

Objectif : Permettre à deux joueurs de contrôler deux serpents distincts simultanément.
Fonctionnalités :
- Le joueur 1 contrôle son serpent avec les flèches directionnelles.
- Le joueur 2 contrôle son serpent avec les touches WASD.
Chaque serpent avance indépendamment et suit ses propres mouvements.
Code :
snake1 = [(300, 300), (290, 300), (280, 300)]
snake2 = [(100, 100), (90, 100), (80, 100)]
dir1, dir2 = "RIGHT", "RIGHT"

keys1 = {"UP": (0, -10), "DOWN": (0, 10), "LEFT": (-10, 0), "RIGHT": (10, 0)}
keys2 = {"W": (0, -10), "S": (0, 10), "A": (-10, 0), "D": (10, 0)}

# Gestion des directions pour les deux joueurs
if event.key == pygame.K_UP and dir1 != "DOWN":
    dir1 = "UP"
if event.key == pygame.K_w and dir2 != "S":
    dir2 = "W"

Étape 7 : Ajout du score
 
Objectif : Ajouter un système de score pour chaque joueur en fonction de la nourriture consommée.
Fonctionnalités :
- Chaque joueur possède un score individuel.
- Le score augmente de 1 à chaque fois qu'un serpent mange la nourriture.
- Les scores sont affichés en haut de l’écran.
Code :
 score1, score2 = 0, 0
 font = pygame.font.Font(None, 36)

# Afficher les scores
SCREEN.blit(font.render(f"Joueur 1: {score1}", True, WHITE), (10, 10))
SCREEN.blit(font.render(f"Joueur 2: {score2}", True, WHITE), (WIDTH - 180, 10))

# Mettre à jour le score lors de la consommation de nourriture
if snake1[0] == food:
    score1 += 1
if snake2[0] == food:
    score2 += 1
3. Conclusion

Le projet Multi-Snake respecte les spécifications demandées, offrant une expérience multijoueur complète avec un système de score dynamique.
Chaque étape a été implémentée en respectant les principes de la programmation modulaire en Python.
Le jeu propose les fonctionnalités suivantes :
- Mode multijoueur avec deux joueurs.
- Contrôle indépendant des serpents.
- Gestion des collisions avec murs et serpents.
- Apparition aléatoire de nourriture et système de score.

Le lien GitHub :
cameli0295/multi_snake: camelia
https://github.com/cameli0295/multi_snake

