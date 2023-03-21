import pygame

from Bonuses_package.bonus import Bonus
from Enemies_package.asteroid import Asteroid
from Enemies_package.star_lord import Star_lord
from Sprites_package.sprites import bonuses, enemies


# Define the Gun class
class Gun(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()

        # Stats
        self.damage = 0
        self.fire_rate = 0
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
        self.laser_audio = pygame.mixer.Sound('Additional_resources/Audio/Laser_sound.mp3')
        self.laser_audio.set_volume(0.2)
        self.laser_audio.play()

    def movement(self):
        self.rect.y += -self.bullet_speed

        if self.rect.y < -100:
            self.kill()

    def hit_service(self):
        collided_enemies = pygame.sprite.spritecollide(self, enemies, False)

        if collided_enemies:
            for enemy in collided_enemies:
                if enemy.hp > 0:
                    enemy.hp += -self.damage
                elif type(enemy) == Asteroid:
                    bonus = Bonus(enemy.rect.center, enemy.speed_y * 2)
                    enemy.kill()
                    self.kill()
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
