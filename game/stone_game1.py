import random

from comm.common import slow_print


def stone_game():
    slow_print('****石头剪刀布****')
    print('下面你将和计算机来一场石头剪刀布游戏 !')
    n = 1
    while True:
        print('第 {} 局'.format(n))
        print('1. 石头\n2. 剪刀\n3. 布\n')
        computer = random.choice(('石头', '剪刀', '布'))
        shuru = input('请出拳(输入q退出,输入数字) :')
        if shuru == 'q':
            print('已退出')
            break
        if computer == '石头':
            if shuru == '1':
                print('计算机:石头')
                print('你:石头')
                print("结果:平局")
                n = n + 1
            elif shuru == '2':
                print("计算机:石头")
                print('你:剪刀')
                print("结果:计算机获胜")
                n = n + 1
            elif shuru == '3':
                print("计算机:石头")
                print('你:布')
                print("结果:你获胜 !")
                n = n + 1
            else:
                print('选项', shuru, '无效')
        elif computer == '剪刀':
            if shuru == '1':
                print("计算机:剪刀")
                print('你:石头')
                print('结果:你获胜 !')
                n = n + 1
            elif shuru == '2':
                print('计算机:剪刀')
                print('你:剪刀')
                print('结果:平局')
                n = n + 1
            elif shuru == '3':
                print('计算机:剪刀')
                print('你:布')
                print('结果:计算机获胜')
                n = n + 1
            else:
                print('选项', shuru, '无效')
        else:
            if shuru == '1':
                print("计算机:布")
                print('你:石头')
                print('结果:计算机获胜')
                n = n + 1
            elif shuru == '2':
                print('计算机:布')
                print('你:剪刀')
                print('结果:你获胜 !')
                n = n + 1
            elif shuru == '3':
                print('计算机:布')
                print('你:布')
                print('结果:平局')
                n = n + 1
            else:
                print('选项', shuru, '无效')


if __name__ == '__main__':
    stone_game()
