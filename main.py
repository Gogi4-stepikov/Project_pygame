import random
import pygame
import sys


def draw_start_button(screen):
    st_txt = font.render("Начать игру", True, pygame.Color("Black"))
    st_bt = pygame.Rect(width // 2 - st_txt.get_width() // 2 - 20, height // 2 - st_txt.get_height() // 2 - 10, 200, 50)
    pygame.draw.rect(screen, pygame.Color("White"), st_bt)
    screen.blit(st_txt, (st_bt.x + 35, st_bt.y + 12))
    return st_bt

def draw_settings_button(screen):
    se_text = font.render("Настройки", True, pygame.Color("Black"))
    se_bt = pygame.Rect(10, 60, se_text.get_width() + 100, se_text.get_height() // 2 + 20)
    pygame.draw.rect(screen, pygame.Color("White"), se_bt)
    screen.blit(se_text, (se_bt.x + 50, se_bt.y + 5))
    return se_bt

def draw_return_button(screen):
    se_re_text = font.render("Вернуться", True, pygame.Color("Black"))
    se_re_bt = pygame.Rect(10, 60, se_re_text.get_width() + 100, se_re_text.get_height() // 2 + 20)
    pygame.draw.rect(screen, pygame.Color("White"), se_bt)
    screen.blit(se_re_text, (se_re_bt.x + 50, se_re_bt.y + 5))
    return se_re_bt

def draw_settings(screen):
    set_lbl = font.render("Настройки", True, pygame.Color("Black"))
    screen.blit(set_lbl, (width // 2 - set_lbl.get_width() // 2, height // 2 - set_lbl.get_height() // 2 - 500))

def draw_color_settings_button(screen):
    clr_text = font.render("Цвет", True, pygame.Color("Black"))
    color_settings_rect = pygame.Rect(width // 2 - clr_text.get_width() // 2 - 40, height // 2 - 120, 150, 40)
    pygame.draw.rect(screen, pygame.Color("White"), color_settings_rect)
    screen.blit(clr_text, (width // 2 - clr_text.get_width() // 2, height // 2 - clr_text.get_height() // 2 - 100))
    return color_settings_rect

def random_color_change():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def draw_music_settings_button(screen):
    msc_txt = font.render("Музыка", True, pygame.Color("Black"))
    music_settings_button_rect = pygame.Rect(width // 2 - msc_txt.get_width() // 2 - 220, height // 2 - 120, 150, 40)
    pygame.draw.rect(screen, pygame.Color("White"), music_settings_button_rect)
    screen.blit(msc_txt, (width // 2 - msc_txt.get_width() // 2 - 200, height // 2 - msc_txt.get_height() // 2 - 100))
    return music_settings_button_rect

def draw_character_settings_button(screen):
    chr_txt = font.render("Персонаж", True, pygame.Color("Black"))
    chr_rect = pygame.Rect(width // 2 - chr_txt.get_width() // 2 + 190, height // 2 - 120, 150, 40)
    pygame.draw.rect(screen, pygame.Color("White"), chr_rect)
    screen.blit(chr_txt, (width // 2 - chr_txt.get_width() // 2 + 210, height // 2 - chr_txt.get_height() // 2 - 100))
    return chr_rect

def draw_continue_button(screen): #добавить потом
    continue_button_rect = pygame.Rect(width // 2 - 100, height // 2 - 50, 200, 50)
    pygame.draw.rect(screen, pygame.Color("White"), continue_button_rect)
    continue_text = font.render("Продолжить", True, pygame.Color("Black"))
    screen.blit(continue_text, (continue_button_rect.x + 30, continue_button_rect.y + 10))
    return continue_button_rect

def draw_settings_button_for_cont(screen):
    se_cont_text = font.render("Настройки", True, pygame.Color("Black"))
    se_cont_bt = pygame.Rect(10, 60, se_cont_text.get_width() + 100, se_cont_text.get_height() // 2 + 20)
    pygame.draw.rect(screen, pygame.Color("White"), se_cont_bt)
    screen.blit(se_cont_text, (se_cont_bt.x + 50, se_cont_bt.y + 5))
    return se_cont_bt

def draw_settings_button_for_cont_ret(screen):
    se_cont_text_ret = font.render("Вернуться", True, pygame.Color("Black"))
    se_cont_bt_ret = pygame.Rect(10, 60, se_cont_text_ret.get_width() + 100, se_cont_text_ret.get_height() // 2 + 20)
    pygame.draw.rect(screen, pygame.Color("White"), se_cont_bt_ret)
    screen.blit(se_cont_text_ret, (se_cont_bt_ret.x + 50, se_cont_bt_ret.y + 5))
    return se_cont_bt_ret


pygame.init()
size = width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
font = pygame.font.Font(None, 36)
pygame.mixer.music.load("musicbg.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
music_playing = True
boy_image = pygame.image.load("boy.png").convert_alpha()
girl_image = pygame.image.load("girl.png").convert_alpha()
room_image = pygame.image.load("room.png").convert_alpha()
image = boy_image
chr_rect = draw_character_settings_button(screen)
image_rect = image.get_rect(center=(chr_rect.centerx, chr_rect.bottom + image.get_height() // 2 + 20))
bg_color = (255, 0, 0)
current_screen = "start"
st_bt = None
se_bt = None
color_settings_rect = None
music_settings_rect = None
se_re_bt = None
continue_button_rect = None
se_cont_bt = None
se_cont_bt_ret = None
running = True
change_image = False
while running:
    screen.fill(bg_color)
    if current_screen == "start":
        st_bt = draw_start_button(screen)
        se_bt = draw_settings_button(screen)
        image_rect = image.get_rect(center=(chr_rect.centerx - 200, chr_rect.bottom + image.get_height() // 2 + 50))
        screen.blit(image, image_rect)
    elif current_screen == "settings":
        draw_settings(screen)
        color_settings_rect = draw_color_settings_button(screen)
        chr_rect = draw_character_settings_button(screen)
        music_settings_rect = draw_music_settings_button(screen)
        image_rect = image.get_rect(center=(chr_rect.centerx, chr_rect.bottom + image.get_height() // 2 - 50))
        screen.blit(image, image_rect)
        se_re_bt = draw_return_button(screen)
    elif current_screen == "settings_for_cont":
        draw_settings(screen)
        color_settings_rect = draw_color_settings_button(screen)
        chr_rect = draw_character_settings_button(screen)
        music_settings_rect = draw_music_settings_button(screen)
        image_rect = image.get_rect(center=(chr_rect.centerx, chr_rect.bottom + image.get_height() // 2 - 50))
        screen.blit(image, image_rect)
        se_cont_bt_ret = draw_settings_button_for_cont_ret(screen)
    elif current_screen == "continue":
        room_image_scaled = pygame.transform.scale(room_image, (width, height))
        screen.blit(room_image_scaled, (0, 0))
        se_cont_bt = draw_settings_button_for_cont(screen)
        image_scaled = pygame.transform.scale(image, (width // 4, height // 4))
        image_rect = image_scaled.get_rect(center=(width // 2 + 300, height // 2 + 400))
        screen.blit(image, image_rect)
    elif current_screen == "end":
        end_text = font.render("GAME OVER", True, pygame.Color("Black"))
        screen.blit(end_text, (width // 2 - end_text.get_width() // 2, height // 2 - end_text.get_height() // 2))
    if change_image:
        if image == boy_image:
            image = girl_image
        else:
            image = boy_image
        image_rect = image.get_rect(center=image_rect.center)
        change_image = False
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "start" and st_bt.collidepoint(event.pos):
                current_screen = "continue"
            elif current_screen == "start" and se_bt.collidepoint(event.pos):
                current_screen = "settings"
            elif current_screen == "settings" and chr_rect.collidepoint(event.pos):
                change_image = True
            elif current_screen == "settings" and color_settings_rect.collidepoint(event.pos):
                bg_color = random_color_change()
            elif current_screen == "settings" and music_settings_rect.collidepoint(event.pos):
                if music_playing:
                    pygame.mixer.music.pause()
                    music_playing = False
                else:
                    pygame.mixer.music.unpause()
                    music_playing = True
            elif current_screen == "settings" and se_re_bt.collidepoint(event.pos):
                current_screen = "start"
            elif current_screen == "continue" and se_cont_bt.collidepoint(event.pos):
                current_screen = "settings_for_cont"
            elif current_screen == "settings_for_cont" and chr_rect.collidepoint(event.pos):
                change_image = True
            elif current_screen == "settings_for_cont" and color_settings_rect.collidepoint(event.pos):
                bg_color = random_color_change()
            elif current_screen == "settings_for_cont" and music_settings_rect.collidepoint(event.pos):
                if music_playing:
                    pygame.mixer.music.pause()
                    music_playing = False
                else:
                    pygame.mixer.music.unpause()
                    music_playing = True
            elif current_screen == "settings_for_cont" and se_cont_bt_ret.collidepoint(event.pos):
                current_screen = "continue"
