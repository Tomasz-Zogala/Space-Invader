import pygame

from Enemies_package.asteroid import Asteroid
from Enemies_package.bounty_hunter import Bounty_hunter
from Enemies_package.galactic_devourer import Galactic_devourer
from Enemies_package.ghast_of_the_void import Ghast_of_the_void
from Enemies_package.star_lord import Star_lord
from Consts_package.consts import players, guns, bonuses, enemies, enemies_laser_guns, SCREEN_WIDTH, SCREEN_HEIGHT, \
    game_over, gameplay_state, first_run, star_lord_arrived, bounty_hunter_arrived, ghast_of_the_void_arrived, \
    galactic_devourer_arrived, fullscreen, user_giving_data
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
play_again_mR = play_again_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))

welcome_m = font.render('WELCOME TO SPACE X CALIBUR', False, '#E7CFCF')
welcome_mR = welcome_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))

to_play_m = font.render('Press SPACE to play!', False, '#E7CFCF')
to_play_mR = to_play_m.get_rect(center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT * 3 / 4)))

enter_nickname_m = font.render('Enter your nickname:', False, '#E7CFCF')
enter_nickname_mR = enter_nickname_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))

# Boss announcements
warning_m = font.render('!!! WARNING WARNING WARNING !!!', False, '#E7CFCF')
warning_mR = warning_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))

star_lord_announcement_m = font.render('Star lord has detected our presence in space', False, '#E7CFCF')
star_lord_announcement_mR = star_lord_announcement_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 12))

bounty_hunter_announcement_m = font.render('Bounty hunter?\'s engines make the air vibrate', False, '#E7CFCF')
bounty_hunter_announcement_mR = bounty_hunter_announcement_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 12))

ghast_of_the_void_announcement_m = font.render('The swarm queen is seen on the radar', False, '#E7CFCF')
ghast_of_the_void_announcement_mR = ghast_of_the_void_announcement_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 12))

galactic_devourer_announcement_m = font.render('Unexplained anomaly ahead', False, '#E7CFCF')
galactic_devourer_announcement_mR = galactic_devourer_announcement_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 12))
galactic_devourer_announcement_m2 = font.render('WHAT IS IT???', False, '#E7CFCF')
galactic_devourer_announcement_mR2 = galactic_devourer_announcement_m2.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 8))


# Display score
def display_score(score, pos_x, pos_y, color):
    score_surf = font.render(f'SCORE: {score}', False, color)
    score_rect = score_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(score_surf, score_rect)

# Display gun type
def display_timer(timer, pos_x, pos_y, color):
    timer_surf = font.render(f'TIME: {round(timer/60, 1)}', False, color)
    timer_rect = timer_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(timer_surf, timer_rect)

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


# Display user input nickname
def display_user_input_nickname(nickname, pos_x, pos_y, color):
    nickname_surf = font.render(f' {nickname}', False, color)
    nickname_rect = nickname_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(nickname_surf, nickname_rect)


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


user_nickname = ''
player_score_map = {}
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_over = True
        if not gameplay_state:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and first_run:
                # Reset
                guns.empty()
                enemies.empty()
                enemies_laser_guns.empty()
                bonuses.empty()

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

                gameplay_state = True
                first_run = False
            if not first_run:
                if user_giving_data:
                    if event.type == pygame.KEYDOWN and event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN:
                        user_nickname += event.unicode
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                        user_nickname = user_nickname[:-1]
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and user_nickname:
                        user_giving_data = False
                if not user_giving_data:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                        player_score_map = {user_nickname: player.score}

                        with open("Leader_board.txt", "a") as f:
                            for key, value in player_score_map.items():
                                f.write(key + ":" + str(value) + "\n")

                        #####################################
                        guns.empty()
                        enemies.empty()
                        enemies_laser_guns.empty()
                        bonuses.empty()

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
                        #######################
                        user_giving_data = True
                        gameplay_state = True
                        user_nickname = ''
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
        display_timer(game_boss_timer, SCREEN_WIDTH / 2, 150, '#E7CFCF')
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
            gameplay_state = False

        # Game script
        if 1200 <= game_boss_timer <= 1800:
            screen.blit(warning_m, warning_mR)
            screen.blit(star_lord_announcement_m, star_lord_announcement_mR)

        if game_boss_timer >= 1800 and not star_lord_arrived:
            star_lord_arrived = True
            star_lord = Star_lord()
            enemies.add(star_lord)

        if 3000 <= game_boss_timer <= 3600:
            screen.blit(warning_m, warning_mR)
            screen.blit(bounty_hunter_announcement_m, bounty_hunter_announcement_mR)

        if game_boss_timer >= 3600 and not bounty_hunter_arrived:
            bounty_hunter_arrived = True
            bounty_hunter = Bounty_hunter()
            enemies.add(bounty_hunter)

        if 4800 <= game_boss_timer <= 5400:
            screen.blit(warning_m, warning_mR)
            screen.blit(ghast_of_the_void_announcement_m, ghast_of_the_void_announcement_mR)

        if game_boss_timer >= 5400 and not ghast_of_the_void_arrived:
            ghast_of_the_void_arrived = True
            ghast_of_the_void = Ghast_of_the_void(SCREEN_HEIGHT / 16, SCREEN_HEIGHT / 16, 1, True)
            enemies.add(ghast_of_the_void)

        if 6600 <= game_boss_timer <= 7200:
            screen.blit(warning_m, warning_mR)
            screen.blit(galactic_devourer_announcement_m, galactic_devourer_announcement_mR)
            screen.blit(galactic_devourer_announcement_m2, galactic_devourer_announcement_mR2)

        if game_boss_timer >= 7200 and not galactic_devourer_arrived:
            galactic_devourer_arrived = True
            galactic_devourer = Galactic_devourer()
            enemies.add(galactic_devourer)
    else:
        if first_run:
            screen.blit(background_graphics, screen_background_position)
            screen.blit(welcome_m, welcome_mR)
            screen.blit(to_play_m, to_play_mR)
        else:
            if user_giving_data:
                screen.blit(background_graphics, screen_background_position)
                screen.blit(enter_nickname_m, enter_nickname_mR)
                display_score(player.score, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100, '#E7CFCF')
                display_user_input_nickname(user_nickname, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 10,
                                            '#E7CFCF')
            else:
                screen.blit(background_graphics, screen_background_position)
                screen.blit(play_again_m, play_again_mR)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
