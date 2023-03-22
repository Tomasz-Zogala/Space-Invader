import pygame

from Consts_package.consts import players


# Define the abstract Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Stats
        self.hp = 0
        self.speed_x = 0
        self.speed_y = 0

        # Image data
        self.width = 0
        self.height = 0
        self.color = '#000000'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.x = self.width
        self.rect.y = self.height

    def movement(self):
        pass

    def attack_ranged(self):
        pass

    def attack_melee(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

    def update(self):
        pass
