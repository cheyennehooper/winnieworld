import pygame
import sys

from player import Player

#init game
pygame.init()

#tile setup
tile_size = 32
tiles_x = 20
tiles_y = 15

#display
WIDTH, HEIGHT = tile_size * tiles_x, tile_size * tiles_y
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("winnies world")

#load winnie!
winnie_img = pygame.image.load("assets/winnie.png")
winnie_rect = winnie_img.get_rect(center=(WIDTH//2, HEIGHT//2))

player = Player(tile_size//2, tile_size//2)

#game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player.update()


    #tile board temp
    for row in range(tiles_y):
        for col in range(tiles_x):
            color = (158,207,141) if (row + col) % 2 == 0 else (109,185,102)
            rect = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
            pygame.draw.rect(screen, color, rect)




    #drawing on screen
    player.draw(screen)
    pygame.display.flip()

#quit game
pygame.quit()
sys.exit()