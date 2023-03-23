import pygame

from Enemies_package.asteroid import Asteroid
from Enemies_package.bounty_hunter import Bounty_hunter
from Enemies_package.galactic_devourer import Galactic_devourer
from Enemies_package.ghast_of_the_void import Ghast_of_the_void
from Enemies_package.star_lord import Star_lord
from Consts_package.consts import players, guns, bonuses, enemies, enemies_laser_guns, SCREEN_WIDTH, SCREEN_HEIGHT, \
    game_over, gameplay_state, first_run, star_lord_arrived, bounty_hunter_arrived, ghast_of_the_void_arrived, \
    galactic_devourer_arrived, fullscreen
from Player_package.player import Player

pygame.init()

# Game clock
clock = pygame.time.Clock()
game_score_timer = 0
game_boss_timer = 0

# Screen
pygame.display.set_caption('SPACE X CALIBUR')
if fullscreen:
    screen_background_position = (-120, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    background_graphics = pygame.image.load('Additional_resources/Graphics/Background_wallpaper.png').convert()
else:
    screen_background_position = (0, 0)
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    background_graphics = pygame.image.load('Additional_resources/Graphics/Background_wallpaper2.png').convert()
pygame.mouse.set_visible(False)

# Menu Audio
background_audio = pygame.mixer.Sound("Additional_resources/Audio/Second_main_menu.mp3")
background_audio.play(loops=-1)
background_audio.set_volume(0.2)
background_audio.play()

# Game messages
font = pygame.font.Font('Additional_resources/Font/Pixel_font.ttf', 50)
font_stats = pygame.font.Font('Additional_resources/Font/Pixel_font.ttf', 25)

play_again_m = font.render('Press SPACE to play again!', False, '#E7CFCF')
play_again_mR = play_again_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))

welcome_m = font.render('WELCOME TO SPACE X CALIBUR', False, '#E7CFCF')
welcome_mR = welcome_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))

to_play_m = font.render('Press SPACE to play!', False, '#E7CFCF')
to_play_mR = to_play_m.get_rect(center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT * 3 / 4)))


# Display score
def display_score(score, pos_x, pos_y, color):
    score_surf = font.render(f'SCORE: {score}', False, color)
    score_rect = score_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(score_surf, score_rect)


# Display HP
def display_hp(hp, pos_x, pos_y, color):
    hp_surf = font.render(f'HP: {round(hp, 2)}', False, color)
    hp_rect = hp_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(hp_surf, hp_rect)


# Display Stats
def display_stats(speed, damage, fire_rate, pos_x, pos_y, color):
    damage_surf = font_stats.render(f'DMG: {round(damage, 2)}', False, color)
    damage_rect = damage_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(damage_surf, damage_rect)

    fire_rate_surf = font_stats.render(f'FIRE RATE: {round(1 / fire_rate, 2)}', False, color)
    fire_rate_rect = fire_rate_surf.get_rect(center=(pos_x, pos_y + 30))
    screen.blit(fire_rate_surf, fire_rate_rect)

    speed_surf = font_stats.render(f'SPEED: {round(speed, 2)}', False, color)
    speed_rect = speed_surf.get_rect(center=(pos_x, pos_y + 60))
    screen.blit(speed_surf, speed_rect)


# Display gun type
def display_gun(gun_type, pos_x, pos_y, color):
    gun_surf = font_stats.render(f'GUN: {gun_type}', False, color)
    gun_rect = gun_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(gun_surf, gun_rect)


def display_gun_availability(gun_1, gun_2, gun_3, gun_4, gun_5, gun_6):
    gun_1_image = pygame.Surface([15, 15])
    if gun_1:
        gun_1_image.fill('#60a05b')
    else:
        gun_1_image.fill('#e40b00')
    gun_1_image_rect = gun_1_image.get_rect()
    gun_1_image_rect.x = SCREEN_WIDTH / 2 - 50
    gun_1_image_rect.y = SCREEN_HEIGHT - 20
    screen.blit(gun_1_image, gun_1_image_rect)

    gun_2_image = pygame.Surface([15, 15])
    if gun_2:
        gun_2_image.fill('#60a05b')
    else:
        gun_2_image.fill('#e40b00')
    gun_2_image_rect = gun_2_image.get_rect()
    gun_2_image_rect.x = SCREEN_WIDTH / 2 - 30
    gun_2_image_rect.y = SCREEN_HEIGHT - 20
    screen.blit(gun_2_image, gun_2_image_rect)

    gun_3_image = pygame.Surface([15, 15])
    if gun_3:
        gun_3_image.fill('#60a05b')
    else:
        gun_3_image.fill('#e40b00')
    gun_3_image_rect = gun_3_image.get_rect()
    gun_3_image_rect.x = SCREEN_WIDTH / 2 - 10
    gun_3_image_rect.y = SCREEN_HEIGHT - 20
    screen.blit(gun_3_image, gun_3_image_rect)

    gun_4_image = pygame.Surface([15, 15])
    if gun_4:
        gun_4_image.fill('#60a05b')
    else:
        gun_4_image.fill('#e40b00')
    gun_4_image_rect = gun_4_image.get_rect()
    gun_4_image_rect.x = SCREEN_WIDTH / 2 + 10
    gun_4_image_rect.y = SCREEN_HEIGHT - 20
    screen.blit(gun_4_image, gun_4_image_rect)

    gun_5_image = pygame.Surface([15, 15])
    if gun_5:
        gun_5_image.fill('#60a05b')
    else:
        gun_5_image.fill('#e40b00')
    gun_5_image_rect = gun_5_image.get_rect()
    gun_5_image_rect.x = SCREEN_WIDTH / 2 + 30
    gun_5_image_rect.y = SCREEN_HEIGHT - 20
    screen.blit(gun_5_image, gun_5_image_rect)

    gun_6_image = pygame.Surface([15, 15])
    if gun_6:
        gun_6_image.fill('#60a05b')
    else:
        gun_6_image.fill('#e40b00')
    gun_6_image_rect = gun_6_image.get_rect()
    gun_6_image_rect.x = SCREEN_WIDTH / 2 + 50
    gun_6_image_rect.y = SCREEN_HEIGHT - 20
    screen.blit(gun_6_image, gun_6_image_rect)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_over = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not gameplay_state:

            # Reset
            guns.empty()
            enemies.empty()
            enemies_laser_guns.empty()
            bonuses.empty()

            gameplay_state = True
            star_lord_arrived = False
            bounty_hunter_arrived = False
            ghast_of_the_void_arrived = False
            galactic_devourer_arrived = False

            for i in range(2):
                asteroid = Asteroid()
                enemies.add(asteroid)

            if not players:
                player = Player()
                players.add(player)

            player.kill()
            player = Player()
            players.add(player)

            game_score_timer = 0
            game_boss_timer = 0

    if gameplay_state:
        screen.blit(background_graphics, screen_background_position)

        # Draw the sprites
        guns.draw(screen)
        players.draw(screen)
        enemies.draw(screen)
        enemies_laser_guns.draw(screen)
        bonuses.draw(screen)

        # Update the sprites
        guns.update()
        players.update()
        enemies.update()
        enemies_laser_guns.update()
        bonuses.update()

        display_score(player.score, SCREEN_WIDTH / 2, 50, '#E7CFCF')
        display_hp(player.hp, SCREEN_WIDTH - 110, SCREEN_HEIGHT - 50, '#E7CFCF')
        display_stats(player.speed, player.gun_damage_multiplier, player.gun_fire_rate_multiplier, 115, SCREEN_HEIGHT - 110, '#E7CFCF')
        display_gun(player.using_gun_type, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 40, '#E7CFCF')
        display_gun_availability(player.minigun, player.rocket_launcher, player.laser_thrower, player.laser_rifle, player.laser_ring, player.sniper_rifle)

        # Timers
        game_score_timer += 1
        game_boss_timer += 1

        # Score update
        if game_score_timer >= 100 and player.score > 0:
            player.score += -5
            game_score_timer = 0

        # is Player alive
        if not players:
            first_run = False
            gameplay_state = False

        # Game script
        if game_boss_timer >= 10000 and not star_lord_arrived:
            star_lord_arrived = True
            star_lord = Star_lord()
            enemies.add(star_lord)

        if game_boss_timer >= 10000 and not bounty_hunter_arrived:
            bounty_hunter_arrived = True
            bounty_hunter = Bounty_hunter()
            enemies.add(bounty_hunter)

        if game_boss_timer >= 10000 and not ghast_of_the_void_arrived:
            ghast_of_the_void_arrived = True
            ghast_of_the_void = Ghast_of_the_void(SCREEN_HEIGHT/16, SCREEN_HEIGHT/16, 1, True)
            enemies.add(ghast_of_the_void)

        if game_boss_timer >= 10000 and not galactic_devourer_arrived:
            galactic_devourer_arrived = True
            galactic_devourer = Galactic_devourer()
            enemies.add(galactic_devourer)
    else:
        if first_run:
            screen.blit(background_graphics, screen_background_position)
            screen.blit(welcome_m, welcome_mR)
            screen.blit(to_play_m, to_play_mR)

        else:
            screen.blit(background_graphics, screen_background_position)
            screen.blit(play_again_m, play_again_mR)
            display_score(player.score, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100, '#E7CFCF')

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
