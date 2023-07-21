from colorama import Fore

list = []


def junfen():
    print(Fore.CYAN + '这是一个可以计算平均数的程序')
    print(Fore.MAGENTA + '')
    e = 1
    while True:
        try:
            print("---------------第 {} 次---------------".format(e))
            huoqu_str = input('请输入数字的数量(输入q退出):')
            equation = input('是否要去掉最高数和最低数(y / 其他字符):')
            if huoqu_str == 'q':
                print('已退出')
                break
            huoqu = int(huoqu_str)
            zuihouhuoqu = huoqu + 1
            for i in range(1, zuihouhuoqu):
                print('请输入第', i, '个数:', end='')
                score = float(input())
                list.append(score)
            zonghe = sum(list)
            jieguo = zonghe / huoqu
            print('平均值为:', jieguo)
            e = e + 1
            if equation == 'y':
                huoqu = int(huoqu_str)
                zuihouhuoqu = huoqu + 1
                for i in range(1, zuihouhuoqu):
                    print('请输入第', i, '个数:', end='')
                    score = float(input())
                    list.append(score)
                zuidifen = min(list)
                zuigaofen = max(list)
                print('去掉最低分:', zuidifen)
                list.remove(min)
                print('去掉最高分:', zuigaofen)
                list.remove(max)
                zonghe = sum(list)
                jieguo = zonghe / huoqu
                print('平均值为:', jieguo)
                e = e + 1
        except:
            print(Fore.RED + '输入有误')
            print(Fore.MAGENTA + '')


if __name__ == '__main__':
    junfen()
