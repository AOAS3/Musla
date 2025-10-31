import pygame
import cv2
import sys

def play_video(video_path):
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width, screen_height = screen.get_size()
    clock = pygame.time.Clock()

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erreur : impossible de charger la vidéo.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        frame_surface = pygame.transform.scale(frame_surface, (screen_width, screen_height))
        screen.blit(frame_surface, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                cap.release()
                return  # quitte la vidéo

        clock.tick(30)

    cap.release()
