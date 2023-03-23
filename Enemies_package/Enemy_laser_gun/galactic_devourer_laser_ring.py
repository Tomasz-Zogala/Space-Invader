import pygame


from Consts_package.consts import players, SCALE
from Enemies_package.Enemy_laser_gun.enemy_laser_gun import Enemy_laser_gun


class Galactic_devourer_laser_ring(Enemy_laser_gun):
    def __init__(self, center, damage, fire_rate, bullet_speed, width, height, color):
        super().__init__(center, damage, fire_rate, bullet_speed, width, height, color)

        self.range_timer_max = 150 * SCALE
        self.range_timer_min = 0

        # Audio

    def movement(self):
        self.rect.y += -self.bullet_speed

        if self.range_timer_max <= self.range_timer_min:
            self.kill()
            self.range_timer_max = 0
        self.range_timer_min += 100

    def hit_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

    def update(self):
        self.movement()
        self.hit_service()