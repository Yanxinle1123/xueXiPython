import mpmath


def pi50wei():
    while True:
        huoqu = input('请输入位数(输入q退出, 范围 6-1000 ):')
        if huoqu == 'q':
            print('已退出')
            break
        try:
            huoqu = int(huoqu)
            if huoqu < 6 or huoqu > 1000:  # 检查位数是否在有效范围内
                print('位数应该在 6-1000 的范围内')
            else:
                mpmath.mp.dps = huoqu  # 设置精度为用户输入的值
                pi = mpmath.pi  # 获取圆周率的值
                print(pi)
        except:
            print('输入有误')


if __name__ == '__main__':
    pi50wei()
