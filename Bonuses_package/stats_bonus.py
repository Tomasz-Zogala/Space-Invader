import random

import pygame

from Bonuses_package.bonus import Bonus
from Consts_package.consts import players


# Define the Stats_bonus class
class Stats_bonus(Bonus):
    def __init__(self, center, speed):
        super().__init__(center, speed)

        # Stats
        self.speed = speed

        # Image data
        self.color = '#FFCC00'
        self.height = 30
        self.weight = 30

        # Image
        self.image = pygame.Surface([self.weight, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

    def player_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)
        if collided_player:
            for player in collided_player:
                random_numer = random.randint(1, 3)
                if random_numer == 1:
                    player.gun_damage_multiplier += 0.5
                if random_numer == 2:
                    player.gun_fire_rate_multiplier += -0.05
                if random_numer == 3:
                    player.speed += 2
            self.kill()
            player.score += 50
