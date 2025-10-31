import pygame
from player import Player
import vidintro

pygame.init()
clock = pygame.time.Clock()

# l'intro
vidintro.play_video("content/intro/1022.mp4")

# Paramètre pour la taille de l'écran
info = pygame.display.Info()
largeur_ecran, hauteur_ecran = info.current_w, info.current_h

# Fenêtre 
screen = pygame.display.set_mode((largeur_ecran, hauteur_ecran), pygame.FULLSCREEN)
pygame.display.set_caption("My Adventure")

# Les fonds
back_exterieur = pygame.image.load("content/texture pack/green texture.png").convert()#Fond vert du jeu
back_interieur = pygame.image.load("content/texture pack/inside.png").convert()#musée
muse = pygame.image.load("content/texture pack/musee.png").convert_alpha()# Porte du musée

# La musica del musée
pygame.mixer.music.load("content/music/Endgame.mp3")  # chemin vers ta musique
pygame.mixer.music.set_volume(0.5)  # volume (0.0 à 1.0)

# Le joueur
player = Player(200, 400, largeur_ecran, hauteur_ecran)

# L'entrée du musée
muse_x, muse_y = 380, 100
muse_largeur, muse_hauteur = 260, 220
entree_musee = pygame.Rect(muse_x + 80, muse_y + muse_hauteur - 10, 100, 10)
# Liste pour la collision avec la porte
murs_musee = [
    pygame.Rect(muse_x + 10, muse_y + 10, muse_largeur - 20, 10),
    pygame.Rect(muse_x + 10, muse_y + 10, 10, muse_hauteur - 20),
    pygame.Rect(muse_x + muse_largeur - 20, muse_y + 10, 10, muse_hauteur - 20),
    pygame.Rect(muse_x + 10, muse_y + muse_hauteur - 30, muse_largeur - 20, 20)
]

# Porte rouge à l'intérieur pour sortir (elle est placée loin de l'entrée)
porte_sortie_musee = pygame.Rect(500, 100, 50, 100)  # exemple : en haut à droite du musée

# Les états du jeu
dans_musee = False
musique_lancee = False
start_time = 0  # pour gérer le délai avant mouvement et musique

#Fondu pour l'entrée et la sortie du personnages
def transition_noir(screen, vitesse=10, attendre=20):
    noir = pygame.Surface((largeur_ecran, hauteur_ecran))
    noir.fill((0, 0, 0))
    for alpha in range(0, 255, vitesse):
        noir.set_alpha(alpha)
        screen.blit(noir, (0, 0))
        pygame.display.flip()
        pygame.time.delay(attendre)

def handle_collisions(rect, murs):
    for mur in murs:
        if rect.colliderect(mur):
            if rect.bottom > mur.top and rect.top < mur.top:
                rect.bottom = mur.top
            elif rect.top < mur.bottom and rect.bottom > mur.bottom:
                rect.top = mur.bottom
            elif rect.right > mur.left and rect.left < mur.left:
                rect.right = mur.left
            elif rect.left < mur.right and rect.right > mur.right:
                rect.left = mur.right
    return rect

# Boucle du jeu
running = True
back = back_exterieur

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    #  Bloque le joueur avant que la musique se lance 
    if dans_musee and not musique_lancee:
        elapsed = pygame.time.get_ticks() - start_time
        if elapsed >= 3000:  # 3 secondes
            pygame.mixer.music.play(-1)  # boucle infiniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiie
            musique_lancee = True
        else:
            keys = []  # aucune touche ne fonctionne(logique on a rien mit dans les clés)
    else:
        keys = pygame.key.get_pressed()
        player.update(keys)

    if not dans_musee:
        player.rect = handle_collisions(player.rect, murs_musee)

    # Transition d'entrée dans le musée
    if not dans_musee and player.rect.colliderect(entree_musee):
        transition_noir(screen)
        dans_musee = True
        back = back_interieur
        player.rect.x, player.rect.y = 200, 500  # position d'apparition dans le musée
        start_time = pygame.time.get_ticks()  # démarre le timer pour le délai
        musique_lancee = False

    # La sortie du musée
    if dans_musee and player.rect.colliderect(porte_sortie_musee):
        transition_noir(screen)
        dans_musee = False
        back = back_exterieur
        player.rect.x, player.rect.y = 400, 340  # position devant l'entrée
        pygame.mixer.music.stop()  # arrêter la musique

    # Affichage 
    screen.fill((0, 0, 0))
    screen.blit(back, (0, 0))

    if not dans_musee:
        screen.blit(muse, (muse_x, muse_y))
    else:
        # DEBUG : afficher la porte rouge
        pygame.draw.rect(screen, (255, 0, 0), porte_sortie_musee)

    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
