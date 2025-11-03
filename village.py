import pygame
def village():
    # Maisons du village
    house_image = pygame.image.load("content/texture pack/house.png").convert_alpha()

    maisons_village = [
        {"pos": (300, 400)},
        {"pos": (600, 380)},
        {"pos": (900, 420)},
        {"pos": (1200, 400)},
    ]
    #à mettre dans la boucle du jeu de le main.py
    if zone_actuelle == "village":
    for maison in maisons_village:
        screen.blit(house_image, maison["pos"])
    murs_maisons = [pygame.Rect(x, y, house_image.get_width(), house_image.get_height()) 
                for (x, y) in [m["pos"] for m in maisons_village]]
    if zone_actuelle == "village":
    player.rect = handle_collisions(player.rect, murs_maisons)


