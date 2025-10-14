import pygame

TAILLE_PERSO = (64, 64)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vitesse = 3
        self.frame = 0
        self.load_images()

    def load_images(self):
        self.sprites_down = [
            pygame.transform.scale(pygame.image.load("content/Perso/char_001.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/char_002.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/char_004.png"), TAILLE_PERSO),
            pygame.transform.scale(pygame.image.load("content/Perso/char_003.png"), TAILLE_PERSO)
        ]

    def update(self, keys):
        if keys[pygame.K_DOWN]:
            self.y += self.vitesse
            self.frame = (self.frame + 1) % len(self.sprites_down)
        else:
            self.frame = 0

    def draw(self, surface):
        surface.blit(self.sprites_down[self.frame], (self.x, self.y))
