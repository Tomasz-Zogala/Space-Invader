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
        self.speed_x = 3
        self.speed_y = 2
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
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left == 800:
            self.rect.right = 0

        if self.rect.bottom >= 150:
            self.speed_y = self.speed_y*-1

        if self.rect.top <= 0:
            self.speed_y = self.speed_y * -1

    def hp_service(self):
        if self.hp <= self.hp/2:
            self.image.fill('#451212')

    def bullet_service(self):
        pygame.sprite.spritecollide(self, guns, True)

    def update(self):
        self.bullet_service()
        self.movement()
        self.hp_service()
