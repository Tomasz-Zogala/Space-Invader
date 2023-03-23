import pygame

from Bonuses_package.bonus import Bonus
from Consts_package.consts import SCREEN_HEIGHT, SCREEN_WIDTH, players


# Define the Score_bonus class
class Score_bonus(Bonus):
    def __init__(self, center, speed):
        super().__init__(center, speed)

        # Stats
        self.speed = speed
        self.score_bonus = 50

        # Image data
        self.color = '#A6E742'
        self.height = SCREEN_HEIGHT / 32
        self.width = SCREEN_WIDTH / 32

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

    def player_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)
        if collided_player:
            for player in collided_player:
                self.kill()
                player.score += self.score_bonus
