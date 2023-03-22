import pygame

from Guns_package.bullet_type_gun_package.minigun import Minigun
from Guns_package.bullet_type_gun_package.rocket_launcher import Rocket_launcher
from Guns_package.laser_type_gun_package.laser_thrower import Laser_thrower
from Guns_package.laser_type_gun_package.laser_rifle import Laser_rifle
from Guns_package.laser_type_gun_package.laser_ring import Laser_ring

from Consts_package.consts import guns, SCREEN_WIDTH, SCREEN_HEIGHT
from Guns_package.bullet_type_gun_package.sniper_rifle import Sniper_rifle


# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Stats
        self.speed = 10
        self.hp = 3

        # Equipment
        self.gun_list = ["Minigun", "Rocket_launcher", "Laser_thrower", "Laser_rifle", "Laser_ring", "Sniper_rifle"]
        self.gun_index = 0
        self.using_gun_type = self.gun_list[self.gun_index]

        # Weapon upgrade
        self.gun_damage_multiplier = 1
        self.gun_fire_rate_multiplier = 1

        # Obtained gun
        self.minigun = True
        self.rocket_launcher = False
        self.flame_thrower = False
        self.laser_rifle = False
        self.laser_ring = False
        self.sniper_rifle = False

        # Timer
        self.player_timer = 0

        # Image data
        self.width = 50
        self.height = 50
        self.color = '#384426'

        # Image
        self.image = pygame.image.load('Additional_resources/Graphics/Space_lord.png').convert_alpha()
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT-SCREEN_HEIGHT/10)

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
                self.rect.left = SCREEN_WIDTH
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.left >= SCREEN_WIDTH:
                self.rect.right = 0
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            if self.rect.top <= 0:
                self.rect.top = 0
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

    def shooting(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.using_gun_type == 'Minigun' and self.player_timer <= 0:
            laser_gun = Minigun(self.rect.center, self.gun_damage_multiplier, self.gun_fire_rate_multiplier)
            guns.add(laser_gun)
            self.player_timer = laser_gun.fire_rate

        if keys[pygame.K_SPACE] and self.using_gun_type == 'Rocket_launcher' and self.player_timer <= 0:
            rocket_launcher = Rocket_launcher(self.rect.center, self.gun_damage_multiplier, self.gun_fire_rate_multiplier)
            guns.add(rocket_launcher)
            self.player_timer = rocket_launcher.fire_rate

        if keys[pygame.K_SPACE] and self.using_gun_type == 'Laser_thrower' and self.player_timer <= 0:
            flame_thrower = Laser_thrower(self.rect.center, self.gun_damage_multiplier, self.gun_fire_rate_multiplier)
            guns.add(flame_thrower)
            self.player_timer = flame_thrower.fire_rate

        if keys[pygame.K_SPACE] and self.using_gun_type == 'Laser_rifle' and self.player_timer <= 0:
            laser_rifle = Laser_rifle(self.rect.center, self.gun_damage_multiplier, self.gun_fire_rate_multiplier)
            guns.add(laser_rifle)
            self.player_timer = laser_rifle.fire_rate

        if keys[pygame.K_SPACE] and self.using_gun_type == 'Laser_ring' and self.player_timer <= 0:
            laser_ring = Laser_ring(self.rect.center, self.gun_damage_multiplier, self.gun_fire_rate_multiplier)
            guns.add(laser_ring)
            self.player_timer = laser_ring.fire_rate

        if keys[pygame.K_SPACE] and self.using_gun_type == 'Sniper_rifle' and self.player_timer <= 0:
            sniper_rifle = Sniper_rifle(self.rect.center, self.gun_damage_multiplier, self.gun_fire_rate_multiplier)
            guns.add(sniper_rifle)
            self.player_timer = sniper_rifle.fire_rate

        self.player_timer += -100

    def change_gun(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and self.minigun:
            self.using_gun_type = self.gun_list[0]

        if keys[pygame.K_2] and self.rocket_launcher:
            self.using_gun_type = self.gun_list[1]

        if keys[pygame.K_3] and self.flame_thrower:
            self.using_gun_type = self.gun_list[2]

        if keys[pygame.K_4] and self.laser_rifle:
            self.using_gun_type = self.gun_list[3]

        if keys[pygame.K_5] and self.laser_ring:
            self.using_gun_type = self.gun_list[4]

        if keys[pygame.K_6] and self.sniper_rifle:
            self.using_gun_type = self.gun_list[5]

    def update(self):
        self.movement()
        self.shooting()
        self.change_gun()
