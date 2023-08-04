import random
import sys

import pyautogui
import pygame

a = pyautogui
# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Snake Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# Set up snake and food
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = [10, 0]
snake_colors = [random_color() for _ in range(len(snake_pos))]
food_pos = [random.randrange(1, WIDTH // 10) * 10, random.randrange(1, HEIGHT // 10) * 10]
food_color = random_color()
food_spawn = True
score = 0

# Set up game clock
clock = pygame.time.Clock()

# Set up font for score display
font = pygame.font.Font(None, 36)


def draw_score():
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))


def move_towards_food():
    if snake_pos[0][0] < food_pos[0]:
        return [10, 0]
    elif snake_pos[0][0] > food_pos[0]:
        return [-10, 0]
    elif snake_pos[0][1] < food_pos[1]:
        return [0, 10]
    elif snake_pos[0][1] > food_pos[1]:
        return [0, -10]


a.moveTo(600, 300)

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

    # Move snake
    snake_speed = move_towards_food()
    snake_pos.insert(0, [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]])
    snake_colors.insert(0, random_color())
    if snake_pos[0] == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_pos.pop()
        snake_colors.pop()

    # Spawn food
    if not food_spawn:
        food_pos = [random.randrange(1, WIDTH // 10) * 10, random.randrange(1, HEIGHT // 10) * 10]
        food_color = random_color()
    food_spawn = True

    # Check for collisions with walls
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT:
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(WHITE)
    for i, pos in enumerate(snake_pos):
        pygame.draw.rect(screen, snake_colors[i], pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Draw score
    draw_score()

    # Update display
    pygame.display.flip()

    # Cap framerate
    clock.tick(100)  # Set the frame rate to the maximum value
