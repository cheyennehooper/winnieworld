import pygame

tile_size = 32

class TileMap:
    def __init__(self):
        self.tiles_x = 20
        self.tiles_y = 15

    def draw(self, screen):
        for row in range(self.tiles_y):
            for col in range(self.tiles_x):
                color = (158,207,141) if (row + col) % 2 == 0 else (109,185,102)
                rect = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
                pygame.draw.rect(screen, color, rect)
