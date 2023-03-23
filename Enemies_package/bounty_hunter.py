import pygame
import math


from Enemies_package.enemy import Enemy
from Enemies_package.Enemy_laser_gun.enemy_laser_gun import Enemy_laser_gun
from Consts_package.consts import enemies_laser_guns, SCREEN_WIDTH, players, SCREEN_HEIGHT, SCALE


# Define the Bounty_hunter class
class Bounty_hunter(Enemy):
    def __init__(self):
        super().__init__()

        # Stats
        self.hp = 100
        self.speed_x = 3 * SCALE
        self.speed_y = 3 * SCALE
        self.damage = 1
        self.radius = 100 * SCALE
        self.angle = 0

        # Timer
        self.bounty_hunter_timer = 0
        self.bounty_hunter_overheating_timer = 0
        self.bounty_hunter_overheating_timer_max = 20000
        self.bounty_hunter_overheating_timer_2 = 0
        self.overheating_passed = True

        # Image data
        self.width = 75 * SCALE
        self.height = 75 * SCALE
        self.color = '#000000'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = (SCREEN_WIDTH/2-self.radius/2, SCREEN_HEIGHT/10)

    def movement(self):
        self.rect.x = SCREEN_WIDTH / 2 - self.radius + self.radius * math.cos(self.angle)
        self.rect.y = SCREEN_HEIGHT / 10 + self.radius * math.sin(self.angle)
        self.angle += 0.1

    def attack_ranged(self):
        if self.bounty_hunter_overheating_timer <= self.bounty_hunter_overheating_timer_max:

            if self.bounty_hunter_timer <= 0:
                enemy_laser_gun = Enemy_laser_gun(self.rect.center, 1, 1500, 10, 25, 25, "#73FE1E")
                enemies_laser_guns.add(enemy_laser_gun)
                self.bounty_hunter_timer = enemy_laser_gun.fire_rate

            self.bounty_hunter_timer += -100
            self.bounty_hunter_overheating_timer += 100
            self.bounty_hunter_overheating_timer_2 = 0

        else:

            if self.bounty_hunter_overheating_timer_2 >= self.bounty_hunter_overheating_timer_max*2:
                self.bounty_hunter_overheating_timer = 0

            self.bounty_hunter_overheating_timer_2 += 100

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