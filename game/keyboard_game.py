import random

from comm.common import tuichu, input_timeout, TimeoutExpired, print_orange, print_green, print_red

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'i', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
number = []


def keyboard_game():
    print_orange('这是一个打字游戏')
    while True:
        number.clear()
        yunhuan = random.randint(5, 20)
        for i in range(yunhuan):
            number1 = random.choice(char)
            number.append(number1)
        last_str = "".join(number)
        print_green(last_str)
        while True:
            try:
                huoqu = input_timeout('请输入这几个字母(输入q退出): ')
                tuichu(huoqu)
                if huoqu == last_str:
                    print_green('输入正确 !')
                    break
                else:
                    print_red('这个单词输入错误')
            except TimeoutExpired:
                print_red("\n时间用完")
                break


if __name__ == '__main__':
    keyboard_game()
