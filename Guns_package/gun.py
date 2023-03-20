import pygame

from Bonuses_package.bonus import Bonus
from Enemies_package.asteroid import Asteroid
from Sprites_package.sprites import asteroids, bonuses


# Define the Gun class
class Gun(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()

        # Stats
        self.damage = 1
        self.fire_rate = 1500

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
        self.laser_audio = pygame.mixer.Sound('Additional_resources/Audio/Laser_sound.mp3')
        self.laser_audio.set_volume(0.2)
        self.laser_audio.play()

    def movement(self):
        self.rect.y += -10

        if self.rect.y < -100:
            self.kill()

    def hit_service(self):
        collided_enemies = pygame.sprite.spritecollide(self, asteroids, False)
        if collided_enemies:
            for enemy in collided_enemies:
                if enemy.hp > 1:
                    enemy.hp += -self.damage
                else:
                    bonus = Bonus(enemy.rect.center, enemy.speed*2)
                    enemy.kill()
                    self.kill()
                    bonuses.add(bonus)
                    asteroid = Asteroid()
                    asteroids.add(asteroid)

    def update(self):
        self.movement()
        self.hit_service()
