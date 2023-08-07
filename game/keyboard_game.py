import random
import time

from comm.common import input_timeout, TimeoutExpired, orange_print, green_print, red_print, yellow_input2, \
    purple_print

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'i', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
number = []


def keyboard_game():
    orange_print('这是一个打字游戏')
    while True:
        shuru = yellow_input2('1.低等\n2.中等\n3.高等\n请选择难度, 输入数字, 输入q退出): ')
        if shuru == 'q':
            orange_print('已退出')
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
                    red_print('输入有误')
                    break
                purple_print('------------------------------第 {} 关------------------------------'.format(r))
                sleep_time = word_len / 4
                print('请看下面的单词', sleep_time, '秒后在输入')
                time.sleep(1)
                green_print(last_str)
                # print('word_len =', word_len, '|timeout = ', timeout, '|sleep_time =', sleep_time)
                time.sleep(sleep_time)
                huoqu = input_timeout('请输入这几个字母(输入q退出): ', timeout)
                if huoqu == 'q':
                    orange_print('已退出')
                    break
                elif huoqu == last_str:
                    green_print('输入正确 !')
                    r = r + 1
                    continue
                else:
                    red_print('这个单词输入错误')
                    r = r + 1
            except TimeoutExpired:
                red_print("\n时间已用完")
                r = r + 1
                continue


if __name__ == '__main__':
    keyboard_game()
