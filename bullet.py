import pygame

from bonus import Bonus
from enemy import Enemy
from sprites import enemies, bonuses


# Define the Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()

        # Stats
        self.dmg = 1

        # Image data
        self.width = 10
        self.height = 15
        self.color = '#938D8D'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

        # Audio
        self.laser_audio = pygame.mixer.Sound('Audio/Laser_sound.mp3')
        self.laser_audio.set_volume(0.2)
        self.laser_audio.play()

    def movement(self):
        self.rect.y += -10

        if self.rect.y < -100:
            self.kill()

    def hit_service(self):
        collided_enemies = pygame.sprite.spritecollide(self, enemies, False)
        if collided_enemies:
            for enemy in collided_enemies:
                if enemy.hp > 0:
                    enemy.hp += -self.dmg
                else:
                    bonus = Bonus(enemy.rect.center, enemy.speed*2)
                    enemy.kill()
                    bonuses.add(bonus)
                    enemy = Enemy()
                    enemies.add(enemy)

    def update(self):
        self.movement()
        self.hit_service()
