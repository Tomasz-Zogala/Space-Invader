import pygame

from bonus import Bonus
from bullet import Bullet
from sprites import bullets, bonuses


# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill("BLACK")
        self.rect = self.image.get_rect()

        # Starting point
        self.rect.centerx = 400
        self.rect.centery = 750

        # Weapon
        self.bullet_timer = 0
        self.bullet_delay = 1200
        self.bullet_dmg = 1
        self.weapon_upgrade_timer = 0

        # Stats
        self.speed = 10
        self.hp = 3

        # Audio
        self.player_appear_audio = pygame.mixer.Sound("Audio/Boss_appear.mp3")
        self.player_appear_audio.set_volume(0.5)
        self.player_appear_audio.play()

    def update(self):
        # Bonus getting
        collided_bonus = pygame.sprite.spritecollide(self, bonuses, True)
        if collided_bonus:
            self.bullet_dmg += 1

        # Move the player based on arrow key input
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
        if keys[pygame.K_SPACE] and self.bullet_timer >= self.bullet_delay:
            # Create a new bullet sprite and add it to the bullets group
            bullet = Bullet(self.rect.centerx-5, self.rect.centery, self.bullet_dmg)
            bullets.add(bullet)
            self.bullet_timer = 0

        # Increment the timer variable by the time elapsed since the last frame
        self.bullet_timer += 100