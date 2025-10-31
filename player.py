import pygame

TAILLE_PERSO = (64, 64)

class Player:
    def __init__(self, x, y, largeur_ecran, hauteur_ecran):
        self.vitesse = 3
        self.frame = 0
        self.largeur_ecran = largeur_ecran
        self.hauteur_ecran = hauteur_ecran

        # Crée le rectangle du joueur
        self.rect = pygame.Rect(x, y, TAILLE_PERSO[0], TAILLE_PERSO[1])

        # Charge les sprites
        self.sprites_down = [
            pygame.transform.scale(pygame.image.load("content/Perso/char_001.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/char_002.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/char_003.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/char_004.png"), TAILLE_PERSO)
        ]

    def update(self, keys): #update sert à mettre à jour les touches du personnage hors de keys 
        # Déplacement
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.vitesse
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.vitesse
        if keys[pygame.K_UP]:
            self.rect.y -= self.vitesse
        if keys[pygame.K_DOWN]:
            self.rect.y += self.vitesse

      
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.largeur_ecran:
            self.rect.right = self.largeur_ecran
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.hauteur_ecran:
            self.rect.bottom = self.hauteur_ecran

        # Animation (facultative)
        if any([keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN]]):
            self.frame = (self.frame + 1) % len(self.sprites_down)
        else:
            self.frame = 0

    def draw(self, surface):
        surface.blit(self.sprites_down[self.frame], self.rect)
