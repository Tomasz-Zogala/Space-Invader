import pygame
import random

from Enemies_package.Enemy_laser_gun.galactic_devourer_laser_ring import Galactic_devourer_laser_ring
from Enemies_package.enemy import Enemy
from Consts_package.consts import enemies_laser_guns, SCREEN_WIDTH, players, SCREEN_HEIGHT, SCALE


# Define the Galactic_devourer class
class Galactic_devourer(Enemy):
    def __init__(self):
        super().__init__()

        # Stats
        self.damage = 0.5
        self.hp = 40
        self.acceleration = 1
        self.speed_x = random.randint(-2, 2) * SCALE
        self.speed_y = random.randint(-4, 4) * SCALE

        # Timer
        self.galactic_devourer_timer = 0
        self.galactic_devourer_overheating_timer = 0
        self.galactic_devourer_overheating_timer_max = 20000
        self.galactic_devourer_overheating_timer_2 = 0
        self.overheating_passed = True

        # Image data
        self.width = 120 * SCALE
        self.height = 120 * SCALE
        self.color = '#145343'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.x = random.randrange(0, SCREEN_WIDTH)
        self.rect.y = SCREEN_HEIGHT/8

    def movement(self):
        self.rect.x += self.speed_x * self.acceleration
        self.rect.y += self.speed_y * self.acceleration
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.speed_x *= -1
        if self.rect.bottom >= SCREEN_HEIGHT or self.rect.top <= 0:
            self.speed_y *= -1

    def attack_ranged(self):
        if self.galactic_devourer_overheating_timer <= self.galactic_devourer_overheating_timer_max:

            if self.galactic_devourer_timer <= 0:
                galactic_devourer_laser_ring = Galactic_devourer_laser_ring(self.rect.center, 1, 300, 10, 250, 250, "#73FE1E")
                enemies_laser_guns.add(galactic_devourer_laser_ring)
                self.galactic_devourer_timer = galactic_devourer_laser_ring.fire_rate
                self.acceleration = 3

            self.galactic_devourer_timer += -100
            self.galactic_devourer_overheating_timer += 100
            self.galactic_devourer_overheating_timer_2 = 0

        else:
            self.acceleration = 1
            if self.galactic_devourer_overheating_timer_2 >= self.galactic_devourer_overheating_timer_max*2:
                self.galactic_devourer_overheating_timer = 0

            self.galactic_devourer_overheating_timer_2 += 100

    def attack_melee(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

    def hp_service(self):
        if self.hp <= 30:
            self.image.fill('#451212')

    def update(self):
        self.attack_ranged()
        self.attack_melee()
        self.movement()
        self.hp_service()