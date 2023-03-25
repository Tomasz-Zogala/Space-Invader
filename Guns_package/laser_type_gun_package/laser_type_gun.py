import pygame
import random

from Bonuses_package.gun_bonus import Gun_bonus
from Bonuses_package.hp_bonus import Hp_bonus
from Bonuses_package.score_bonus import Score_bonus
from Bonuses_package.stats_bonus import Stats_bonus
from Enemies_package.asteroid import Asteroid
from Enemies_package.bounty_hunter import Bounty_hunter
from Enemies_package.galactic_devourer import Galactic_devourer
from Enemies_package.ghast_of_the_void import Ghast_of_the_void
from Enemies_package.star_lord import Star_lord
from Consts_package.consts import bonuses, enemies, SCALE
from Enemies_package.stardust import Stardust
from Guns_package.gun import Gun


# Define the abstract Laser_type_gun class
class Laser_type_gun(Gun):
    def __init__(self, center, damage_multiplier, fire_rate_multiplier):
        super().__init__(center, damage_multiplier, fire_rate_multiplier)

        # Stats
        self.damage = 0 * damage_multiplier
        self.fire_rate = 0 * fire_rate_multiplier
        self.bullet_speed = 0 * SCALE
        self.bonus_probability = random.randrange(0, 100)

        # Image data
        self.width = 0 * SCALE
        self.height = 0 * SCALE
        self.color = '#000000'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

    def movement(self):
        pass

    def killing(self, enemy):
        if type(enemy) == Asteroid:
            enemy.kill()
            if self.bonus_probability <= 60:
                bonus = Score_bonus(enemy.rect.center, enemy.speed_y * 0.5)
                bonuses.add(bonus)
            elif 60 < self.bonus_probability <= 80:
                bonus = Stats_bonus(enemy.rect.center, enemy.speed_y * 0.5)
                bonuses.add(bonus)
            elif 80 < self.bonus_probability <= 95:
                bonus = Hp_bonus(enemy.rect.center, enemy.speed_y * 0.5)
                bonuses.add(bonus)
            else:
                bonus = Gun_bonus(enemy.rect.center, enemy.speed_y * 0.5)
                bonuses.add(bonus)
            enemy = Asteroid()
            enemies.add(enemy)

        elif type(enemy) == Star_lord:
            enemy.kill()
            bonus = Gun_bonus(enemy.rect.center, enemy.speed_y * 0.3)
            bonuses.add(bonus)
            bonus = Hp_bonus(enemy.rect.center, enemy.speed_y * 0.5)
            bonuses.add(bonus)
            if self.bonus_probability <= 90:
                bonus = Score_bonus(enemy.rect.center, enemy.speed_y * 1)
                bonuses.add(bonus)
            else:
                bonus = Stats_bonus(enemy.rect.center, enemy.speed_y * 1)
                bonuses.add(bonus)

        elif type(enemy) == Bounty_hunter:
            enemy.kill()
            bonus = Gun_bonus(enemy.rect.center, enemy.speed_y * 0.3)
            bonuses.add(bonus)
            bonus = Hp_bonus(enemy.rect.center, enemy.speed_y * 0.5)
            bonuses.add(bonus)
            if self.bonus_probability <= 90:
                bonus = Score_bonus(enemy.rect.center, enemy.speed_y * 1)
                bonuses.add(bonus)
            else:
                bonus = Stats_bonus(enemy.rect.center, enemy.speed_y * 1)
                bonuses.add(bonus)

        elif type(enemy) == Ghast_of_the_void:
            enemy.kill()
            bonus = Gun_bonus(enemy.rect.center, enemy.speed_y * 0.3)
            bonuses.add(bonus)
            bonus = Hp_bonus(enemy.rect.center, enemy.speed_y * 0.5)
            bonuses.add(bonus)
            if self.bonus_probability <= 90:
                bonus = Score_bonus(enemy.rect.center, enemy.speed_y * 1)
                bonuses.add(bonus)
            else:
                bonus = Stats_bonus(enemy.rect.center, enemy.speed_y * 1)
                bonuses.add(bonus)

        elif type(enemy) == Galactic_devourer:
            enemy.kill()
            bonus = Gun_bonus(enemy.rect.center, enemy.speed_y * 0.3)
            bonuses.add(bonus)
            bonus = Hp_bonus(enemy.rect.center, enemy.speed_y * 0.5)
            bonuses.add(bonus)
            if self.bonus_probability <= 90:
                bonus = Score_bonus(enemy.rect.center, enemy.speed_y * 1)
                bonuses.add(bonus)
            else:
                bonus = Stats_bonus(enemy.rect.center, enemy.speed_y * 1)
                bonuses.add(bonus)

        elif type(enemy) == Stardust:
            enemy.kill()

    def hit_service(self):
        collided_enemies = pygame.sprite.spritecollide(self, enemies, False)
        if collided_enemies:
            for enemy in collided_enemies:
                enemy.hp += -self.damage
                if enemy.hp <= 0:
                    self.killing(enemy)
