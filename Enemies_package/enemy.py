import pygame
import random

from Sprites_package.sprites import guns


# Define the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Stats
        self.hp = 0
        self.speed = 0

        # Image data
        self.width = 0
        self.height = 0
        self.color = '#000000'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.x = self.width
        self.rect.y = self.height

    def movement(self):
        pass

    def hp_service(self):
        pass

    def bullet_service(self):
        pass

    def update(self):
        self.bullet_service()
        self.movement()
        self.hp_service()

    def default(self):
        pass
