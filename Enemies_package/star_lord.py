import pygame
import random

from Enemies_package.enemy import Enemy
from Sprites_package.sprites import guns


# Define the Star_lord class
class Star_lord(Enemy):
    def __init__(self):
        super().__init__()

        # Stats
        self.hp = 20
        self.speed = 2
        self.star_lord_timer = 0

        # Image data
        self.width = 100
        self.height = 50
        self.color = '#145343'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = (400, 50)

    def movement(self):
        self.rect.x += self.speed
        if self.rect.left == 800:
            self.rect.right = 0

    def hp_service(self):
        if self.hp == 15:
            print(15)

        if self.hp == 10:
            print(10)

        if self.hp == 5:
            print(5)

    def bullet_service(self):
        pygame.sprite.spritecollide(self, guns, True)

    def update(self):
        self.bullet_service()
        self.movement()
        self.hp_service()

    def default(self):
        pass
