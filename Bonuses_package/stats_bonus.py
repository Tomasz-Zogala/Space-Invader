import pygame
import random

from Bonuses_package.bonus import Bonus

from Constants_package.constants import players, SCALE


# Define the Stats_bonus class
class Stats_bonus(Bonus):
    def __init__(self, center):
        super().__init__(center)

        # Stats
        self.speed = 2 * SCALE
        self.score_bonus = 50

        # Image data
        self.color = '#000000'
        self.color_damage_up = '#F3A31F'
        self.color_fire_rate_up = '#F3DA1F'
        self.color_speed_up = '#1FF3D3'
        self.height = 40 * SCALE
        self.width = 40 * SCALE

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()

        # Set bonus
        self.bonus_type = random.randint(1, 3)
        if self.bonus_type == 1:
            self.image.fill(self.color_damage_up)
        if self.bonus_type == 2:
            self.image.fill(self.color_fire_rate_up)
        if self.bonus_type == 3:
            self.image.fill(self.color_speed_up)

        # Position
        self.rect.center = center

    def collision_with_player_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)
        if collided_player:
            for player in collided_player:
                if self.bonus_type == 1:
                    player.gun_damage_multiplier += 0.3
                if self.bonus_type == 2:
                    player.gun_fire_rate_multiplier += -0.03
                if self.bonus_type == 3:
                    player.speed += 1.5 * SCALE
                self.kill()
                player.score += self.score_bonus
