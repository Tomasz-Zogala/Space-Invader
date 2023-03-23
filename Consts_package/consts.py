import pygame

# Screen
# SCREEN_WIDTH = 2560
# SCREEN_HEIGHT = 1600

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Game
game_over = False
gameplay_state = False
first_run = True
star_lord_arrived = False
bounty_hunter_arrived = False

# Player
players = pygame.sprite.Group()

# Guns
guns = pygame.sprite.Group()

# Enemies
enemies = pygame.sprite.Group()
enemies_laser_guns = pygame.sprite.Group()

# Bonuses
bonuses = pygame.sprite.Group()