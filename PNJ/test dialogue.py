import pygame
pygame.init()

# Paramètres de la fenêtre
screen_width = 1280
screen_height = 840
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("LEs PuZzLeS")
continuer=True
while continuer:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
pygame.quit()

