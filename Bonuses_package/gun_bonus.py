import pygame

from Bonuses_package.bonus import Bonus
from Consts_package.consts import players


# Define the Gun_bonus class
class Gun_bonus(Bonus):
    def __init__(self, center, speed):
        super().__init__(center, speed)

        # Stats
        self.speed = speed

        # Image data
        self.color = '#00FFFF'
        self.height = 50
        self.weight = 50

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
                if player.laser_ring:
                    player.sniper_rifle = True

                if player.laser_rifle:
                    player.laser_ring = True

                if player.flame_thrower:
                    player.laser_rifle = True

                if player.rocket_launcher:
                    player.flame_thrower = True

                if player.minigun:
                    player.rocket_launcher = True

            self.kill()
            player.score += 100
