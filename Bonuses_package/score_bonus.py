import pygame

from Bonuses_package.bonus import Bonus


# Define the Bonus class
class Score_bonus(Bonus):
    def __init__(self, center, speed):
        super().__init__(center, speed)

        # Stats
        self.speed = speed

        # Image data
        self.color = '#A6E742'
        self.height = 40
        self.weight = 40

        # Image
        self.image = pygame.Surface([self.weight, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

    def update(self):
        self.movement()
