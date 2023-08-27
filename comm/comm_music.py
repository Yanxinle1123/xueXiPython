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


def quit_music():
    pygame.mixer.music.stop()
    pygame.mixer.quit()


def play_music_with_window(music_file, cycle_time_ms=28000, is_need_init=False, is_hide_window=True):
    win = Tk()
    play_music(music_file, is_need_init)
    if is_hide_window and is_need_init:
        win.withdraw()
    win.after(cycle_time_ms, play_music_with_window, music_file, cycle_time_ms, False, is_hide_window)
    return win


def play_music_with_window2(win, music_file, cycle_time_ms=290000,
                            is_need_init=False, is_hide_window=True):
    play_music(music_file, is_need_init)
    if is_hide_window and is_need_init:
        win.withdraw()
    ret_id = win.after(cycle_time_ms, play_music_with_window2, win, music_file, cycle_time_ms, False, is_hide_window)
    return ret_id


def change_music(win, music_file, cycle_time_ms=290000,
                 is_need_init=False, is_hide_window=True, ret_id=None):
    stop_music()
    if ret_id is not None:
        win.after_cancel(ret_id)

    ret_id = play_music_with_window2(win, music_file, cycle_time_ms,
                                     is_need_init, is_hide_window)
    return ret_id

# window = Tk()
# music_file = "/Users/lele/Music/Joachim Neuville - Arena [mqms].ogg"
# play_music_with_window(music_file, 10000, False)
# window.mainloop()
