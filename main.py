import pygame


def draw_start_button(screen):
    start_button_rect = pygame.Rect(width // 2 - 100, height // 2 - 50, 200, 50)
    pygame.draw.rect(screen, pygame.Color("White"), start_button_rect)
    start_text = font.render("Начать игру", True, pygame.Color("Black"))
    screen.blit(start_text, (start_button_rect.x + 50, start_button_rect.y + 10))
    return start_button_rect

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
continue_button_rect = None
while True:
    screen.fill(pygame.Color("darkolivegreen1"))
    if current_screen == "start":
        start_button_rect = draw_start_button(screen)
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
            elif current_screen == "continue" and continue_button_rect.collidepoint(event.pos):
                current_screen = "end"
