import random

from comm.common import slow_print


def stone_game():
    slow_print('* * * * 石 头 剪 刀 布 * * * *')
    print('下面你将和计算机来一场石头剪刀布游戏 !')
    n = 1
    while True:
        huoqu = input('一次共 5 局, 是否开始(输入q退出):')
        if huoqu == 'q':
            print('已退出')
            break
        e = 1
        while e <= 5:
            print('* * * * 第 {} 局 * * * *'.format(n))
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
                e = e + 1
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
                e = e + 1
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
                e = e + 1


if __name__ == '__main__':
    stone_game()
