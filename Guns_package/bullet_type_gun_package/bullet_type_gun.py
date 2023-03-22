import pygame

from Bonuses_package.gun_bonus import Gun_bonus
from Bonuses_package.hp_bonus import Hp_bonus
from Bonuses_package.stats_bonus import Stats_bonus
from Enemies_package.asteroid import Asteroid
from Enemies_package.bounty_hunter import Bounty_hunter
from Enemies_package.star_lord import Star_lord
from Consts_package.consts import bonuses, enemies, guns
from Guns_package.gun import Gun


# Define the abstract Bullet_type_gun class
class Bullet_type_gun(Gun):
    def __init__(self, center, damage_multiplier, fire_rate_multiplier):
        super().__init__(center, damage_multiplier, fire_rate_multiplier)

        # Stats
        self.damage = 0 * damage_multiplier
        self.fire_rate = 0 * fire_rate_multiplier
        self.bullet_speed = 0

        # Image data
        self.width = 0
        self.height = 0
        self.color = '#938D8D'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

    def movement(self):
        self.rect.y += -self.bullet_speed
        if self.rect.y < -100:
            self.kill()

    def killing(self, enemy):
        if type(enemy) == Asteroid:
            enemy.kill()
            bonus = Gun_bonus(enemy.rect.center, enemy.speed_y * 2)
            bonuses.add(bonus)
            enemy = Asteroid()
            enemies.add(enemy)

        elif type(enemy) == Star_lord:
            enemy.kill()
            self.kill()
            for i in range(2):
                asteroid = Asteroid()
                enemies.add(asteroid)

        elif type(enemy) == Bounty_hunter:
            enemy.kill()
            self.kill()
            for i in range(2):
                asteroid = Asteroid()
                enemies.add(asteroid)

    def hit_service(self):
        collided_enemies = pygame.sprite.spritecollide(self, enemies, False)
        if collided_enemies:
            for enemy in collided_enemies:
                pygame.sprite.spritecollide(enemy, guns, True)
                enemy.hp += -self.damage
                if enemy.hp <= 0:
                    self.killing(enemy)
