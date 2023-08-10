from comm.common import *


def rgb_and_hex():
    orange_print('这是一个可以把RGB值转换成十六进制值\n'
                 '也可以把十六进制值转换成RGB值的程序')
    while True:
        try:
            huoqu = cyan_input('1. RGB值转换成十六进制值\n'
                               '2. 十六进制值转换成RGB值\n'
                               '请选择(输入数字，输入q退出):')
            if huoqu == 'q':
                orange_print('已退出')
                break
            elif huoqu == '1':
                while True:
                    shuru = yellow_input2('请输入一个RGB值, 比如 "235,235,235"(不用空格分) , 输入q退出:')
                    if shuru == 'q':
                        orange_print('已退出')
                        break
                    else:
                        hox = rgb_to_hex(shuru)
                        purple_print('十六进制值为:')
                        print(hox)
            elif huoqu == '2':
                while True:
                    shuru = yellow_input2('请输入一个十六进制值值, 比如 "292c33" , 输入q退出:')
                    if shuru == 'q':
                        orange_print('已退出')
                        break
                    else:
                        rgb = hex_to_rgb(shuru)
                        purple_print('RGB值为:')
                        print(rgb)
            else:
                red_print('选项无效')
        except:
            red_print('输入有误')


if __name__ == '__main__':
    rgb_and_hex()
