import random

from comm.common import tuichu, input_timeout

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'i', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
number = []


def keyboard_game():
    print('这是一个打字游戏')
    while True:
        number.clear()
        yunhuan = random.randint(5, 20)
        for i in range(yunhuan):
            number1 = random.choice(char)
            number.append(number1)
        last_str = "".join(number)
        print(last_str)
        while True:
            huoqu = input_timeout('请输入这几个字母(输入q退出): ')
            tuichu(huoqu)
            if huoqu == last_str:
                print('输入正确 !')
                break
            else:
                print('这个单词输入错误')


if __name__ == '__main__':
    keyboard_game()
