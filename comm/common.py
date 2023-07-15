import sys


def tuichu(guess_str, tishi='已退出'):
    if guess_str == 'q':
        print(tishi)
        sys.exit()
