import pygame
import random

class Bonus(pygame.sprite.Sprite):
    def __init__(self, center ,speed):
        super().__init__()

        # Stats
        self.speed = speed

        # Image data
        self.color = '#A6E742'
        self.height = 15
        self.weight = 15

        # Image
        self.image = pygame.Surface([self.weight, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center
    def movement(self):
        self.rect.y += self.speed
        if self.rect.y > 800:
            self.kill()
    def update(self):
        self.movement()


