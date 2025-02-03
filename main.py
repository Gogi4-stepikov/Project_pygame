import random
import pygame
import sys
import time


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

def draw_dialog_one(screen):
    if image == boy_image:
        name = "Петя"
    else:
        name = "Катя"
    d_one_txt = font.render(f"Привет, я {name}!" , True, pygame.Color("Black"))
    screen.blit(d_one_txt, (width - d_one_txt.get_width() // 2 - 850, height - d_one_txt.get_height() // 2 - 550))

def draw_dialog_two(screen):
    d_two_txt = font.render("Ура! День рождения!", True, pygame.Color("Black"))
    screen.blit(d_two_txt, (width - d_two_txt.get_width() // 2 - 850, height - d_two_txt.get_height() // 2 - 550))

def draw_dialog_three(screen):
    d_three_txt = font.render("Что это за коробка?", True, pygame.Color("Black"))
    screen.blit(d_three_txt, (width - d_three_txt.get_width() // 2 - 850, height - d_three_txt.get_height() // 2 - 550))

def draw_dialog_four(screen):
    d_four_txt = font.render("Ого компьютер!", True, pygame.Color("Black"))
    screen.blit(d_four_txt, (width - d_four_txt.get_width() // 2 - 850, height - d_four_txt.get_height() // 2 - 550))

def draw_dialog_five(screen):
    d_five_txt = font.render("Куда бы его поставить?", True, pygame.Color("Black"))
    screen.blit(d_five_txt, (width - d_five_txt.get_width() // 2 - 850, height - d_five_txt.get_height() // 2 - 550))

def draw_dialog_six(screen):
    d_six_txt = font.render("Отлично!", True, pygame.Color("Black"))
    screen.blit(d_six_txt, (width - d_six_txt.get_width() // 2 - 850, height - d_six_txt.get_height() // 2 - 550))

def draw_dialog_seven(screen):
    d_seven_txt = font.render("Во что поиграем?", True, pygame.Color("Black"))
    screen.blit(d_seven_txt, (width - d_seven_txt.get_width() // 2 - 850, height - d_seven_txt.get_height() // 2 - 550))

def draw_havent_money(screen):
    money_lbl = font.render("Недостаточно денег", True, pygame.Color("Black"))
    screen.blit(money_lbl, (width // 2 - money_lbl.get_width() // 2, height // 2 - money_lbl.get_height() // 2))

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

def draw_buy_one(screen):
    buy_it_one_txt = font.render("Купить", True, pygame.Color("Black"))
    buy_one = pygame.Rect(
        width // 2 - buy_it_one_txt.get_width() // 2 - 200,
        height // 2 - buy_it_one_txt.get_height() // 2 - 220,
        200, 50
    )
    pygame.draw.rect(screen, pygame.Color("Green"), buy_one)
    screen.blit(buy_it_one_txt, (buy_one.x + 40, buy_one.y + 7))
    return buy_one

def draw_buy_two(screen):
    buy_it_two_txt = font.render("Купить", True, pygame.Color("Black"))
    buy_two = pygame.Rect(
        width // 2 - buy_it_two_txt.get_width() // 2 - 200,
        height // 2 - buy_it_two_txt.get_height() // 2 + 80,
        200, 50
    )
    pygame.draw.rect(screen, pygame.Color("Green"), buy_two)
    screen.blit(buy_it_two_txt, (buy_two.x + 40, buy_two.y + 7))
    return buy_two

def draw_buy_three(screen):
    buy_it_three_txt = font.render("Купить", True, pygame.Color("Black"))
    buy_three = pygame.Rect(
        width // 2 - buy_it_three_txt.get_width() // 2 - 200,
        height // 2 - buy_it_three_txt.get_height() // 2 + 380,
        200, 50
    )
    pygame.draw.rect(screen, pygame.Color("Green"), buy_three)
    screen.blit(buy_it_three_txt, (buy_three.x + 40, buy_three.y + 7))
    return buy_three

def draw_return_button_for_shop(screen):
    re_sh_text = font.render("Вернуться", True, pygame.Color("Black"))
    re_sh_bt = pygame.Rect(10, 60, re_sh_text.get_width() + 100, re_sh_text.get_height() // 2 + 20)
    pygame.draw.rect(screen, pygame.Color("White"), re_sh_bt)
    screen.blit(re_sh_text, (re_sh_bt.x + 50, re_sh_bt.y + 5))
    return re_sh_bt

def draw_settings_button_for_cont_ret(screen):
    se_cont_text_ret = font.render("Вернуться", True, pygame.Color("Black"))
    se_cont_bt_ret = pygame.Rect(10, 60, se_cont_text_ret.get_width() + 100, se_cont_text_ret.get_height() // 2 + 20)
    pygame.draw.rect(screen, pygame.Color("White"), se_cont_bt_ret)
    screen.blit(se_cont_text_ret, (se_cont_bt_ret.x + 50, se_cont_bt_ret.y + 5))
    return se_cont_bt_ret

def draw_return_button_for_snake(screen):
    snake_ret = font.render("Вернуться", True, pygame.Color("Black"))
    snake_rect = pygame.Rect(10, 60, snake_ret.get_width() + 100, snake_ret.get_height() // 2 + 20)
    pygame.draw.rect(screen, pygame.Color("White"), snake_rect)
    screen.blit(snake_ret, (snake_rect.x + 50, snake_rect.y + 5))
    return snake_rect

def load_money():
    try:
        with open("money.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

def save_money(money):
    try:
        with open("money.txt", "w") as f:
            f.write(str(money))
    except Exception as e:
        print(f"Ошибка сохранения денег", {e})

def game_snake():
    global game_over_snake
    snake_part = 10
    speed = 50

    def show_score(score):
        value = font.render("Ваш счёт:" + str(score), True, pygame.Color("Black"))
        value_text = value.get_rect(center=(width // 2, height - 600))
        screen.blit(value, value_text)

    def snake_character(snake_part, snake_list):
        for x in snake_list:
            pygame.draw.rect(screen, pygame.Color("Green"), [x[0], x[1], snake_part, snake_part])

    def message(msg, color):
        mesg = font.render(msg, True, color)
        screen.blit(mesg, [width / 6, height / 3])

    game_over_snake = False
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    snake_length = 1
    foodx = random.randrange(0, width - snake_part, snake_part)
    foody = random.randrange(0, height - snake_part, snake_part)
    score = 0
    clock = pygame.time.Clock()
    game_over_time = 0
    while not game_over_snake:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_part:
                    x1_change = -snake_part
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -snake_part:
                    x1_change = snake_part
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_part:
                    y1_change = -snake_part
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -snake_part:
                    y1_change = snake_part
                    x1_change = 0
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over_snake = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(bg_color)
        pygame.draw.rect(screen, pygame.Color("Red"), (foodx, foody, snake_part, snake_part))
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        show_score(score)
        if len(snake_list) > snake_length:
            snake_list = snake_list[1:]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over_snake = True
        snake_character(snake_part, snake_list)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = random.randrange(0, width - snake_part, snake_part)
            foody = random.randrange(0, height - snake_part, snake_part)
            snake_length += 1
            score += 1
        clock.tick(speed)
        if game_over_snake:
            message("Вы проиграли! Ваш счет: " + str(score), (0, 0, 0))
            pygame.display.update()
            pygame.time.delay(2000)
            current_screen = "continue"
            return

pygame.init()
size = width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
font = pygame.font.Font(None, 36)
money = load_money()
pygame.mixer.music.load("musicbg.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
music_playing = True
boy_image = pygame.transform.scale(pygame.image.load("boy.png").convert_alpha(), (width // 5.5, height // 3.5))
girl_image = pygame.transform.scale(pygame.image.load("girl.png").convert_alpha(), (width // 5.5, height // 3.5))
room_image = pygame.image.load("room.png").convert_alpha()
shop_image = pygame.transform.scale(pygame.image.load("shop.jpg").convert_alpha(), (width // 16, height // 16))
item_one_image = pygame.transform.scale(pygame.image.load("ЮЧА.png").convert_alpha(), (width // 5, height // 6))
sold_one_image = pygame.transform.scale(pygame.image.load("Pug.png").convert_alpha(), (width // 9, height // 8))
item_two_image = pygame.transform.scale(pygame.image.load("Мяч.png").convert_alpha(), (width // 5, height // 6))
sold_two_image = pygame.transform.scale(pygame.image.load("Ball.png").convert_alpha(), (width // 9, height // 9))
item_three_image = pygame.transform.scale(pygame.image.load("Сок.png").convert_alpha(), (width // 5, height // 6))
sold_three_image = pygame.transform.scale(pygame.image.load("ju.png").convert_alpha(), (width // 12, height // 9))
dialog_image = pygame.transform.scale(pygame.image.load("dialog.png").convert_alpha(), (width // 9, height // 6))
box_image = pygame.transform.scale(pygame.image.load("box.png").convert_alpha(), (width // 9, height // 6))
pc_image = pygame.transform.scale(pygame.image.load("computer.png").convert_alpha(), (width // 10, height // 7))
desk_image = pygame.transform.scale(pygame.image.load("Desktop.png").convert_alpha(), (width // 10, height // 7))
snake_game = pygame.transform.scale(pygame.image.load("snake.jpg").convert_alpha(), (width // 10, height // 6))
image = boy_image
chr_rect = draw_character_settings_button(screen)
image_rect = image.get_rect(center=(chr_rect.centerx, chr_rect.bottom + image.get_height() // 2 + 20))
bg_color = (120, 180, 160)
current_screen = "start"
st_bt = None
se_bt = None
color_settings_rect = None
music_settings_rect = None
se_re_bt = None
continue_button_rect = None
se_cont_bt = None
se_cont_bt_ret = None
shop_rect = None
re_sh_bt = None
buy_one = None
buy_two = None
buy_three = None
image_rect = None
pc_set_rect = None
snake_rect = None
running = True
change_image = False
dialog_one = False
game_over_snake = False
dialog_two = False
dialog_three = False
dialog_four = False
dialog_five = False
box_opened = False
box_closed = True
dialog_six = False
dialog_seven = False
pc_set = False
item_one_sold = False
item_two_sold = False
item_three_sold = False
havent_money = False
image_clicks = 0
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
        image_rect = image.get_rect(center=(width // 2 + 300, height // 2 + 400))
        screen.blit(image, image_rect)
        shop_rect = shop_image.get_rect(bottomright=(width - 100, height - 100))
        screen.blit(shop_image, shop_rect)
        if item_one_sold:
            sold_one_rect = sold_one_image.get_rect(center=(width - 1600, height - 300))
            screen.blit(sold_one_image, sold_one_rect)
        if item_two_sold:
            sold_two_rect = sold_two_image.get_rect(center=(width - 2000, height - 260))
            screen.blit(sold_two_image, sold_two_rect)
        if item_three_sold:
            sold_three_rect = sold_three_image.get_rect(center=(width - 1150, height - 350))
            screen.blit(sold_three_image, sold_three_rect)
        if dialog_one:
            dialog_one_rect = dialog_image.get_rect(center=(width - 850, height - 540))
            screen.blit(dialog_image, dialog_one_rect)
            draw_dialog_one(screen)
        if dialog_two:
            dialog_two_rect = dialog_image.get_rect(center=(width - 850, height - 540))
            screen.blit(dialog_image, dialog_two_rect)
            draw_dialog_two(screen)
        if dialog_three:
            dialog_three_rect = dialog_image.get_rect(center=(width - 850, height - 540))
            screen.blit(dialog_image, dialog_three_rect)
            draw_dialog_three(screen)
        if dialog_four:
            dialog_four_rect = dialog_image.get_rect(center=(width - 850, height - 540))
            screen.blit(dialog_image, dialog_four_rect)
            draw_dialog_four(screen)
        if dialog_five:
            dialog_five_rect = dialog_image.get_rect(center=(width - 850, height - 540))
            screen.blit(dialog_image, dialog_five_rect)
            draw_dialog_five(screen)
        if box_opened:
            pc_rect = pc_image.get_rect(center=(width - 600, height - 300))
            screen.blit(pc_image, pc_rect)
        if box_closed:
            box_rect = box_image.get_rect(center=(width - 600, height - 300))
            screen.blit(box_image, box_rect)
        if dialog_six:
            dialog_six_rect = dialog_image.get_rect(center=(width - 850, height - 540))
            screen.blit(dialog_image, dialog_six_rect)
            draw_dialog_six(screen)
        if dialog_seven:
            dialog_seven_rect = dialog_image.get_rect(center=(width - 850, height - 540))
            screen.blit(dialog_image, dialog_seven_rect)
            draw_dialog_seven(screen)
        if pc_set:
            pc_set_rect = desk_image.get_rect(center=(width - 1350, height - 485))
            screen.blit(desk_image, pc_set_rect)
    elif current_screen == "shop":
        if not item_one_sold:
            item_one_rect = item_one_image.get_rect(center=(width - 1300, height - 1000))
            screen.blit(item_one_image, item_one_rect)
            buy_one = draw_buy_one(screen)
        if not item_two_sold:
            item_two_rect = item_two_image.get_rect(center=(width - 1300, height - 700))
            screen.blit(item_two_image, item_two_rect)
            buy_two = draw_buy_two(screen)
        if not item_three_sold:
            item_three_rect = item_three_image.get_rect(center=(width - 1300, height - 400))
            screen.blit(item_three_image, item_three_rect)
            buy_three = draw_buy_three(screen)
        if havent_money:
            draw_havent_money(screen)
        re_sh_bt = draw_return_button_for_shop(screen)
        mo_txt = font.render(f"Деньги: {money}", True, pygame.Color("Black"))
        screen.blit(mo_txt, (width // 2 - mo_txt.get_width() // 2, height // 2 - mo_txt.get_height() // 2 - 500))
    elif current_screen == "games":
        ga_txt = font.render("Игры", True, pygame.Color("Black"))
        screen.blit(ga_txt, (width // 2 - ga_txt.get_width() // 2, height // 2 - ga_txt.get_height() // 2 - 500))
        snake_rect = snake_game.get_rect(center=(width - 1290, height - 1000))
        screen.blit(snake_game, snake_rect)
        pygame.display.update()
    elif current_screen == "snake_game":
        snake_rect = draw_return_button_for_snake(screen)
        game_snake()
        if game_over_snake:
            current_screen = "continue"
            game_over_snake = False
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
            elif current_screen == "continue" and shop_rect.collidepoint(event.pos):
                current_screen = "shop"
            elif current_screen == "continue" and image_rect.collidepoint(event.pos):
                image_clicks += 1
                if image_clicks == 1:
                    dialog_one = True
                if image_clicks == 2:
                    dialog_two = True
                    dialog_one = False
                if image_clicks == 3:
                    dialog_three = True
                    dialog_two = False
                if image_clicks == 4:
                    dialog_four = True
                    box_opened = True
                    box_closed = False
                    dialog_three = False
                if image_clicks == 5:
                    dialog_four = False
                    dialog_five = True
                if image_clicks == 6:
                    dialog_five = False
                    dialog_six = True
                    box_opened = False
                    pc_set = True
                if image_clicks == 7:
                    dialog_six = False
                    dialog_seven = True
                if image_clicks > 7:
                    dialog_seven = False
            elif current_screen == "shop" and buy_one.collidepoint(event.pos):
                if money >= 300:
                    money -= 300
                    save_money(money)
                    item_one_sold = True
                    havent_money = False
                else:
                    havent_money = True
            elif current_screen == "shop" and buy_two.collidepoint(event.pos):
                if money >= 150:
                    money -= 150
                    save_money(money)
                    item_two_sold = True
                    havent_money = False
                else:
                    havent_money = True
            elif current_screen == "shop" and buy_three.collidepoint(event.pos):
                if money >= 200:
                    money -= 200
                    save_money(money)
                    item_three_sold = True
                    havent_money = False
                else:
                    havent_money = True
            elif current_screen == "shop" and re_sh_bt.collidepoint(event.pos):
                havent_money = False
                current_screen = "continue"
            elif current_screen == "settings_for_cont" and music_settings_rect.collidepoint(event.pos):
                if music_playing:
                    pygame.mixer.music.pause()
                    music_playing = False
                else:
                    pygame.mixer.music.unpause()
                    music_playing = True
            elif current_screen == "settings_for_cont" and se_cont_bt_ret.collidepoint(event.pos):
                current_screen = "continue"
            elif pc_set_rect is not None and current_screen == "continue":
                if pc_set_rect.collidepoint(event.pos):
                    current_screen = "games"
            elif current_screen == "games" and snake_rect.collidepoint(event.pos):
                current_screen = "snake_game"
