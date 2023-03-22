import pygame


from Consts_package.consts import players, enemies_laser_guns, SCREEN_HEIGHT


class Enemy_laser_gun(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()

        # Stats
        self.damage = 1
        self.fire_rate = 1000
        self.bullet_speed = 15

        # Image data
        self.width = 15
        self.height = 30
        self.color = '#000000'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

        # Audio
        # self.laser_audio = pygame.mixer.Sound()
        # self.laser_audio.set_volume(0.2)
        # self.laser_audio.play()

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