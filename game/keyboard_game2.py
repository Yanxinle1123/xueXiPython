import pygame

# 初始化 Pygame 库
pygame.init()

# 创建窗口
screen = pygame.display.set_mode((800, 600))

# 设置窗口标题
pygame.display.set_caption('Hello, Pygame!')

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 渲染画面
    screen.fill((255, 255, 255))
    pygame.display.flip()

# 退出 Pygame 库
pygame.quit()
