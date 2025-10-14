import pygame
import player
from player import Player 

pygame.init()

# Fenêtre
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("My Adventure")
clock = pygame.time.Clock()

# Chargement du fond
back = pygame.image.load("content/texture pack/green texture.png").convert()

# Chargement du joueur
player = Player(200, 200)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    
    keys = pygame.key.get_pressed()
    player.update(keys)

  
    screen.blit(back, (0, 0))
    player.draw(screen)

   
    pygame.display.flip()
    clock.tick(60)

pygame.quit()  