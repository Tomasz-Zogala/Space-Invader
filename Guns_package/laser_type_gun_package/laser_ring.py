import pygame

from Consts_package.consts import SCREEN_HEIGHT, SCALE
from Guns_package.laser_type_gun_package.laser_type_gun import Laser_type_gun


# Define the Laser_ring class
class Laser_ring(Laser_type_gun):
    def __init__(self, center, damage_multiplier, fire_rate_multiplier):
        super().__init__(center, damage_multiplier, fire_rate_multiplier)

        # Stats
        self.damage = 0.1 * damage_multiplier
        self.fire_rate = 80 * fire_rate_multiplier
        self.bullet_speed = 10 * SCALE
        self.range_timer_max = 150 * SCALE
        self.range_timer_min = 0

        # Image data
        self.width = 300 * SCALE
        self.height = 300 * SCALE
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

        if self.range_timer_max <= self.range_timer_min:
            self.kill()
            self.range_timer_max = 0
        self.range_timer_min += 100
