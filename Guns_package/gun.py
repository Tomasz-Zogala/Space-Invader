import pygame

from Bonuses_package.bonus import Bonus
from Enemies_package.asteroid import Asteroid
from Sprites_package.sprites import asteroids, bonuses, star_lords


# Define the Gun class
class Gun(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()

        # Stats
        self.damage = 1
        self.fire_rate = 300

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
        collided_asteroid = pygame.sprite.spritecollide(self, asteroids, False)
        if collided_asteroid:
            for asteroid in collided_asteroid:
                if asteroid.hp > 1:
                    asteroid.hp += -self.damage
                else:
                    bonus = Bonus(asteroid.rect.center, asteroid.speed*2)
                    asteroid.kill()
                    self.kill()
                    bonuses.add(bonus)
                    asteroid = Asteroid()
                    asteroids.add(asteroid)

        collided_star_lord = pygame.sprite.spritecollide(self, star_lords, False)
        if collided_star_lord:
            for star_lord in collided_star_lord:
                if star_lord.hp > 1:
                    star_lord.hp += -self.damage
                else:
                    star_lord.kill()
                    self.kill()

    def update(self):
        self.movement()
        self.hit_service()
