import math

from colored import Fore

from comm.common import tuichu


def check():
    print(Fore.RGB(126, 251, 85) + "这是一个可以检查你的算数结果是否正确的程序")
    r = 1
    while True:
        try:
            shuru = input(Fore.RGB(255, 165, 0) + '请输入计算公式(输入q退出):')
            print('--------------------第 {} 题--------------------'.format(r))
            tuichu(shuru)
            answer = input('请输入你的答案(输入q退出) :')
            tuichu(answer)
            answer = float(answer)
            jieguo = eval(shuru)
            if math.isclose(jieguo, answer):
                print("结果正确 !")
                r = r + 1
            else:
                print("结果错误, 正确结果为:", jieguo)
                r = r + 1
            huoqu = input("还要继续检查吗？输入q退出,输入其他字母或数字继续:")
            tuichu(huoqu)
        except:
            print(Fore.RGB(255, 99, 71) + '输入有误')
            print(Fore.RGB(255, 165, 0) + '')


if __name__ == '__main__':
    check()
