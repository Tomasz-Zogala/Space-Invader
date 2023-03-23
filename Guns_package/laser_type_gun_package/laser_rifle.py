import pygame

from Consts_package.consts import SCREEN_HEIGHT, SCALE
from Guns_package.laser_type_gun_package.laser_type_gun import Laser_type_gun


# Define the Laser_rifle class
class Laser_rifle(Laser_type_gun):
    def __init__(self, center, damage_multiplier, fire_rate_multiplier):
        super().__init__(center, damage_multiplier, fire_rate_multiplier)

        # Stats
        self.damage = 0.06 * damage_multiplier
        self.fire_rate = 70 * fire_rate_multiplier
        self.bullet_speed = 15 * SCALE

        # Image data
        self.width = 5 * SCALE
        self.height = 20 * SCALE
        self.color = '#033BFB'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

        # Audio

    def movement(self):
        self.rect.y += -self.bullet_speed
        if self.rect.y < -100:
            self.kill()