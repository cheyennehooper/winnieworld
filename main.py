import pygame
import sys

#init game
pygame.init()

#display
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("winnies world")

#load winnie!
winnie_img = pygame.image.load("assets/winnie.png")
winnie_rect = winnie_img.get_rect(center=(WIDTH//2, HEIGHT//2))

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((225,225,225))
    screen.blit(winnie_img, winnie_rect)
    pygame.display.flip()

#quit game
pygame.quit()
sys.exit()