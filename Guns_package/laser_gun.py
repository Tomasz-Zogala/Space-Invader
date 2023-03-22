import pygame

from Guns_package.gun import Gun
from Bonuses_package.bonus import Bonus
from Enemies_package.asteroid import Asteroid
from Enemies_package.star_lord import Star_lord
from Consts_package.consts import bonuses, enemies


# Define the Laser_gun class
class Laser_gun(Gun):
    def __init__(self, center, damage_multiplier, fire_rate_multiplier):
        super().__init__(center, damage_multiplier, fire_rate_multiplier)

        # Stats
        self.damage = 1 * damage_multiplier
        self.fire_rate = 600 * fire_rate_multiplier
        self.bullet_speed = 10

        # Image data
        self.width = 10
        self.height = 15
        self.color = '#938D8D'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

        # Audio
        self.laser_audio = pygame.mixer.Sound('Additional_resources/Audio/Laser_sound.mp3')
        self.laser_audio.set_volume(0.2)
        self.laser_audio.play()
