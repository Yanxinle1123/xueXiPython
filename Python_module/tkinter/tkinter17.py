from tkinter import Tk

import pygame

# 设置音乐文件路径
music_file = "Joachim Neuville - Arena [mqms].ogg"

# 初始化pygame
pygame.mixer.init()

# 创建Tkinter窗口
window = Tk()
window.title("音乐播放器")


# 定义播放音乐的函数
def play_music():
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    window.after(288000, play_music)  # 1秒后再次调用play_music函数，实现循环播放


play_music()

# 运行Tkinter主循环
window.mainloop()
