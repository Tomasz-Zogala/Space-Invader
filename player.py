import pygame

from bonus import Bonus
from bullet import Bullet
from sprites import bullets, bonuses
# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Stats
        self.speed = 10
        self.hp = 3
        # Weapon
        self.bullet_timer = 0
        self.bullet_delay = 1500
        self.bullet_dmg = 1
        self.weapon_upgrade_timer = 0

        # Image data
        self.width = 50
        self.height = 50
        self.color = '#384426'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.centerx = 400
        self.rect.centery = 700

        # Audio
        self.player_appear_audio = pygame.mixer.Sound("Audio/Boss_appear.mp3")
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
        if keys[pygame.K_SPACE] and self.bullet_timer >= self.bullet_delay:
            # Create a new bullet sprite and add it to the bullets group
            bullet = Bullet(self.rect.center)
            bullets.add(bullet)
            self.bullet_timer = 0
        self.bullet_timer += 100
    def bonus_service(self):
        collided_bonus = pygame.sprite.spritecollide(self, bonuses, True)
        if collided_bonus:
            self.score += 10
    def update(self):
        self.movement()
        self.shooting()
        self.bonus_service()