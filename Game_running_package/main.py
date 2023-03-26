import pygame
import re

from Player_package.player import Player
from Enemies_package.asteroid import Asteroid
from Enemies_package.stardust import Stardust
from Enemies_package.star_lord import Star_lord
from Enemies_package.bounty_hunter import Bounty_hunter
from Enemies_package.ghast_of_the_void import Ghast_of_the_void
from Enemies_package.galactic_devourer import Galactic_devourer

from Constants_package.constants import players, enemies, guns, bonuses, enemies_laser_guns, SCREEN_WIDTH, \
    SCREEN_HEIGHT, \
    game_over_flag, game_running_flag, game_first_run_flag, fullscreen_flag, user_enters_nickname_flag, \
    incorrect_nickname_flag, \
    star_lord_arrived_flag, bounty_hunter_arrived_flag, ghast_of_the_void_arrived_flag, galactic_devourer_arrived_flag, \
    first_stardust_wave_flag, second_stardust_wave_flag, third_stardust_wave_flag, fourth_stardust_wave_flag, SECOND, \
    boss_rush_arrived_flag3, boss_rush_arrived_flag2, boss_rush_arrived_flag1

pygame.init()

# Game clock
clock = pygame.time.Clock()
game_score_timer = 0
game_boss_timer = 0

# Screen
pygame.display.set_caption('Nebula Crusaders')
if fullscreen_flag:
    screen_background_position = (-120, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    background_graphics = pygame.image.load('Additional_resources/Graphics/Background_wallpaper.png').convert()
else:
    screen_background_position = (0, 0)
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    background_graphics = pygame.image.load('Additional_resources/Graphics/Background_wallpaper2.png').convert()
pygame.mouse.set_visible(False)

# Game Audio
background_audio = pygame.mixer.Sound("Additional_resources/Audio/main_theme.mp3")
background_audio.play(loops=-1)
background_audio.set_volume(0.2)

# Fonts
font_125 = pygame.font.Font('Additional_resources/Font/Pixel_font.ttf', 125)
font_100 = pygame.font.Font('Additional_resources/Font/Pixel_font.ttf', 100)
font_75 = pygame.font.Font('Additional_resources/Font/Pixel_font.ttf', 75)
font_60 = pygame.font.Font('Additional_resources/Font/Pixel_font.ttf', 60)
font_50 = pygame.font.Font('Additional_resources/Font/Pixel_font.ttf', 50)
font_40 = pygame.font.Font('Additional_resources/Font/Pixel_font.ttf', 40)
font_35 = pygame.font.Font('Additional_resources/Font/Pixel_font.ttf', 35)
font_30 = pygame.font.Font('Additional_resources/Font/Pixel_font.ttf', 30)
font_25 = pygame.font.Font('Additional_resources/Font/Pixel_font.ttf', 25)

# Game messages (Fullscreen)
welcome_m = font_125.render('Welcome to', False, '#FCFCF4')
welcome_mR = welcome_m.get_rect(center=(SCREEN_WIDTH / 2, 200))

nebula_m = font_125.render('Nebula Crusaders', False, '#FCFCF4')
nebula_mR = nebula_m.get_rect(center=(SCREEN_WIDTH / 2, 300))

controls_m = font_125.render('CONTROLS:', False, '#FCFCF4')
controls_mR = controls_m.get_rect(center=(SCREEN_WIDTH / 2, 650))

controls_m1 = font_75.render('Movement:', False, '#FCFCF4')
controls_mR1 = controls_m1.get_rect(center=(700, 750))

controls_m1C = font_75.render('< ↑ > ↓', False, '#FCFCF4')
controls_mR1C = controls_m1C.get_rect(center=(700, 850))

controls_m2 = font_75.render('Switching guns:', False, '#FCFCF4')
controls_mR2 = controls_m2.get_rect(center=(SCREEN_WIDTH / 2, 750))

controls_m2C = font_75.render('1 2 3 4 5 6', False, '#FCFCF4')
controls_mR2C = controls_m2C.get_rect(center=(SCREEN_WIDTH / 2, 850))

controls_m3 = font_75.render('Shooting:', False, '#FCFCF4')
controls_mR3 = controls_m3.get_rect(center=(1860, 750))

controls_m3C = font_75.render('SPACE', False, '#FCFCF4')
controls_mR3C = controls_m3C.get_rect(center=(1860, 850))

to_play_m = font_125.render('Press SPACE to play!', False, '#FCFCF4')
to_play_mR = to_play_m.get_rect(center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT * 3 / 4)))

to_leave_m = font_50.render('Press ESC to leave game at any time', False, '#FCFCF4')
to_leave_mR = to_leave_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100))

play_again_m = font_125.render('Press SPACE to play again!', False, '#FCFCF4')
play_again_mR = play_again_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))

to_play_leaderboard_m = font_125.render('Press SPACE to play!', False, '#FCFCF4')
to_play_leaderboard_mR = to_play_leaderboard_m.get_rect(center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT - 150)))

enter_nickname_m = font_125.render('Enter your nickname:', False, '#FCFCF4')
enter_nickname_mR = enter_nickname_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))

leaderboard_m = font_125.render('Leaderboard:', False, '#FCFCF4')
leaderboard_mR = leaderboard_m.get_rect(center=(SCREEN_WIDTH / 2, 100))

incorrect_nickname = font_125.render('INCORRECT NICKNAME', False, '#FF0000')
incorrect_nicknameR = incorrect_nickname.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 4))

# Game messages (Windowed)
welcome_mW = font_50.render('Welcome to', False, '#FCFCF4')
welcome_mRW = welcome_m.get_rect(center=(870, 150))

nebula_mW = font_50.render('Nebula Crusaders', False, '#FCFCF4')
nebula_mRW = nebula_m.get_rect(center=(1000, 200))

controls_mW = font_50.render('CONTROLS:', False, '#FCFCF4')
controls_mRW = controls_m.get_rect(center=(850, 375))

controls_m1W = font_30.render('Movement:', False, '#FCFCF4')
controls_mR1W = controls_m1.get_rect(center=(530, 425))

controls_m1CW = font_30.render('< ↑ > ↓', False, '#FCFCF4')
controls_mR1CW = controls_m1C.get_rect(center=(500, 475))

controls_m2W = font_30.render('Switching guns:', False, '#FCFCF4')
controls_mR2W = controls_m2.get_rect(center=(830, 425))

controls_m2CW = font_30.render('1 2 3 4 5 6', False, '#FCFCF4')
controls_mR2CW = controls_m2C.get_rect(center=(775, 475))

controls_m3W = font_30.render('Shooting:', False, '#FCFCF4')
controls_mR3W = controls_m3.get_rect(center=(985, 425))

controls_m3CW = font_30.render('SPACE', False, '#FCFCF4')
controls_mR3CW = controls_m3C.get_rect(center=(930, 475))

to_play_mW = font_50.render('Press SPACE to play!', False, '#FCFCF4')
to_play_mRW = to_play_m.get_rect(center=(1100, 600))

to_leave_mW = font_40.render('Press ESC to leave game at any time', False, '#FCFCF4')
to_leave_mRW = to_leave_m.get_rect(center=(750, 700))

to_play_leaderboard_mW = font_60.render('Press SPACE to play!', False, '#FCFCF4')
to_play_leaderboard_mRW = to_play_leaderboard_m.get_rect(center=(1000, 700))

enter_nickname_mW = font_60.render('Enter your nickname:', False, '#FCFCF4')
enter_nickname_mRW = enter_nickname_m.get_rect(center=(1025, 230))

leaderboard_mW = font_60.render('Leaderboard:', False, '#FCFCF4')
leaderboard_mRW = leaderboard_m.get_rect(center=(855, 100))

incorrect_nicknameW = font_60.render('INCORRECT NICKNAME', False, '#FF0000')
incorrect_nicknameRW = incorrect_nickname.get_rect(center=(975, 700))

# Boss announcements (Fullscreen)
warning_m = font_125.render('!!! WARNING WARNING WARNING !!!', False, '#FCFCF4')
warning_mR = warning_m.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
star_lord_announcement_m = font_75.render('Star lord has detected our presence in space', False, '#FCFCF4')
star_lord_announcement_mR = star_lord_announcement_m.get_rect(
    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 12))
bounty_hunter_announcement_m = font_75.render('Bounty hunter?\'s engines make the air vibrate', False, '#FCFCF4')
bounty_hunter_announcement_mR = bounty_hunter_announcement_m.get_rect(
    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 12))
ghast_of_the_void_announcement_m = font_75.render('The swarm queen is seen on the radar', False, '#FCFCF4')
ghast_of_the_void_announcement_mR = ghast_of_the_void_announcement_m.get_rect(
    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 12))
galactic_devourer_announcement_m = font_75.render('Unexplained anomaly ahead', False, '#FCFCF4')
galactic_devourer_announcement_mR = galactic_devourer_announcement_m.get_rect(
    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 12))
galactic_devourer_announcement_m2 = font_125.render('WHAT IS IT???', False, '#FCFCF4')
galactic_devourer_announcement_mR2 = galactic_devourer_announcement_m2.get_rect(
    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 6))
boss_rush_announcement_m = font_125.render('THATS BOSS RUSH', False, '#FCFCF4')
boss_rush_announcement_mR = boss_rush_announcement_m.get_rect(
    center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 12))

# Boss announcements (Windowed)
warning_mW = font_60.render('!!! WARNING WARNING WARNING !!!', False, '#FCFCF4')
warning_mRW = warning_m.get_rect(center=(1220, 175))
star_lord_announcement_mW = font_30.render('Star lord has detected our presence in space', False, '#FCFCF4')
star_lord_announcement_mRW = star_lord_announcement_m.get_rect(center=(1200, 225))
bounty_hunter_announcement_mW = font_30.render('Bounty hunter?\'s engines make the air vibrate', False, '#FCFCF4')
bounty_hunter_announcement_mRW = bounty_hunter_announcement_m.get_rect(center=(1215, 225))
ghast_of_the_void_announcement_mW = font_30.render('The swarm queen is seen on the radar', False, '#FCFCF4')
ghast_of_the_void_announcement_mRW = ghast_of_the_void_announcement_m.get_rect(center=(1100, 225))
galactic_devourer_announcement_mW = font_30.render('Unexplained anomaly ahead', False, '#FCFCF4')
galactic_devourer_announcement_mRW = galactic_devourer_announcement_m.get_rect(center=(950, 225))
galactic_devourer_announcement_m2W = font_60.render('WHAT IS IT???', False, '#FCFCF4')
galactic_devourer_announcement_mR2W = galactic_devourer_announcement_m2.get_rect(center=(875, 315))
boss_rush_announcement_mW = font_60.render('THATS BOSS RUSH', False, '#FCFCF4')
boss_rush_announcement_mRW = boss_rush_announcement_m.get_rect(center=(1200, 225))


# Display score (Fullscreen)
def display_score(score, pos_x, pos_y, color):
    score_surf = font_100.render(f'SCORE:{score}', False, color)
    score_rect = score_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(score_surf, score_rect)


# Display score (Windowed)
def display_scoreW(score, pos_x, pos_y, color):
    score_surf = font_50.render(f'SCORE:{score}', False, color)
    score_rect = score_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(score_surf, score_rect)


# Display gun type (Fullscreen)
def display_timer(timer, pos_x, pos_y, color):
    timer_surf = font_75.render(f'TIME:{round(timer / 60, 1)}', False, color)
    timer_rect = timer_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(timer_surf, timer_rect)


# Display gun type (Windowed)
def display_timerW(timer, pos_x, pos_y, color):
    timer_surf = font_35.render(f'TIME:{round(timer / 60, 1)}', False, color)
    timer_rect = timer_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(timer_surf, timer_rect)


# Display HP (Fullscreen)
def display_hp(hp, pos_x, pos_y, color):
    hp_surf = font_100.render(f'HP:{round(hp, 2)}', False, color)
    hp_rect = hp_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(hp_surf, hp_rect)


# Display HP (Windowed)
def display_hpW(hp, pos_x, pos_y, color):
    hp_surf = font_50.render(f'HP:{round(hp, 2)}', False, color)
    hp_rect = hp_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(hp_surf, hp_rect)


# Display Stats (Fullscreen)
def display_stats(speed, damage, fire_rate, pos_x, pos_y, color):
    damage_surf = font_60.render(f'DMG:{round(damage, 2)}', False, color)
    damage_rect = damage_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(damage_surf, damage_rect)

    fire_rate_surf = font_60.render(f'FIRE RATE:{round(1 / fire_rate, 2)}', False, color)
    fire_rate_rect = fire_rate_surf.get_rect(center=(pos_x, pos_y + 65))
    screen.blit(fire_rate_surf, fire_rate_rect)

    speed_surf = font_60.render(f'SPEED:{round(speed, 2)}', False, color)
    speed_rect = speed_surf.get_rect(center=(pos_x, pos_y + 130))
    screen.blit(speed_surf, speed_rect)


# Display Stats (Windowed)
def display_statsW(speed, damage, fire_rate, pos_x, pos_y, color):
    damage_surf = font_25.render(f'DMG:{round(damage, 2)}', False, color)
    damage_rect = damage_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(damage_surf, damage_rect)

    fire_rate_surf = font_25.render(f'FIRE RATE:{round(1 / fire_rate, 2)}', False, color)
    fire_rate_rect = fire_rate_surf.get_rect(center=(pos_x, pos_y + 28))
    screen.blit(fire_rate_surf, fire_rate_rect)

    speed_surf = font_25.render(f'SPEED:{round(speed, 2)}', False, color)
    speed_rect = speed_surf.get_rect(center=(pos_x, pos_y + 56))
    screen.blit(speed_surf, speed_rect)


# Display gun type (Fullscreen)
def display_gun(gun_type, pos_x, pos_y, color):
    gun_surf = font_50.render(f'GUN:{gun_type}', False, color)
    gun_rect = gun_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(gun_surf, gun_rect)


# Display gun type (Windowed)
def display_gunW(gun_type, pos_x, pos_y, color):
    gun_surf = font_25.render(f'GUN:{gun_type}', False, color)
    gun_rect = gun_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(gun_surf, gun_rect)


# Display user input nickname (Fullscreen)
def display_user_input_nickname(nickname, pos_x, pos_y, color):
    nickname_surf = font_100.render(f'{nickname}', False, color)
    nickname_rect = nickname_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(nickname_surf, nickname_rect)


# Display user input nickname (Windowed)
def display_user_input_nicknameW(nickname, pos_x, pos_y, color):
    nickname_surf = font_50.render(f'{nickname}', False, color)
    nickname_rect = nickname_surf.get_rect(center=(pos_x, pos_y))
    screen.blit(nickname_surf, nickname_rect)


# Display score (Fullscreen)
def display_leader_board(pos_x, pos_y, color):
    with open("Leaderboard.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                key, value = line.split(":")
                player_score_map_output[key] = int(value)

    sorted_player_score_map_output = {k: v for k, v in
                                      sorted(player_score_map_output.items(), key=lambda item: item[1], reverse=True)}

    for i, (key, value) in enumerate(sorted_player_score_map_output.items()):
        if i < 9:
            text = f"{i + 1}.  {key} {value}"
            text_surface = font_75.render(text, True, color)
            screen.blit(text_surface, (pos_x, i * 100 + pos_y))
        else:
            text = f"{i + 1}. {key} {value}"
            text_surface = font_75.render(text, True, color)
            screen.blit(text_surface, (pos_x, i * 100 + pos_y))
        if i == 9:
            break


# Display score (Windowed)
def display_leader_boardW(pos_x, pos_y, color):
    with open("Leaderboard.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                key, value = line.split(":")
                player_score_map_output[key] = int(value)

    sorted_player_score_map_output = {k: v for k, v in
                                      sorted(player_score_map_output.items(), key=lambda item: item[1], reverse=True)}

    for i, (key, value) in enumerate(sorted_player_score_map_output.items()):
        if i < 9:
            text = f"{i + 1}.  {key} {value}"
            text_surface = font_35.render(text, True, color)
            screen.blit(text_surface, (pos_x, i * 45 + pos_y))
        else:
            text = f"{i + 1}. {key} {value}"
            text_surface = font_35.render(text, True, color)
            screen.blit(text_surface, (pos_x, i * 45 + pos_y))
        if i == 9:
            break


# Graphical availability of guns (Fullscreen)
def display_gun_availability(gun_1, gun_2, gun_3, gun_4, gun_5, gun_6):
    gun_1_image = pygame.Surface([30, 30])
    if gun_1:
        gun_1_image.fill('#60a05b')
    else:
        gun_1_image.fill('#e40b00')
    gun_1_image_rect = gun_1_image.get_rect()
    gun_1_image_rect.x = SCREEN_WIDTH / 2 - 100
    gun_1_image_rect.y = SCREEN_HEIGHT - 40
    screen.blit(gun_1_image, gun_1_image_rect)

    gun_2_image = pygame.Surface([30, 30])
    if gun_2:
        gun_2_image.fill('#60a05b')
    else:
        gun_2_image.fill('#e40b00')
    gun_2_image_rect = gun_2_image.get_rect()
    gun_2_image_rect.x = SCREEN_WIDTH / 2 - 60
    gun_2_image_rect.y = SCREEN_HEIGHT - 40
    screen.blit(gun_2_image, gun_2_image_rect)

    gun_3_image = pygame.Surface([30, 30])
    if gun_3:
        gun_3_image.fill('#60a05b')
    else:
        gun_3_image.fill('#e40b00')
    gun_3_image_rect = gun_3_image.get_rect()
    gun_3_image_rect.x = SCREEN_WIDTH / 2 - 20
    gun_3_image_rect.y = SCREEN_HEIGHT - 40
    screen.blit(gun_3_image, gun_3_image_rect)

    gun_4_image = pygame.Surface([30, 30])
    if gun_4:
        gun_4_image.fill('#60a05b')
    else:
        gun_4_image.fill('#e40b00')
    gun_4_image_rect = gun_4_image.get_rect()
    gun_4_image_rect.x = SCREEN_WIDTH / 2 + 20
    gun_4_image_rect.y = SCREEN_HEIGHT - 40
    screen.blit(gun_4_image, gun_4_image_rect)

    gun_5_image = pygame.Surface([30, 30])
    if gun_5:
        gun_5_image.fill('#60a05b')
    else:
        gun_5_image.fill('#e40b00')
    gun_5_image_rect = gun_5_image.get_rect()
    gun_5_image_rect.x = SCREEN_WIDTH / 2 + 60
    gun_5_image_rect.y = SCREEN_HEIGHT - 40
    screen.blit(gun_5_image, gun_5_image_rect)

    gun_6_image = pygame.Surface([30, 30])
    if gun_6:
        gun_6_image.fill('#60a05b')
    else:
        gun_6_image.fill('#e40b00')
    gun_6_image_rect = gun_6_image.get_rect()
    gun_6_image_rect.x = SCREEN_WIDTH / 2 + 100
    gun_6_image_rect.y = SCREEN_HEIGHT - 40
    screen.blit(gun_6_image, gun_6_image_rect)


# Graphical availability of guns (Windowed)
def display_gun_availabilityW(gun_1, gun_2, gun_3, gun_4, gun_5, gun_6):
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


def reset_game():
    guns.empty()
    enemies.empty()
    enemies_laser_guns.empty()
    bonuses.empty()
    players.empty()

    for i in range(7):
        asteroid = Asteroid()
        enemies.add(asteroid)


player_nickname = ''
player_score_map_input = {}
player_score_map_output = {}

while not game_over_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_flag = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_over_flag = True

        if not game_running_flag:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_first_run_flag:
                reset_game()

                player = Player()
                players.add(player)

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

                game_score_timer = 0
                game_boss_timer = 0

                game_running_flag = True
                game_first_run_flag = False
            else:
                if user_enters_nickname_flag:
                    if event.type == pygame.KEYDOWN and event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN and event.key != pygame.K_SPACE:
                        player_nickname += event.unicode
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                        player_nickname = player_nickname[:-1]
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

                        nickname_pattern = re.compile(r'^[a-zA-Z0-9]{1,12}$')

                        if nickname_pattern.match(player_nickname):
                            player_score_map_input = {player_nickname: player.score}

                            with open("Leaderboard.txt", "a") as f:
                                for key, value in player_score_map_input.items():
                                    f.write(key + ":" + str(value) + "\n")

                            player_score_map_input.clear()
                            player_nickname = ''
                            user_enters_nickname_flag = False
                            incorrect_nickname_flag = False
                        else:
                            player_nickname = ''
                            incorrect_nickname_flag = True
                else:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        reset_game()

                        player = Player()
                        players.add(player)

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

                        game_score_timer = 0
                        game_boss_timer = 0

                        user_enters_nickname_flag = True
                        game_running_flag = True
    if game_running_flag:
        # Background
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

        if fullscreen_flag:
            display_score(player.score, SCREEN_WIDTH / 2, 75, '#FCFCF4')
            display_timer(game_boss_timer, SCREEN_WIDTH / 2, 170, '#FCFCF4')
            display_hp(player.hp, SCREEN_WIDTH - 180, SCREEN_HEIGHT - 60, '#FCFCF4')
            display_stats(player.speed, player.gun_damage_multiplier, player.gun_fire_rate_multiplier, 275,
                          SCREEN_HEIGHT - 180, '#FCFCF4')
            display_gun(player.using_gun_type, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 70, '#FCFCF4')
            display_gun_availability(player.minigun, player.laser_rifle, player.rocket_launcher, player.laser_ring,
                                     player.sniper_rifle, player.laser_thrower)
        else:
            display_scoreW(player.score, 640, 30, '#FCFCF4')
            display_timerW(game_boss_timer, 640, 70, '#FCFCF4')
            display_hpW(player.hp, 1155, 765, '#FCFCF4')
            display_statsW(player.speed, player.gun_damage_multiplier, player.gun_fire_rate_multiplier, 110, 720,
                           '#FCFCF4')
            display_gunW(player.using_gun_type, 640, 765, '#FCFCF4')
            display_gun_availabilityW(player.minigun, player.laser_rifle, player.rocket_launcher, player.laser_ring,
                                      player.sniper_rifle, player.laser_thrower)

        # Timers
        game_score_timer += 1
        game_boss_timer += 1

        # Score update
        if game_score_timer >= 100 and player.score > 0:
            player.score += -5
            game_score_timer = 0

        # is Player alive
        if not players:
            game_running_flag = False

        # Game script
        if 40 * SECOND <= game_boss_timer <= 45 * SECOND:
            if fullscreen_flag:
                screen.blit(warning_m, warning_mR)
                screen.blit(star_lord_announcement_m, star_lord_announcement_mR)
            else:
                screen.blit(warning_mW, warning_mRW)
                screen.blit(star_lord_announcement_mW, star_lord_announcement_mRW)

        if game_boss_timer >= 45 * SECOND and not star_lord_arrived_flag:
            star_lord_arrived_flag = True
            star_lord = Star_lord()
            enemies.add(star_lord)

        if game_boss_timer >= 80 * SECOND and not first_stardust_wave_flag:
            for i in range(150):
                stardust = Stardust()
                enemies.add(stardust)
            first_stardust_wave_flag = True

        if 85 * SECOND <= game_boss_timer <= 90 * SECOND:
            if fullscreen_flag:
                screen.blit(warning_m, warning_mR)
                screen.blit(bounty_hunter_announcement_m, bounty_hunter_announcement_mR)
            else:
                screen.blit(warning_mW, warning_mRW)
                screen.blit(bounty_hunter_announcement_mW, bounty_hunter_announcement_mRW)

        if game_boss_timer >= 90 * SECOND and not bounty_hunter_arrived_flag:
            bounty_hunter_arrived_flag = True
            bounty_hunter = Bounty_hunter()
            enemies.add(bounty_hunter)

        if game_boss_timer >= 125 * SECOND and not second_stardust_wave_flag:
            for i in range(200):
                stardust = Stardust()
                enemies.add(stardust)
            second_stardust_wave_flag = True

        if 130 * SECOND <= game_boss_timer <= 135 * SECOND:
            if fullscreen_flag:
                screen.blit(warning_m, warning_mR)
                screen.blit(ghast_of_the_void_announcement_m, ghast_of_the_void_announcement_mR)
            else:
                screen.blit(warning_mW, warning_mRW)
                screen.blit(ghast_of_the_void_announcement_mW, ghast_of_the_void_announcement_mRW)

        if game_boss_timer >= 135 * SECOND and not ghast_of_the_void_arrived_flag:
            ghast_of_the_void_arrived_flag = True
            ghast_of_the_void = Ghast_of_the_void(SCREEN_HEIGHT / 16, SCREEN_HEIGHT / 16, 1, True)
            enemies.add(ghast_of_the_void)

        if game_boss_timer >= 170 * SECOND and not third_stardust_wave_flag:
            for i in range(250):
                stardust = Stardust()
                enemies.add(stardust)
            third_stardust_wave_flag = True

        if 175 * SECOND <= game_boss_timer <= 180 * SECOND:
            if fullscreen_flag:
                screen.blit(warning_m, warning_mR)
                screen.blit(galactic_devourer_announcement_m, galactic_devourer_announcement_mR)
                screen.blit(galactic_devourer_announcement_m2, galactic_devourer_announcement_mR2)
            else:
                screen.blit(warning_mW, warning_mRW)
                screen.blit(galactic_devourer_announcement_mW, galactic_devourer_announcement_mRW)
                screen.blit(galactic_devourer_announcement_m2W, galactic_devourer_announcement_mR2W)

        if game_boss_timer >= 180 * SECOND and not galactic_devourer_arrived_flag:
            galactic_devourer_arrived_flag = True
            galactic_devourer = Galactic_devourer()
            enemies.add(galactic_devourer)

        if game_boss_timer >= 215 * SECOND and not fourth_stardust_wave_flag:
            for i in range(300):
                stardust = Stardust()
                enemies.add(stardust)
            fourth_stardust_wave_flag = True

        if 220 * SECOND <= game_boss_timer <= 225 * SECOND:
            if fullscreen_flag:
                screen.blit(warning_m, warning_mR)
                screen.blit(boss_rush_announcement_m, boss_rush_announcement_mR)
            else:
                screen.blit(warning_mW, warning_mRW)
                screen.blit(boss_rush_announcement_mW, boss_rush_announcement_mRW)

        if game_boss_timer >= 225 * SECOND and not boss_rush_arrived_flag1:
            boss_rush_arrived_flag = True
            star_lord1 = Star_lord()
            enemies.add(star_lord1)
            bounty_hunter1 = Bounty_hunter()
            enemies.add(bounty_hunter1)
            ghast_of_the_void1 = Ghast_of_the_void()
            enemies.add(ghast_of_the_void1)
            galactic_devourer1 = Galactic_devourer()
            enemies.add(galactic_devourer1)

        if 165 * SECOND <= game_boss_timer <= 270 * SECOND:
            if fullscreen_flag:
                screen.blit(warning_m, warning_mR)
                screen.blit(boss_rush_announcement_m, boss_rush_announcement_mR)
            else:
                screen.blit(warning_mW, warning_mRW)
                screen.blit(boss_rush_announcement_mW, boss_rush_announcement_mRW)

        if game_boss_timer >= 270 * SECOND and not boss_rush_arrived_flag2:
            boss_rush_arrived_flag = True
            star_lord2 = Star_lord()
            enemies.add(star_lord2)
            bounty_hunter2 = Bounty_hunter()
            enemies.add(bounty_hunter2)
            ghast_of_the_void2 = Ghast_of_the_void()
            enemies.add(ghast_of_the_void2)
            galactic_devourer2 = Galactic_devourer()
            enemies.add(galactic_devourer2)

        if 310 * SECOND <= game_boss_timer <= 315 * SECOND:
            if fullscreen_flag:
                screen.blit(warning_m, warning_mR)
                screen.blit(boss_rush_announcement_m, boss_rush_announcement_mR)
            else:
                screen.blit(warning_mW, warning_mRW)
                screen.blit(boss_rush_announcement_mW, boss_rush_announcement_mRW)

        if game_boss_timer >= 315 * SECOND and not boss_rush_arrived_flag3:
            boss_rush_arrived_flag = True
            star_lord3 = Star_lord()
            enemies.add(star_lord3)
            bounty_hunter3 = Bounty_hunter()
            enemies.add(bounty_hunter3)
            ghast_of_the_void3 = Ghast_of_the_void()
            enemies.add(ghast_of_the_void3)
            galactic_devourer3 = Galactic_devourer()
            enemies.add(galactic_devourer3)

        if game_boss_timer >= 360 * SECOND:
            game_running_flag = False

    else:
        if game_first_run_flag:
            if fullscreen_flag:
                screen.blit(background_graphics, screen_background_position)
                screen.blit(welcome_m, welcome_mR)
                screen.blit(nebula_m, nebula_mR)
                screen.blit(controls_m, controls_mR)
                screen.blit(controls_m1, controls_mR1)
                screen.blit(controls_m1C, controls_mR1C)
                screen.blit(controls_m2, controls_mR2)
                screen.blit(controls_m2C, controls_mR2C)
                screen.blit(controls_m3, controls_mR3)
                screen.blit(controls_m3C, controls_mR3C)
                screen.blit(to_play_m, to_play_mR)
                screen.blit(to_leave_m, to_leave_mR)
            else:
                screen.blit(background_graphics, screen_background_position)
                screen.blit(welcome_mW, welcome_mRW)
                screen.blit(nebula_mW, nebula_mRW)
                screen.blit(controls_mW, controls_mRW)
                screen.blit(controls_m1W, controls_mR1W)
                screen.blit(controls_m1CW, controls_mR1CW)
                screen.blit(controls_m2W, controls_mR2W)
                screen.blit(controls_m2CW, controls_mR2CW)
                screen.blit(controls_m3W, controls_mR3W)
                screen.blit(controls_m3CW, controls_mR3CW)
                screen.blit(to_play_mW, to_play_mRW)
                screen.blit(to_leave_mW, to_leave_mRW)
        else:
            if user_enters_nickname_flag:
                if fullscreen_flag:
                    screen.blit(background_graphics, screen_background_position)
                    screen.blit(enter_nickname_m, enter_nickname_mR)
                    display_score(player.score, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 12, '#FCFCF4')
                    display_user_input_nickname(player_nickname, SCREEN_WIDTH / 2,
                                                SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 10, '#FCFCF4')
                    if incorrect_nickname_flag:
                        screen.blit(incorrect_nickname, incorrect_nicknameR)
                else:
                    screen.blit(background_graphics, screen_background_position)
                    screen.blit(enter_nickname_mW, enter_nickname_mRW)
                    display_scoreW(player.score, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 12, '#FCFCF4')
                    display_user_input_nicknameW(player_nickname, SCREEN_WIDTH / 2,
                                                 SCREEN_HEIGHT / 3 + SCREEN_HEIGHT / 10, '#FCFCF4')
                    if incorrect_nickname_flag:
                        screen.blit(incorrect_nicknameW, incorrect_nicknameRW)
            else:
                if fullscreen_flag:
                    screen.blit(background_graphics, screen_background_position)
                    screen.blit(leaderboard_m, leaderboard_mR)
                    display_leader_board(SCREEN_WIDTH / 2 - SCREEN_WIDTH / 5 + SCREEN_WIDTH / 30, 300, '#FCFCF4')
                    screen.blit(to_play_leaderboard_m, to_play_leaderboard_mR)
                else:
                    screen.blit(background_graphics, screen_background_position)
                    screen.blit(leaderboard_mW, leaderboard_mRW)
                    display_leader_boardW(SCREEN_WIDTH / 2 - SCREEN_WIDTH / 5 + SCREEN_WIDTH / 30, 135, '#FCFCF4')
                    screen.blit(to_play_leaderboard_mW, to_play_leaderboard_mRW)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
