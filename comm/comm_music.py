from tkinter import Tk

import pygame


def play_music(music_file, is_need_init=False):
    # music_file = "Joachim Neuville - Arena [mqms].ogg"
    if is_need_init:
        pygame.mixer.init()
        pygame.mixer.music.load(music_file)
    pygame.mixer.music.stop()
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


def play_music_with_window(music_file, cycle_time_ms=28000, is_need_init=False, is_hide_window=True):
    win = Tk()
    play_music(music_file, is_need_init)
    if is_hide_window:
        win.withdraw()
    win.after(cycle_time_ms, play_music_with_window, music_file)


window = Tk()
music_file = "/Users/lele/Music/Joachim Neuville - Arena [mqms].ogg"
play_music_with_window(music_file, 290000, True)
window.withdraw()
window.mainloop()
