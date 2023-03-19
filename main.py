import random

import pygame
from enemy import Enemy
from player import Player
from sprites import enemies, bullets, players, bonuses

# Set the dimensions of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create some enemies and add them to the group
for i in range(4):
    enemy = Enemy(random.randrange(2, 4))
    enemies.add(enemy)

# Create the player sprite
player = Player()
players.add(player)

# Set the game's clock
clock = pygame.time.Clock()

# Start the game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    screen.fill('#0E034E')

    # Draw the sprites
    players.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)
    bonuses.draw(screen)

    # Update the sprites
    players.update()
    enemies.update()
    bullets.update()
    bonuses.update()

    # Check for collisions between the player and enemies
    if pygame.sprite.spritecollide(player, enemies, True):
        game_over = True


    # Update the screen
    pygame.display.flip()

    # Delay to get 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
