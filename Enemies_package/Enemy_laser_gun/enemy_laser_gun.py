import pygame


from Consts_package.consts import players, enemies_laser_guns, SCREEN_HEIGHT


class Enemy_laser_gun(pygame.sprite.Sprite):
    def __init__(self, center, damage, fire_rate, bullet_speed, width, height, color):
        super().__init__()

        # Stats
        self.damage = damage
        self.fire_rate = fire_rate
        self.bullet_speed = bullet_speed

        # Image data
        self.width = width
        self.height = height
        self.color = color

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

        # Audio

    def movement(self):
        self.rect.y += self.bullet_speed

        if self.rect.y > SCREEN_HEIGHT+100:
            self.kill()

    def hit_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                pygame.sprite.spritecollide(player, enemies_laser_guns, True)
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

    def update(self):
        self.movement()
        self.hit_service()