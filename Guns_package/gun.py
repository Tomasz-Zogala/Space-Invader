import pygame

from Bonuses_package.bonus import Bonus
from Bonuses_package.score_bonus import Score_bonus
from Enemies_package.asteroid import Asteroid
from Enemies_package.star_lord import Star_lord
from Consts_package.consts import bonuses, enemies, guns


# Define the Gun class
class Gun(pygame.sprite.Sprite):
    def __init__(self, center, damage_multiplier, fire_rate_multiplier):
        super().__init__()

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

        # Audio
        # self.laser_audio = pygame.mixer.Sound()
        # self.laser_audio.set_volume(0.2)
        # self.laser_audio.play()

    def movement(self):
        self.rect.y += -self.bullet_speed

        if self.rect.y < -100:
            self.kill()

    def hit_service(self):
        collided_enemies = pygame.sprite.spritecollide(self, enemies, False)

        if collided_enemies:
            for enemy in collided_enemies:
                pygame.sprite.spritecollide(enemy, guns, True)
                enemy.hp += -self.damage
                if enemy.hp <= 0:
                    if type(enemy) == Asteroid:

                        enemy.kill()

                        bonus = Score_bonus(enemy.rect.center, enemy.speed_y * 2)
                        bonuses.add(bonus)

                        enemy = Asteroid()
                        enemies.add(enemy)
                    elif type(enemy) == Star_lord:
                        enemy.kill()
                        for i in range(2):
                            asteroid = Asteroid()
                            enemies.add(asteroid)

    def update(self):
        self.movement()
        self.hit_service()
