import pygame

from Enemies_package.enemy import Enemy
from enemy_laser_gun.enemy_laser_gun import Enemy_laser_gun
from Consts_package.consts import enemies_laser_guns, SCREEN_WIDTH, players


# Define the Star_lord class
class Star_lord(Enemy):
    def __init__(self):
        super().__init__()

        # Stats
        self.hp = 120
        self.speed_x = 3
        self.speed_y = 2
        self.damage = 1

        # Timer
        self.star_lord_timer = 0

        # Image data
        self.width = 100
        self.height = 50
        self.color = '#145343'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = (SCREEN_WIDTH/2, 50)

    def movement(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left == SCREEN_WIDTH:
            self.rect.right = 0

        if self.rect.bottom >= 150:
            self.speed_y = self.speed_y*-1

        if self.rect.top <= 0:
            self.speed_y = self.speed_y * -1

    def attack_ranged(self):
        if self.star_lord_timer <= 0:
            enemy_laser_gun = Enemy_laser_gun(self.rect.center, 1, 2500, 5, 30, 30, "#FE1E1E")
            enemies_laser_guns.add(enemy_laser_gun)
            self.star_lord_timer = enemy_laser_gun.fire_rate
        self.star_lord_timer += -100

    def attack_melee(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

    def hp_service(self):
        if self.hp <= 30:
            self.image.fill('#451212')

    def update(self):
        self.attack_ranged()
        self.attack_melee()
        self.movement()
        self.hp_service()