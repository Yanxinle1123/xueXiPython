import random
import sys

import pygame

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
title = 'Moving Bubbles'
hex_color = '#F6F6F6'
rgb_color = pygame.Color(hex_color)
screen.fill(rgb_color)
original_ball1 = pygame.image.load('/Users/lele/lele/141691486798_.pic.jpg')
ball_width1 = 200
ball_height1 = 200
ball = pygame.transform.scale(original_ball1, (ball_width1, ball_height1))
ballrect = ball.get_rect()
x = random.randint(10, 25)
y = random.randint(10, 30)
clock = pygame.time.Clock()
pygame.display.set_caption(title)

speed = 60
is_plus_pressed = False
is_minus_pressed = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # 检查按下的键是否是q
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_EQUALS:
                is_plus_pressed = True
            elif event.key == pygame.K_MINUS:
                is_minus_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_EQUALS:
                is_plus_pressed = False
            elif event.key == pygame.K_MINUS:
                is_minus_pressed = False

    if is_plus_pressed:
        speed += 0.5
    elif is_minus_pressed:
        speed -= 0.5
    if speed == 151:
        speed = 150
    elif speed == 29:
        speed = 30

    screen.fill(rgb_color)
    ballrect = ballrect.move(x, y)

    if ballrect.left < 0 or ballrect.right > width:
        x = -x
    if ballrect.top < 0 or ballrect.bottom > height:
        y = -y

    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(speed)
