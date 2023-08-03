import select
import sys
import time

from colored import Fore


def tuichu(input_str, tishi='已退出', tuichu_str='q'):
    if input_str == tuichu_str:
        orange_print(tishi)
        sys.exit()


class TimeoutExpired(Exception):
    pass


def input_timeout(prompt, timeout=9):
    print(Fore.RGB(225, 255, 0) + prompt, end=" ", flush=True)
    fds = [sys.stdin]
    result = []
    r, _, _ = select.select(fds, [], [], timeout)
    if not r:
        raise TimeoutExpired()

    input_str = sys.stdin.readline().rstrip()
    result.append(input_str)
    return result[0]


def stop_thread(thread):
    thread.cancel()


def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # 换行


def slow_input(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    return input()  # 换行


def tuichu2(input_str, tishi='已退出', tuichu_str='n'):
    if input_str == tuichu_str:
        print(tishi)
        sys.exit()


def slow_print2(text, delay=0.25):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def orange_print(input_str):
    print(Fore.RGB(255, 170, 0) + input_str)


def green_print(input_str):
    print(Fore.RGB(125, 250, 85) + input_str)


def blue_print(input_str):
    print(Fore.RGB(50, 150, 225) + input_str)


def red_print(input_str):
    print(Fore.RGB(225, 0, 50) + input_str)


def green_input(input_str):
    result = input(Fore.RGB(125, 250, 85) + input_str)
    return result


def yellow_print(input_str):
    print(Fore.CYAN + Fore.GREEN + Fore.RED + Fore.GREEN + Fore.BLUE + Fore.YELLOW + input_str)


def yellow_input(input_str):
    result = input(Fore.CYAN + Fore.GREEN + Fore.RED + Fore.GREEN + Fore.BLUE + Fore.YELLOW + input_str)
    return result


def yellow_print2(input_str):
    print(Fore.RGB(225, 255, 0) + input_str)


def purple_print(input_str):
    print(Fore.RGB(171, 91, 187) + input_str)


def input_yellow2(input_str):
    result = input(Fore.RGB(225, 255, 0) + input_str)
    return result


def is_chinese_start(s):
    return s and 0x4E00 <= ord(s[0]) <= 0x9FA0


def is_chinese_start(s):
    return s and 0x4E00 <= ord(s[0]) <= 0x9FA0
