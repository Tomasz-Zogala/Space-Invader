import pygame
import random

from sprites import bullets


# Define the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.height = 30
        self.weight = 30
        self.hp = 3
        self.speed = speed
        self.color = (64, 64, 64)
        self.image = pygame.Surface([self.weight, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(-100, -self.rect.height)

    def update(self):
        pygame.sprite.spritecollide(self, bullets, True)

        # Move the enemy down the screen
        self.rect.y += self.speed
        if self.rect.y > 800:
            self.rect.x = random.randrange(800 - self.rect.width)
            self.rect.y = random.randrange(-100, -self.rect.height)
            self.default()

        if (self.hp == 2):
            self.image = pygame.Surface([self.weight-2, self.height-2]) # inflate
            self.image.fill('#A92B10')

        if (self.hp == 1):
            self.image = pygame.Surface([self.weight-2, self.height-2]) # inflate
            self.image.fill('#E32800')

    def default(self):
        self.height = 30
        self.weight = 30
        self.hp = 3
        self.speed = 5
        self.image = pygame.Surface([self.weight, self.height])
        self.image.fill(self.color)