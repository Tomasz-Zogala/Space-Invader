import pygame

from Enemies_package.enemy import Enemy
from Enemies_package.Enemy_laser_gun.enemy_laser_gun import Enemy_laser_gun
from Consts_package.consts import enemies_laser_guns, SCREEN_WIDTH, players, enemies, SCREEN_HEIGHT, SCALE


# Define the Ghast_of_the_void class
class Ghast_of_the_void(Enemy):
    def __init__(self, pos_x=SCREEN_HEIGHT/16, pos_y=SCREEN_HEIGHT/16, move_direction=1, first_in_colony=False):
        super().__init__()

        # Stats
        self.damage = 1
        self.hp = 120
        self.speed_x = 4 * SCALE
        self.speed_y = 0 * SCALE
        self.move_direction = move_direction
        self.first_in_colony = first_in_colony

        # Timer
        self.ghast_of_the_void_timer = 0

        # Image data
        self.width = 45 * SCALE
        self.height = 70 * SCALE
        self.color = '#145343'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect.center = (self.pos_x, self.pos_y)

    def movement(self):

        if self.first_in_colony:
            self.rect.x += self.speed_x * self.move_direction * 2
        else:
            self.rect.x += self.speed_x * self.move_direction

        if self.rect.left >= SCREEN_WIDTH:
            self.speed_x = self.speed_x * -1
            ghast_of_the_void = Ghast_of_the_void(SCREEN_WIDTH - 50 * SCALE, 50 * SCALE, -1)
            enemies.add(ghast_of_the_void)
            self.rect.top += 100 * SCALE
            self.first_in_colony = False

        if self.rect.right <= 0:
            self.speed_x = self.speed_x * -1
            ghast_of_the_void = Ghast_of_the_void()
            enemies.add(ghast_of_the_void)
            self.rect.top += 100 * SCALE
            self.first_in_colony = False

        if self.rect.top >= SCREEN_WIDTH + 100:
            self.kill()

    def attack_ranged(self):
        if self.ghast_of_the_void_timer <= 0:
            enemy_laser_gun = Enemy_laser_gun(self.rect.center, 0.2, 2000, 15, 15, 45, "#FE1E1E")
            enemies_laser_guns.add(enemy_laser_gun)
            self.ghast_of_the_void_timer = enemy_laser_gun.fire_rate
        self.ghast_of_the_void_timer += -100

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