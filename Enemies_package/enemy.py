import pygame
import random

from Sprites_package.sprites import guns


# Define the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Stats
        self.hp = 0
        self.speed_x = 0
        self.speed_y = 0

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
        self.rect.y += self.speed_y
        if self.rect.y > 800:
            self.rect.x = random.randrange(800 - self.rect.width)
            self.rect.y = random.randrange(-100, -self.rect.height)

    def hp_service(self):
        if self.hp == 2:
            new_width = int(self.width * 0.8)  # reduce the width by 50%
            new_height = int(self.height * 0.8)  # reduce the height by 50%
            old_center = self.rect.center

            self.image = pygame.transform.scale(self.image, (new_width, new_height))
            self.rect = self.image.get_rect()  # update the rect of the image
            self.rect.center = old_center

            self.image.fill('#DEA0A0')

        if self.hp == 1:
            new_width = int(self.width * 0.7)  # reduce the width by 50%
            new_height = int(self.height * 0.7)  # reduce the height by 50%
            old_center = self.rect.center

            self.image = pygame.transform.scale(self.image, (new_width, new_height))
            self.rect = self.image.get_rect()  # update the rect of the image
            self.rect.center = old_center
            self.image.fill('#B25959')

    def update(self):
        self.movement()
        self.hp_service()
