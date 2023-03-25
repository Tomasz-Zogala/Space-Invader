import pygame
import random

from Enemies_package.enemy import Enemy
from Consts_package.consts import SCREEN_HEIGHT, SCREEN_WIDTH, players, enemies, SCALE


# Define the Stardust class
class Stardust(Enemy):
    def __init__(self):
        super().__init__()

        # Stats
        self.hp = 100
        self.speed_x = random.randrange(-1, 1) * SCALE
        self.speed_y = random.randrange(2, 5) * SCALE
        self.damage = 0.5

        # Image data
        self.width = 15 * SCALE
        self.height = 15 * SCALE
        self.color = '#938D8D'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.x = random.randrange(0, SCREEN_WIDTH)
        self.rect.y = random.randrange(-250, -50)

    def movement(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y > SCREEN_HEIGHT+50:
            self.kill()

    def attack_melee(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                pygame.sprite.spritecollide(player, enemies, True)
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

    def hp_service(self):
        if self.hp <= 50:
            self.image.fill('#DEA0A0')

        if self.hp <= 20:
            self.image.fill('#B25959')

    def update(self):
        self.attack_melee()
        self.movement()
        self.hp_service()