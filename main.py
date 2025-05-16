import pygame
import sys

from player import Player
from tilemap import TileMap

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

tilemap = TileMap()
player = Player(tile_size//2, tile_size//2)

#game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #game logic
    player.update()

    #drawing on screen
    tilemap.draw(screen)
    player.draw(screen)
    pygame.display.flip()

#quit game
pygame.quit()
sys.exit()