import pygame

from Consts_package.consts import SCREEN_HEIGHT


# Define the abstract Bonus class
class Bonus(pygame.sprite.Sprite):
    def __init__(self, center, speed):
        super().__init__()

        # Stats
        self.speed = speed
        self.score_bonus = 0

        # Image data
        self.color = '#000000'
        self.height = 0
        self.width = 0

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

    def movement(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT+100:
            self.kill()

    def player_service(self):
        pass

    def update(self):
        self.player_service()
        self.movement()
