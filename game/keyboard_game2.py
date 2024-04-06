import sys

import pygame

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'i', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
number = []
pygame.init()
pygame.font.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
buffer = pygame.Surface((screen_width, screen_height))
screen.fill((126, 248, 85))
pygame.display.set_caption("Keyboard__Game")
running = True

# 创建三个按钮矩形
button_rect = pygame.Rect(100, 100, 200, 50)
button_rect2 = pygame.Rect(100, 200, 200, 50)
button_rect3 = pygame.Rect(100, 300, 200, 50)
button_rect4 = pygame.Rect(20, 20, 100, 40)

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 获取用户点击的位置
            pos = pygame.mouse.get_pos()
            # 检查用户是否点击了按钮
            if button_rect.collidepoint(pos):
                print("Button 1 clicked!")
                screen.fill((255, 170, 0))
            elif button_rect2.collidepoint(pos):
                print("Button 2 clicked!")
                screen.fill((125, 250, 85))
            elif button_rect3.collidepoint(pos):
                print("Button 3 clicked!")
                screen.fill((225, 255, 0))
            elif button_rect4.collidepoint(pos):
                sys.exit()

    # 创建三个不同大小的字体对象
    font1 = pygame.font.SysFont("Arial", 40)
    font2 = pygame.font.SysFont("Arial", 40)
    font3 = pygame.font.SysFont("Arial", 40)
    font4 = pygame.font.SysFont("Arial", 30)

    # 在屏幕上渲染文本
    text = font1.render("lower", True, (50, 150, 225))
    text2 = font2.render("medium", True, (50, 150, 225))
    text3 = font3.render("advanced", True, (50, 150, 225))
    text4 = font4.render("quit", True, (50, 150, 225))

    # 将文本显示在按钮上
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    text2_rect = text2.get_rect(center=button_rect2.center)
    screen.blit(text2, text2_rect)
    text3_rect = text3.get_rect(center=button_rect3.center)
    screen.blit(text3, text3_rect)
    text4_rect = text4.get_rect(center=button_rect4.center)
    screen.blit(text4, text4_rect)
    # 在屏幕上绘制三个矩形按钮
    pygame.draw.rect(screen, (255, 0, 0), button_rect, 2)
    pygame.draw.rect(screen, (255, 0, 0), button_rect2, 2)
    pygame.draw.rect(screen, (255, 0, 0), button_rect3, 2)
    pygame.draw.rect(screen, (255, 0, 0), button_rect4, 2)

    # 在屏幕上绘制标题文本
    title_font = pygame.font.SysFont("Arial", 48)
    title_text = title_font.render("Keyboard__Game", True, (255, 25, 0))
    screen.blit(title_text, (300, 10))

    pygame.display.update()  # 注意：需要在初始化 Pygame 显示模块之后调用

pygame.quit()  # 循环结束后退出
