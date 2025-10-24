import pygame
from player import Player
import vidintro

pygame.init()
clock = pygame.time.Clock()

vidintro.play_video("content/intro/1022.mp4")




# Paramètre permettant de récupérer la taille de l'écran
info = pygame.display.Info()
largeur_ecran, hauteur_ecran = info.current_w, info.current_h

# Création de la feenêtre avec le paramètre
screen = pygame.display.set_mode((largeur_ecran, hauteur_ecran), pygame.FULLSCREEN)
pygame.display.set_caption("My Adventure")

# Chargement du fond
back = pygame.image.load("content/texture pack/green texture.png")

# Création du joueur + paramètre
player = Player(200, 200, largeur_ecran, hauteur_ecran)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys) # update importé de player

    screen.blit(back, (0, 0))
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
