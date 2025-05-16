import pygame

#playerclass
class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/winnie.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = 3

    def player_input(self):
        #keymapping the motion
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed    
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def update(self):
        self.player_input()

    def draw(self, surface):
        surface.blit(self.image, self.rect)