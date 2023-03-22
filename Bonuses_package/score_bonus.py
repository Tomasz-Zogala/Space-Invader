import pygame

from Bonuses_package.bonus import Bonus


# Define the Score_bonus class
class Score_bonus(Bonus):
    def __init__(self, center, speed):
        super().__init__(center, speed)

        # Stats
        self.speed = speed

        # Image data
        self.color = '#A6E742'
        self.height = 40
        self.weight = 40

        # Image
        self.image = pygame.Surface([self.weight, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center
import pygame

from Bonuses_package.bonus import Bonus
from Consts_package.consts import SCREEN_HEIGHT, players


# Define the Bonus class
class Hp_bonus(Bonus):
    def __init__(self, center, speed):
        super().__init__(center, speed)

        # Stats
        self.speed = speed

        # Image data
        self.color = '#FFFF00'
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
                self.kill()
                player.score += 20

