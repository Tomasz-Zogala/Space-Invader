import pygame

from Bonuses_package.bonus import Bonus
from Consts_package.consts import players, SCREEN_HEIGHT, SCREEN_WIDTH


# Define the Hp_Bonus class
class Hp_bonus(Bonus):
    def __init__(self, center, speed):
        super().__init__(center, speed)

        # Stats
        self.speed = speed
        self.score_bonus = 75

        # Image data
        self.color = '##FA4CDA'
        self.height = SCREEN_HEIGHT / 16
        self.width = SCREEN_WIDTH / 16

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
                if player.hp >= 3:
                    pass
                else:
                    player.hp += 1
                self.kill()
                player.score += self.score_bonus
