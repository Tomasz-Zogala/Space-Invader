import pygame


# Define the Enemy class
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

    def hp_service(self):
        pass

    def update(self):
        pass

        #
        #
        # if self.rect.right >= ((SCREEN_WIDTH*2) / 3):
        #     self.speed_x = self.speed_x * -1
        #
        # if self.rect.left <= SCREEN_WIDTH/3:
        #     self.speed_x = self.speed_x * -1
        #
        # if self.rect.top <= SCREEN_HEIGHT/3:
        #     self.speed_y = self.speed_y * -1
        #
        # if self.rect.bottom >= ((SCREEN_HEIGHT*2) / 3):
        #     self.speed_y = self.speed_y * -1