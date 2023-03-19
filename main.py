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
pygame.display.set_caption('Space masters')
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Menu Audio
background_audio = pygame.mixer.Sound("Audio/Background_menu_v2.mp3")
background_audio.play(loops = -1)
background_audio.play()

# Hit Audio
hit_audio = pygame.mixer.Sound("Audio/Get_hit.mp3")

# Game messages
font = pygame.font.Font('Font/Pixel_font.ttf', 50)
game_message_menu = font.render('Press space to run', False, (0, 0, 0))
game_message_rect = game_message_menu.get_rect(center = (400, 330))

# Create the player sprite
player = Player()
players.add(player)

# Create some enemies and add them to the group
for i in range(4):
    enemy = Enemy(random.randrange(2, 4))
    enemies.add(enemy)

# Set the game's clock
clock = pygame.time.Clock()

# Start the game loop
game_over = False
game_active = True
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if game_active:
            print(".")
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                enemies.empty()
                for i in range(4):
                    enemy = Enemy(random.randrange(2, 4))
                    enemies.add(enemy)
                    player.kill()
                    player = Player()
                    players.add(player)
                game_active = True

    if game_active:
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
        collided_player = pygame.sprite.spritecollide(player, enemies, False)
        if collided_player:
            game_active = False

    else:
        screen.fill('#5334FF')
        screen.blit(game_message_menu, game_message_rect)
        screen.blit(player.image, player.rect)


    # Update the screen
    pygame.display.flip()
    # Delay to get 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
