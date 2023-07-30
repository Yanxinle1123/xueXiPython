import random
import time

from comm.common import input_timeout, TimeoutExpired, print_orange, print_green, print_red, input_yellow2, \
    print_purple

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'i', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
number = []


def keyboard_game():
    print_orange('这是一个打字游戏')
    while True:
        shuru = input_yellow2('1.低等\n2.中等\n3.高等\n请选择难度, 输入数字, 输入q退出): ')
        if shuru == 'q':
            print_orange('已退出')
            break
        r = 1
        while True:
            try:
                number.clear()
                xunhuan = random.randint(5, 25)
                for i in range(xunhuan):
                    number1 = random.choice(char)
                    number.append(number1)
                last_str = "".join(number)
                word_len = len(last_str)
                if shuru == '1':
                    timeout = word_len / 1
                elif shuru == '2':
                    timeout = word_len / 1.5
                elif shuru == '3':
                    timeout = word_len / 2
                else:
                    print_red('输入有误')
                    break
                print_purple('------------------------------第 {} 关------------------------------'.format(r))
                sleep_time = word_len / 4
                print('请看下面的单词', sleep_time, '秒后在输入')
                time.sleep(1)
                print_green(last_str)
                # print('word_len =', word_len, '|timeout = ', timeout, '|sleep_time =', sleep_time)
                time.sleep(sleep_time)
                huoqu = input_timeout('请输入这几个字母(输入q退出): ', timeout)
                if huoqu == 'q':
                    print_orange('已退出')
                    break
                elif huoqu == last_str:
                    print_green('输入正确 !')
                    r = r + 1
                    continue
                else:
                    print_red('这个单词输入错误')
                    r = r + 1
            except TimeoutExpired:
                print_red("\n时间已用完")
                r = r + 1
                continue


if __name__ == '__main__':
    keyboard_game()
