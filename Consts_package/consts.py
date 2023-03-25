import pygame

fullscreen = True

# Screen
if fullscreen:
    SCREEN_WIDTH = 2560
    SCREEN_HEIGHT = 1600
    SCALE = SCREEN_HEIGHT/800
else:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 800
    SCALE = SCREEN_HEIGHT/800

# Game
game_over = False
gameplay_state = False
first_run = True
user_giving_data = True
show_leaderboard = False
play_again = False
incorrect_nickname_flag = False

# Bosses
star_lord_arrived = False
bounty_hunter_arrived = False
ghast_of_the_void_arrived = False
galactic_devourer_arrived = False
first_stardust = False
second_stardust = False
third_stardust = False

# Player
players = pygame.sprite.Group()

# Guns
guns = pygame.sprite.Group()

# Enemies
enemies = pygame.sprite.Group()
enemies_laser_guns = pygame.sprite.Group()

# Bonuses
bonuses = pygame.sprite.Group()

