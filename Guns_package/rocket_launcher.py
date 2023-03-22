import pygame

from Guns_package.gun import Gun
from Bonuses_package.bonus import Bonus
from Enemies_package.asteroid import Asteroid
from Enemies_package.star_lord import Star_lord
from Consts_package.consts import bonuses, enemies


# Define the Rocket_launcher class
class Rocket_launcher(Gun):
    def __init__(self, center):
        super().__init__(center)

        # Stats
        self.damage = 15
        self.fire_rate = 4000
        self.bullet_speed = 5

        # Image data
        self.width = 40
        self.height = 60
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
