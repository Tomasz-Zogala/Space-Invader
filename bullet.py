import pygame
import random

from bonus import Bonus
from enemy import Enemy
from sprites import bullets, enemies, bonuses


# Define the Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, dmg):
        super().__init__()
        self.dmg = dmg
        self.image = pygame.Surface([10, 15])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        # Move the bullet up the screen
        self.rect.y += -10

        collided_enemies = pygame.sprite.spritecollide(self, enemies, False)
        if collided_enemies:
            for enemy in collided_enemies:
                if(enemy.hp > 0):
                    enemy.hp += -self.dmg
                    enemy.height += -5
                    enemy.weight += -5
                else:
                    bonus = Bonus(enemy.rect.x, enemy.rect.y, enemy.speed)
                    enemy.kill()
                    bonuses.add(bonus)
                    enemy = Enemy(random.randrange(2, 4))
                    enemies.add(enemy)

        # Remove the bullet if it goes off the top of the screen
        if self.rect.y < -100:
            self.kill()
