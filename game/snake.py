import random
import sys

import pygame

# 初始化pygame
pygame.init()

# 设置屏幕尺寸和标题
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# 设置游戏速度
clock = pygame.time.Clock()
ball_speed = 1

# 定义颜色
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# 定义蛇和食物的大小
snake_size = 20
food_size = 20

snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = [snake_size, 0]

food_pos = [random.randrange(1, (screen_width // 20)) * 20, random.randrange(1, (screen_height // 20)) * 20]
food_spawn = True

# 游戏主循环
while True:
    # 检查游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_UP]:
                snake_speed = [0, -snake_size]
            if keys[pygame.K_DOWN]:
                snake_speed = [0, snake_size]
            if keys[pygame.K_LEFT]:
                snake_speed = [-snake_size, 0]
            if keys[pygame.K_RIGHT]:
                snake_speed = [snake_size, 0]

    # 更新蛇的位置
    snake_pos.insert(0, list(snake_pos[0]))
    snake_pos[0][0] += snake_speed[0]
    snake_pos[0][1] += snake_speed[1]

    # 检查蛇是否吃到食物
    if snake_pos[0] == food_pos:
        food_spawn = False
    else:
        snake_pos.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (screen_width // 20)) * 20, random.randrange(1, (screen_height // 20)) * 20]
    food_spawn = True

    # 检查蛇是否撞到边界或自己
    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= screen_width or
            snake_pos[0][1] < 0 or snake_pos[0][1] >= screen_height or
            snake_pos[0] in snake_pos[1:]):
        pygame.quit()
        sys.exit()

    # 清除屏幕
    screen.fill(white)

    # 绘制蛇和食物
    for pos in snake_pos:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snake_size, snake_size))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], food_size, food_size))

    # 更新屏幕
    pygame.display.flip()

    # 控制游戏速度
    clock.tick(ball_speed)
