import mpmath


def pi50wei():
    while True:
        huoqu = input('请输入位数(输入q退出):')
        if huoqu == 'q':
            print('已退出')
            break
        try:
            huoqu = int(huoqu)
            mpmath.mp.dps = huoqu + 1  # 设置精度为用户输入的值
            pi = mpmath.pi  # 获取圆周率的值
            print(pi)
        except:
            print('输入有误')


if __name__ == '__main__':
    pi50wei()
