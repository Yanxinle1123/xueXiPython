import random
import sys

import numpy as np
import pygame

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Snake Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# Set up snake and food
snake_pos = np.array([[100, 50], [90, 50], [80, 50]])
snake_speed = np.array([10, 0])
snake_colors = [random_color() for _ in range(len(snake_pos))]
food_pos = np.array([random.randrange(1, WIDTH // 10) * 10, random.randrange(1, HEIGHT // 10) * 10])
food_speed = np.array([0, 0])
food_color = random_color()
score = 0

# Set up game clock
clock = pygame.time.Clock()

# Set up font for score display
font = pygame.font.Font(None, 36)

# Initialize food path
food_path = [food_pos.copy()]


# Set up button
class Button:
    def __init__(self, x, y, width, height, color, text='', text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if self.text:
            font = pygame.font.Font(None, 20)
            text = font.render(self.text, True, self.text_color)
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False


button_x, button_y = 10, 60
button_width, button_height = 200, 40
button_color = (0, 255, 0)
button_text = 'Toggle Auto/Manual'
button_text_color = BLACK
button = Button(button_x, button_y, button_width, button_height, button_color, button_text, button_text_color)

# Set up flag for food movement mode
auto_mode = True


def draw_score():
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))


def generate_food():
    global food_pos
    while True:
        food_pos = np.array([random.randrange(1, WIDTH // 10 - 1) * 10, random.randrange(1, HEIGHT // 10 - 1) * 10])
        if food_pos[1] != snake_pos[0][1]:
            break


def increase_score():
    global score
    score += 1


def move_snake():
    global snake_pos
    global snake_speed
    global food_path

    if auto_mode:
        diff = food_pos - snake_pos[0]
        snake_speed = np.sign(diff) * 10
    else:
        if len(food_path) > 0:
            target_pos = food_path.pop(0)
            snake_speed = (target_pos - snake_pos[0]) / 2  # 蛇速度是食物速度的一半
        else:
            snake_speed = np.array([0, 0])

    snake_pos = np.insert(snake_pos, 0, snake_pos[0] + snake_speed, axis=0)
    snake_colors.insert(0, random_color())

    # 检查蛇头与食物之间的距离
    distance = np.linalg.norm(snake_pos[0] - food_pos)

    if distance <= 20:  # 当距离小于等于20时（允许一格距离），认为食物被吃掉
        generate_food()
        increase_score()
    else:
        snake_pos = snake_pos[:-1]
        snake_colors.pop()


def move_food():
    global food_pos
    global food_speed

    if auto_mode:
        diff = pygame.math.Vector2(snake_pos[0][0] - food_pos[0], snake_pos[0][1] - food_pos[1])
        food_speed = -diff.normalize() * (10 / 3)  # 设置食物速度为蛇速度的三分之一
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            food_speed = np.array([-10, 0])  # 向左移动
        elif keys[pygame.K_RIGHT]:
            food_speed = np.array([10, 0])  # 向右移动
        elif keys[pygame.K_UP]:
            food_speed = np.array([0, -10])  # 向上移动
        elif keys[pygame.K_DOWN]:
            food_speed = np.array([0, 10])  # 向下移动
        else:
            food_speed = np.array([0, 0])  # 停止移动

    new_food_pos = food_pos + food_speed
    # 检查食物移动后是否与蛇身碰撞或超出边界
    if (
            new_food_pos[0] < 0
            or new_food_pos[0] >= WIDTH
            or new_food_pos[1] < 0
            or new_food_pos[1] >= HEIGHT
            or np.any(np.all(snake_pos == new_food_pos, axis=1))  # 避免与蛇身碰撞
    ):
        generate_food()
    else:
        food_pos = new_food_pos


while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        elif button.is_clicked(event):
            auto_mode = not auto_mode
            if auto_mode:
                button.color = (0, 255, 0)
                button.text = 'Toggle Auto/Manual'
            else:
                button.color = (255, 0, 0)
                button.text = 'Toggle Auto/Manual'

    # Move snake
    move_snake()

    # Move food
    move_food()

    # Check for collisions with walls
    if (
            snake_pos[0][0] < 0
            or snake_pos[0][0] >= WIDTH
            or snake_pos[0][1] < 0
            or snake_pos[0][1] >= HEIGHT
    ):
        pygame.quit()
        sys.exit()

    # Check for collision with snake body
    if np.all(snake_pos[0] == snake_pos[1:]):
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(WHITE)
    for i, pos in enumerate(snake_pos):
        pygame.draw.rect(screen, snake_colors[i], pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Draw score
    draw_score()

    # Draw button
    button.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap framerate
    clock.tick(15)
