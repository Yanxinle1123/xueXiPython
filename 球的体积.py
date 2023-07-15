def qiuTiJi():
    print("这是一个可以计算球体积的程序")
    while True:
        pi = 3.14
        banjin_str = input("请输入球的半径(输入q退出)：")
        if banjin_str == 'q':
            print("已退出")
            break
        try:
            banjin = float(banjin_str)
            tj = (4 / 3) * pi * banjin * banjin * banjin
            print("球的体积为:", tj)
        except:
            print("输入错误")


if __name__ == '__main__':
    qiuTiJi()
