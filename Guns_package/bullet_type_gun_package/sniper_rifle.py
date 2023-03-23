import pygame

from Consts_package.consts import SCREEN_HEIGHT, SCALE
from Guns_package.bullet_type_gun_package.bullet_type_gun import Bullet_type_gun


# Define the Sniper_rifle class
class Sniper_rifle(Bullet_type_gun):
    def __init__(self, center, damage_multiplier, fire_rate_multiplier):
        super().__init__(center, damage_multiplier, fire_rate_multiplier)

        # Stats
        self.damage = 15 * damage_multiplier
        self.fire_rate = 5000 * fire_rate_multiplier
        self.bullet_speed = 50 * SCALE

        # Image data
        self.width = 10 * SCALE
        self.height = 10 * SCALE
        self.color = '#938D8D'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

        # Audio
