import pygame

# Fullscreen flag
fullscreen_flag = True

# Time constant
SECOND = 60

# Screen
if fullscreen_flag:
    SCREEN_WIDTH = 2560
    SCREEN_HEIGHT = 1600
    SCALE = SCREEN_HEIGHT/800
else:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 800
    SCALE = SCREEN_HEIGHT/800

# Game flags
game_over_flag = False
game_running_flag = False
game_first_run_flag = True
user_enters_nickname_flag = True
showing_leaderboard_flag = False
incorrect_nickname_flag = False

# Bosses flags
star_lord_arrived_flag = False
bounty_hunter_arrived_flag = False
ghast_of_the_void_arrived_flag = False
galactic_devourer_arrived_flag = False
boss_rush_arrived_flag1 = False
boss_rush_arrived_flag2 = False
boss_rush_arrived_flag3 = False
first_stardust_wave_flag = False
second_stardust_wave_flag = False
third_stardust_wave_flag = False
fourth_stardust_wave_flag = False

# Players sprite group
players = pygame.sprite.Group()

# Guns sprite group
guns = pygame.sprite.Group()

# Enemies sprite group
enemies = pygame.sprite.Group()

# Enemies laser guns sprite group
enemies_laser_guns = pygame.sprite.Group()

# Bonuses sprite group
bonuses = pygame.sprite.Group()