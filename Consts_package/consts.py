import pygame

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Game
game_over = False
gameplay_state = False
first_run = True
is_first_boss_arrived = False

# Player
players = pygame.sprite.Group()

# Guns
guns = pygame.sprite.Group()

# Enemies
enemies = pygame.sprite.Group()
enemies_laser_guns = pygame.sprite.Group()

# Bonuses
bonuses = pygame.sprite.Group()