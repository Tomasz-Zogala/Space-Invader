import pygame

from Enemies_package.asteroid import Asteroid
from Enemies_package.enemy import Enemy
from Sprites_package.sprites import players, asteroids, guns, bonuses
from Player_package.player import Player

pygame.init()

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
pygame.display.set_caption('SPACE X CALIBUR')
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.mouse.set_visible(False)

# Menu Audio
background_audio = pygame.mixer.Sound("Additional_resources/Audio/Background_menu_v2.mp3")
background_audio.play(loops=-1)
background_audio.set_volume(0.2)
background_audio.play()

# Game messages
font = pygame.font.Font('Additional_resources/Font/Pixel_font.ttf', 50)

play_again_m = font.render('Press SPACE to play again!', False, (0, 0, 0))
play_again_mR = play_again_m.get_rect(center=(400, 200))

welcome_m = font.render('WELCOME TO SPACE X CALIBUR', False, (0, 0, 0))
welcome_mR = welcome_m.get_rect(center=(400, 200))

to_play_m = font.render('Press SPACE to play!', False, (0, 0, 0))
to_play_mR = to_play_m.get_rect(center=(400, 600))

# Game setup
player = Player()
players.add(player)

for i in range(4):
    asteroid = Asteroid()
    asteroids.add(asteroid)

clock = pygame.time.Clock()
game_over = False
gameplay_state = False
first_run = True


# Display score
def display_score(score, pos_x, pos_y, color):
    score_surf = font.render(f'Score: {score}', False, color)
    score_rect = score_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(score_surf, score_rect)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_over = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not gameplay_state:
            guns.empty()
            asteroids.empty()
            bonuses.empty()

            for i in range(4):
                asteroid = Asteroid()
                asteroids.add(asteroid)

            player.kill()
            player = Player()
            players.add(player)
            gameplay_state = True

    if gameplay_state:
        screen.fill('#0E034E')
        display_score(player.score, 400, 50, '#E7CFCF')

        # Draw the sprites
        players.draw(screen)
        asteroids.draw(screen)
        guns.draw(screen)
        bonuses.draw(screen)

        # Update the sprites
        players.update()
        asteroids.update()
        guns.update()
        bonuses.update()

        # Check for collisions between the player and enemies
        collided_player = pygame.sprite.spritecollide(player, asteroids, False)
        if collided_player:
            first_run = False
            gameplay_state = False

    else:
        if first_run:
            screen.fill('#3C00AD')
            screen.blit(welcome_m, welcome_mR)
            screen.blit(to_play_m, to_play_mR)

        else:
            screen.fill('#3C00AD')
            screen.blit(play_again_m, play_again_mR)
            display_score(player.score, 400, 700, '#000000')

    # Update the screen
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
