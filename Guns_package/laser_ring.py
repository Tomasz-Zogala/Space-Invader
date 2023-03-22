import pygame

from Bonuses_package.bonus import Bonus
from Bonuses_package.score_bonus import Score_bonus
from Enemies_package.asteroid import Asteroid
from Enemies_package.star_lord import Star_lord
from Guns_package.gun import Gun
from Consts_package.consts import bonuses, enemies


# Define the Laser_ring class
class Laser_ring(Gun):
    def __init__(self, center):
        super().__init__(center)

        # Stats
        self.damage = 0.1
        self.fire_rate = 80
        self.bullet_speed = 10
        self.range_timer_max = 150
        self.range_timer_min = 0

        # Image data
        self.width = 250
        self.height = 250
        self.color = '#033BFB'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

        # Audio
        self.laser_audio = pygame.mixer.Sound('Additional_resources/Audio/Laser_ring_audio.mp3')
        self.laser_audio.set_volume(0.2)
        self.laser_audio.play()

    def movement(self):
        self.rect.y += -self.bullet_speed

        if self.range_timer_max <= self.range_timer_min:
            self.kill()
            self.range_timer_max = 0
        self.range_timer_min += 100

    def hit_service(self):
        collided_enemies = pygame.sprite.spritecollide(self, enemies, False)

        if collided_enemies:
            for enemy in collided_enemies:
                if enemy.hp - self.damage >= 0 or enemy.hp > 0:  # LASER GUN ISSUES ROCKET GREAT
                    enemy.hp += -self.damage
                elif type(enemy) == Asteroid:
                    enemy.kill()
                    self.kill()

                    bonus = Score_bonus(enemy.rect.center, enemy.speed_y * 2)
                    bonuses.add(bonus)

                    enemy = Asteroid()
                    enemies.add(enemy)
                elif type(enemy) == Star_lord:
                    enemy.kill()
                    self.kill()
                    for i in range(2):
                        asteroid = Asteroid()
                        enemies.add(asteroid)

    def update(self):
        self.movement()
        self.hit_service()
