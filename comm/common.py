import sys
import time


def tuichu(input_str, tishi='已退出', tuichu_str='q'):
    if input_str == tuichu_str:
        print(tishi)
        sys.exit()


def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # 换行


def slow_input(text, delay=0.25):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    return input()  # 换行
