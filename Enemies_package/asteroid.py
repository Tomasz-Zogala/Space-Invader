import pygame
import random

from Enemies_package.enemy import Enemy
from Consts_package.consts import SCREEN_HEIGHT, SCREEN_WIDTH, players, enemies, SCALE


# Define the Asteroid class
class Asteroid(Enemy):
    def __init__(self):
        super().__init__()

        # Stats
        self.hp = 20
        self.speed_x = 0 * SCALE
        self.speed_y = random.randrange(3, 5) * SCALE
        self.damage = 1

        # Image data
        self.width = 50 * SCALE
        self.height = 50 * SCALE
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
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = random.randrange(0, SCREEN_WIDTH)
            self.rect.y = -50 * SCALE
            self.default()

    def attack_melee(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                pygame.sprite.spritecollide(player, enemies, True)
                asteroid = Asteroid()
                enemies.add(asteroid)
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

    def hp_service(self):
        if self.hp <= 13:
            new_width = int(self.width * 0.8)
            new_height = int(self.height * 0.8)
            old_center = self.rect.center

            self.image = pygame.transform.scale(self.image, (new_width, new_height))
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            self.image.fill('#DEA0A0')

        if self.hp <= 7:
            new_width = int(self.width * 0.7)
            new_height = int(self.height * 0.7)
            old_center = self.rect.center

            self.image = pygame.transform.scale(self.image, (new_width, new_height))
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            self.image.fill('#B25959')

    def update(self):
        self.attack_melee()
        self.movement()
        self.hp_service()

    def default(self):
        # Stats
        self.hp = 20
        self.speed_x = 0 * SCALE
        self.speed_y = random.randrange(3, 5) * SCALE
        self.damage = 1

        # Image data
        self.width = 50 * SCALE
        self.height = 50 * SCALE
        self.color = '#938D8D'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.x = random.randrange(0, SCREEN_WIDTH)
        self.rect.y = -50 * SCALE
