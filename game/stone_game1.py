import random

from comm.common import slow_print


def stone_game():
    slow_print('****石头剪刀布****')
    while True:
        print('1. 石头\n2. 剪刀\n3. 布\n')
        computer = random.choice(('石头', '剪刀', '布'))
        shuru = input('请出拳(输入q退出,输入数字) :')
        if shuru == 'q':
            print('已退出')
            break
