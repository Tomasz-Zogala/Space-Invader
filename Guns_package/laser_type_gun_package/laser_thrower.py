import pygame


from Guns_package.laser_type_gun_package.laser_type_gun import Laser_type_gun

from Constants_package.constants import SCALE


# Define the Laser_thrower class
class Laser_thrower(Laser_type_gun):
    def __init__(self, center, damage_multiplier, fire_rate_multiplier):
        super().__init__(center, damage_multiplier, fire_rate_multiplier)

        # Stats
        self.damage = 0.08 * damage_multiplier
        self.fire_rate = 80 * fire_rate_multiplier
        self.bullet_speed = 10 * SCALE
        self.range_timer_max = 1200 * SCALE
        self.range_timer_min = 0

        # Image data
        self.width = 45 * SCALE
        self.height = 45 * SCALE
        self.color = '#BB00FF'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

        # Audio
        self.audio = pygame.mixer.Sound("Additional_resources/Audio/laser_thrower.mp3")
        self.audio.set_volume(0.5)
        self.audio.play()

    def movement_service(self):
        self.rect.y += -self.bullet_speed
        if self.range_timer_max <= self.range_timer_min:
            self.kill()
            self.range_timer_max = 0
        self.range_timer_min += 100
