import pygame


from Guns_package.laser_type_gun_package.laser_type_gun import Laser_type_gun


# Define the Laser_thrower class
class Laser_thrower(Laser_type_gun):
    def __init__(self, center, damage_multiplier, fire_rate_multiplier):
        super().__init__(center, damage_multiplier, fire_rate_multiplier)

        # Stats
        self.damage = 0.1 * damage_multiplier
        self.fire_rate = 100 * fire_rate_multiplier
        self.bullet_speed = 15
        self.range_timer_max = 1400
        self.range_timer_min = 0

        # Image data
        self.width = 15
        self.height = 20
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
