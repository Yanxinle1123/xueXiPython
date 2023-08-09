import random
import sys

import pygame


def get_non_overlapping_rect(existing_rects, new_rect_width, new_rect_height):
    while True:
        new_rect = pygame.Rect(random.randint(0, width - new_rect_width),
                               random.randint(0, height - new_rect_height),
                               new_rect_width, new_rect_height)
        if not any(new_rect.colliderect(rect) for rect in existing_rects):
            return new_rect


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
title = 'Moving Bubbles'
hex_color = '#F6F6F6'
rgb_color = pygame.Color(hex_color)
screen.fill(rgb_color)

original_ball = pygame.image.load('/Users/lele/lele/3031903678.png')

# 创建包含1个气泡的列表，每个气泡有一个随机大小和速度
bubbles = []
existing_rects = []


def bubble(ball_size):
    for i in range(1):
        # ball_size = 200
        ball = pygame.transform.scale(original_ball, (ball_size, ball_size))
        ballrect = get_non_overlapping_rect(existing_rects, ball_size, ball_size)
        existing_rects.append(ballrect)
        speed_x = random.choice([-1, -1, 1])
        speed_y = random.choice([-1, -1, 1])
        bubbles.append([ball, ballrect, speed_x, speed_y])


clock = pygame.time.Clock()
pygame.display.set_caption(title)
speed = 250
ball_size = 250
bubble(ball_size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_EQUALS]:
        speed += 1
    elif keys[pygame.K_MINUS]:
        speed -= 1
    elif keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
    if speed >= 501:
        speed = 500
    elif speed <= 9:
        speed = 10

    screen.fill(rgb_color)

    # 更新气泡的位置并绘制到屏幕上
    for i, (ball, ballrect, speed_x, speed_y) in enumerate(bubbles):
        ballrect = ballrect.move(speed_x, speed_y)

        if ballrect.left < 0 or ballrect.right > width:
            speed_x = -speed_x
        if ballrect.top < 0 or ballrect.bottom > height:
            speed_y = -speed_y

        # 更新气泡速度
        bubbles[i] = [ball, ballrect, speed_x, speed_y]

        screen.blit(ball, ballrect)

    pygame.display.flip()
    clock.tick(speed)
