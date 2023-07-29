import sys
import time

from colored import Fore


def tuichu(input_str, tishi='已退出', tuichu_str='q'):
    if input_str == tuichu_str:
        print(tishi)
        sys.exit()


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


def print_orange(input_str):
    print(Fore.RGB(255, 170, 0) + input_str)


def print_green(input_str):
    print(Fore.RGB(125, 250, 85) + input_str)


def print_blue(input_str):
    print(Fore.RGB(50, 150, 225) + input_str)


def print_red(input_str):
    print(Fore.RGB(225, 0, 50) + input_str)


def input_green(input_str):
    result = input(Fore.RGB(125, 250, 85) + input_str)
    return result


def print_yellow(input_str):
    print(Fore.CYAN + Fore.GREEN + Fore.RED + Fore.GREEN + Fore.BLUE + Fore.YELLOW + input_str)


def input_yellow(input_str):
    result = input(Fore.CYAN + Fore.GREEN + Fore.RED + Fore.GREEN + Fore.BLUE + Fore.YELLOW + input_str)
    return result


def print_yellow2(input_str):
    print(Fore.RGB(225, 255, 0) + input_str)


def print_purple(input_str):
    print(Fore.RGB(171, 91, 187) + input_str)


def input_yellow2(input_str):
    result = input(Fore.RGB(225, 255, 0) + input_str)
    return result
