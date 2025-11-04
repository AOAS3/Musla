import pygame

TAILLE_PERSO = (64, 64)

class Player:
    def __init__(self, x, y, largeur_ecran, hauteur_ecran):
        self.vitesse = 3
        self.frame = 0
        self.direction = "down"  # direction actuelle
        self.largeur_ecran = largeur_ecran
        self.hauteur_ecran = hauteur_ecran

        self.rect = pygame.Rect(x, y, *TAILLE_PERSO)

        # Les sprites

        # Bas
        self.sprites_down = [
            pygame.transform.scale(pygame.image.load("content/Perso/char_001.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/char_002.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/char_003.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/char_004.png"), TAILLE_PERSO)
        ]

        # Gauche
        self.sprites_left = [
            pygame.transform.scale(pygame.image.load("content/Perso/Char_right001.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/Char_right002.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/Char_right003.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/Char_right004.png"), TAILLE_PERSO)
        ]

        # Droite
        self.sprites_right = [
            pygame.transform.scale(pygame.image.load("content/Perso/Char_left001.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/Char_left002.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/Char_left003.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/Char_left004.png"), TAILLE_PERSO)
        ]

    def update(self, keys):
        moved = False

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.vitesse
            self.direction = "left"
            moved = True
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.vitesse
            self.direction = "right"
            moved = True
        elif keys[pygame.K_UP]:
            self.rect.y -= self.vitesse
            self.direction = "up"  
            moved = True
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.vitesse
            self.direction = "down"
            moved = True

        # Empêche de sortir de l'écran
        self.rect.clamp_ip(pygame.Rect(0, 0, self.largeur_ecran, self.hauteur_ecran))

        # Animation
        if moved:
            self.frame = (self.frame + 1) % 4
        else:
            self.frame = 0

    def draw(self, surface):
        # Choix du sprite selon la direction
        if self.direction == "left":
            sprite = self.sprites_left[self.frame]
        elif self.direction == "right":
            sprite = self.sprites_right[self.frame]
        else:
            sprite = self.sprites_down[self.frame]

        surface.blit(sprite, self.rect)


