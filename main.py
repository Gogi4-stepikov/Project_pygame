import pygame


def draw_start_button(screen):
    start_button_rect = pygame.Rect(width // 2 - 100, height // 2 - 50, 200, 50)
    pygame.draw.rect(screen, pygame.Color("White"), start_button_rect)
    start_text = font.render("Начать игру", True, pygame.Color("Black"))
    screen.blit(start_text, (start_button_rect.x + 50, start_button_rect.y + 10))
    return start_button_rect

def draw_settings_button(screen):
    settings_button_rect = pygame.Rect(10, 60, 150, 40)
    pygame.draw.rect(screen, pygame.Color("White"), settings_button_rect)
    settings_text = font.render("Настройки", True, pygame.Color("Black"))
    screen.blit(settings_text, (settings_button_rect.x + 50, settings_button_rect.y + 10))
    return settings_button_rect

def draw_settings(screen):
    set_lbl = font.render("Настройки", True, pygame.Color("Black"))
    screen.blit(set_lbl, (width // 2 - set_lbl.get_width() // 2, height // 2 - set_lbl.get_height() // 2 - 500))

def draw_color_settings_button(screen):
    clr_text = font.render("Цвет", True, pygame.Color("Black"))
    color_settings_button_rect = pygame.Rect(width // 2 - clr_text.get_width() // 2, height // 2 - 120, 150, 40)
    pygame.draw.rect(screen, pygame.Color("White"), color_settings_button_rect)
    screen.blit(clr_text, (width // 2 - clr_text.get_width() // 2, height // 2 - clr_text.get_height() // 2 - 100))
    return color_settings_button_rect

def draw_music_settings_button(screen):
    msc_txt = font.render("Музыка", True, pygame.Color("Black"))
    music_settings_button_rect = pygame.Rect(width // 2 - msc_txt.get_width() // 2 - 220, height // 2 - 120, 150, 40)
    pygame.draw.rect(screen, pygame.Color("White"), music_settings_button_rect)
    screen.blit(msc_txt, (width // 2 - msc_txt.get_width() // 2 - 200, height // 2 - msc_txt.get_height() // 2 - 100))
    return music_settings_button_rect

def draw_character_settings_button(screen):
    chr_txt = font.render("Персонаж", True, pygame.Color("Black"))
    character_settings_button_rect = pygame.Rect(width // 2 - chr_txt.get_width() // 2 + 220, height // 2 - 120, 150, 40)
    pygame.draw.rect(screen, pygame.Color("White"), character_settings_button_rect)
    screen.blit(chr_txt, (width // 2 - chr_txt.get_width() // 2 + 210, height // 2 - chr_txt.get_height() // 2 - 100))
    return character_settings_button_rect

def draw_continue_button(screen):
    continue_button_rect = pygame.Rect(width // 2 - 100, height // 2 - 50, 200, 50)
    pygame.draw.rect(screen, pygame.Color("White"), continue_button_rect)
    continue_text = font.render("Продолжить", True, pygame.Color("Black"))
    screen.blit(continue_text, (continue_button_rect.x + 30, continue_button_rect.y + 10))
    return continue_button_rect

pygame.init()
size = width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
font = pygame.font.Font(None, 36)
current_screen = "start"
start_button_rect = None
settings_button_rect = None
color_settings_button_rect = None
continue_button_rect = None
while True:
    screen.fill(pygame.Color("antiquewhite"))
    if current_screen == "start":
        start_button_rect = draw_start_button(screen)
        settings_button_rect = draw_settings_button(screen)
    elif current_screen == "settings":
        draw_settings(screen)
        color_settings_button_rect = draw_color_settings_button(screen)
        character_settings_button_rect = draw_character_settings_button(screen)
        music_settings_rect = draw_music_settings_button(screen)
    elif current_screen == "continue":
        continue_button_rect = draw_continue_button(screen)
    elif current_screen == "end":
        end_text = font.render("GAME OVER", True, pygame.Color("Black"))
        screen.blit(end_text, (width // 2 - end_text.get_width() // 2, height // 2 - end_text.get_height() // 2))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "start" and start_button_rect.collidepoint(event.pos):
                current_screen = "continue"
            elif current_screen == "start" and settings_button_rect.collidepoint(event.pos):
                current_screen = "settings"
            elif current_screen == "settings" and color_settings_button_rect.collidepoint(event.pos):
                current_screen = "color_settings"
            elif current_screen == "color_settings" and color_settings_button_rect.collidepoint(event.pos):
                current_screen = "settings"
            elif current_screen == "settings" and character_settings_button_rect.collidepoint(event.pos):
                current_screen = "character_settings"
            elif current_screen == "character_settings" and character_settings_button_rect.collidepoint(event.pos):
                current_screen = "settings"
            elif current_screen == "continue" and continue_button_rect.collidepoint(event.pos):
                current_screen = "end"
