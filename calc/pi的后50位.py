import mpmath


def pi50wei():
    mpmath.mp.dps = 50  # 设置精度为50位
    pi = mpmath.pi  # 获取圆周率的值
    print(pi)


if __name__ == '__main__':
    pi50wei()
