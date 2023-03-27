import threading

import pygame
import random

from Guns_package.gun import Gun

from Bonuses_package.score_bonus import Score_bonus
from Bonuses_package.stats_bonus import Stats_bonus
from Bonuses_package.hp_bonus import Hp_bonus
from Bonuses_package.gun_bonus import Gun_bonus

from Enemies_package.asteroid import Asteroid
from Enemies_package.stardust import Stardust
from Enemies_package.star_lord import Star_lord
from Enemies_package.bounty_hunter import Bounty_hunter
from Enemies_package.ghast_of_the_void import Ghast_of_the_void
from Enemies_package.galactic_devourer import Galactic_devourer

from Constants_package.constants import bonuses, enemies, SCALE


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

        # Audio
        self.boss_died_audio = pygame.mixer.Sound("Additional_resources/Audio/laser_rifle.mp3")
        self.boss_died_audio.set_volume(0.5)

        # Mutex
        self.lock_for_adding_enemies = threading.Lock()
        self.lock_for_adding_bonuses = threading.Lock()

    def movement_service(self):
        pass

    def killing_enemy_service(self, enemy):
        if type(enemy) == Asteroid:
            if self.bonus_probability <= 60:
                bonus = Score_bonus(enemy.rect.center)
                self.lock_for_adding_bonuses.acquire()
                bonuses.add(bonus)
                self.lock_for_adding_bonuses.release()
            elif 60 < self.bonus_probability <= 80:
                bonus = Stats_bonus(enemy.rect.center)
                self.lock_for_adding_bonuses.acquire()
                bonuses.add(bonus)
                self.lock_for_adding_bonuses.release()
            elif 80 < self.bonus_probability <= 95:
                bonus = Hp_bonus(enemy.rect.center)
                self.lock_for_adding_bonuses.acquire()
                bonuses.add(bonus)
                self.lock_for_adding_bonuses.release()
            else:
                enemy = Asteroid()
                self.lock_for_adding_enemies.acquire()
                enemies.add(enemy)
                self.lock_for_adding_enemies.release()
                bonus = Gun_bonus(enemy.rect.center)
                self.lock_for_adding_bonuses.acquire()
                bonuses.add(bonus)
                self.lock_for_adding_bonuses.release()
            enemy.kill()
            enemy = Asteroid()
            self.lock_for_adding_enemies.acquire()
            enemies.add(enemy)
            self.lock_for_adding_enemies.release()

        elif type(enemy) == Star_lord:
            self.boss_died_audio.play()
            bonus = Gun_bonus(enemy.rect.center)
            self.lock_for_adding_bonuses.acquire()
            bonuses.add(bonus)
            self.lock_for_adding_bonuses.release()
            bonus = Hp_bonus(enemy.rect.center)
            self.lock_for_adding_bonuses.acquire()
            bonuses.add(bonus)
            self.lock_for_adding_bonuses.release()
            if self.bonus_probability <= 90:
                bonus = Score_bonus(enemy.rect.center)
                self.lock_for_adding_bonuses.acquire()
                bonuses.add(bonus)
                self.lock_for_adding_bonuses.release()
            else:
                bonus = Stats_bonus(enemy.rect.center)
                self.lock_for_adding_bonuses.acquire()
                bonuses.add(bonus)
                self.lock_for_adding_bonuses.release()
            enemy.kill()
            enemy = Asteroid()
            self.lock_for_adding_enemies.acquire()
            enemies.add(enemy)
            self.lock_for_adding_enemies.release()

        elif type(enemy) == Bounty_hunter:
            self.boss_died_audio.play()
            bonus = Gun_bonus(enemy.rect.center)
            self.lock_for_adding_bonuses.acquire()
            bonuses.add(bonus)
            self.lock_for_adding_bonuses.release()
            bonus = Hp_bonus(enemy.rect.center)
            self.lock_for_adding_bonuses.acquire()
            bonuses.add(bonus)
            self.lock_for_adding_bonuses.release()
            if self.bonus_probability <= 90:
                bonus = Score_bonus(enemy.rect.center)
                self.lock_for_adding_bonuses.acquire()
                bonuses.add(bonus)
                self.lock_for_adding_bonuses.release()
            else:
                bonus = Stats_bonus(enemy.rect.center)
                self.lock_for_adding_bonuses.acquire()
                bonuses.add(bonus)
                self.lock_for_adding_bonuses.release()
            enemy.kill()
            enemy = Asteroid()
            self.lock_for_adding_enemies.acquire()
            enemies.add(enemy)
            self.lock_for_adding_enemies.release()

        elif type(enemy) == Ghast_of_the_void:
            self.boss_died_audio.play()
            bonus = Gun_bonus(enemy.rect.center)
            self.lock_for_adding_bonuses.acquire()
            bonuses.add(bonus)
            self.lock_for_adding_bonuses.release()
            bonus = Hp_bonus(enemy.rect.center)
            self.lock_for_adding_bonuses.acquire()
            bonuses.add(bonus)
            self.lock_for_adding_bonuses.release()
            if self.bonus_probability <= 90:
                bonus = Score_bonus(enemy.rect.center)
                self.lock_for_adding_bonuses.acquire()
                bonuses.add(bonus)
                self.lock_for_adding_bonuses.release()
            else:
                bonus = Stats_bonus(enemy.rect.center)
                self.lock_for_adding_bonuses.acquire()
                bonuses.add(bonus)
                self.lock_for_adding_bonuses.release()
            enemy.kill()
            enemy = Asteroid()
            self.lock_for_adding_enemies.acquire()
            enemies.add(enemy)
            self.lock_for_adding_enemies.release()

        elif type(enemy) == Galactic_devourer:
            self.boss_died_audio.play()
            bonus = Gun_bonus(enemy.rect.center)
            self.lock_for_adding_bonuses.acquire()
            bonuses.add(bonus)
            self.lock_for_adding_bonuses.release()
            bonus = Hp_bonus(enemy.rect.center)
            self.lock_for_adding_bonuses.acquire()
            bonuses.add(bonus)
            self.lock_for_adding_bonuses.release()
            if self.bonus_probability <= 90:
                bonus = Score_bonus(enemy.rect.center)
                self.lock_for_adding_bonuses.acquire()
                bonuses.add(bonus)
                self.lock_for_adding_bonuses.release()
            else:
                bonus = Stats_bonus(enemy.rect.center)
                self.lock_for_adding_bonuses.acquire()
                bonuses.add(bonus)
                self.lock_for_adding_bonuses.release()
            enemy.kill()
            enemy = Asteroid()
            self.lock_for_adding_enemies.acquire()
            enemies.add(enemy)
            self.lock_for_adding_enemies.release()

        elif type(enemy) == Stardust:
            enemy.kill()

    def collision_with_enemy_service(self):
        collided_enemies = pygame.sprite.spritecollide(self, enemies, False)
        if collided_enemies:
            for enemy in collided_enemies:
                enemy.hp += -self.damage
                if enemy.hp <= 0:
                    self.killing_enemy_service(enemy)
