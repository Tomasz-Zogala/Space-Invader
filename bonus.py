import pygame
import random

class Bonus(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y,speed):
        super().__init__()
        self.height = 15
        self.weight = 15
        self.speed = speed
        self.image = pygame.Surface([self.weight, self.height])
        self.image.fill((0, 200, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):

        # Move the enemy down the screen
        self.rect.y += self.speed
        if self.rect.y > 800:
            self.kill()

