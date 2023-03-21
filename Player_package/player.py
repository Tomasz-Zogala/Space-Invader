import pygame

from Guns_package.laser_gun import Laser_gun
from Guns_package.rocket_launcher import Rocket_launcher
from Sprites_package.sprites import guns, bonuses


# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Stats
        self.speed = 10
        self.player_timer = 0
        self.using_weapon_type = "Rocket_launcher"

        # Image data
        self.width = 50
        self.height = 50
        self.color = '#384426'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = (400, 700)

        # Audio
        self.player_appear_audio = pygame.mixer.Sound("Additional_resources/Audio/Boss_appear.mp3")
        self.player_appear_audio.set_volume(0.5)
        self.player_appear_audio.play()

        # Info
        self.score = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.right <= 0:
                self.rect.left = 800
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.left >= 800:
                self.rect.right = 0
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            if self.rect.top <= 0:
                self.rect.top = 0
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            if self.rect.bottom >= 800:
                self.rect.bottom = 800

    def shooting(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.using_weapon_type == 'Laser_gun' and self.player_timer <= 0:
            laser_gun = Laser_gun(self.rect.center)
            guns.add(laser_gun)
            self.player_timer = laser_gun.fire_rate

        if keys[pygame.K_SPACE] and self.using_weapon_type == 'Rocket_launcher' and self.player_timer <= 0:
            rocket_launcher = Rocket_launcher(self.rect.center)
            guns.add(rocket_launcher)
            self.player_timer = rocket_launcher.fire_rate

        self.player_timer += -100



    def bonus_service(self):
        collided_bonus = pygame.sprite.spritecollide(self, bonuses, True)
        if collided_bonus:
            self.score += 100

    def update(self):
        self.movement()
        self.shooting()
        self.bonus_service()
