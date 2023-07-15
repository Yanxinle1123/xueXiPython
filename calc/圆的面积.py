def yuanMianJi():
    print("这是一个可以计算圆面积的程序")
    while True:
        pi = 3.14
        bj_str = input("请输入圆的半径(输入q退出)：")
        if bj_str == 'q':
            print("已退出")
            break
        try:
            bj = float(bj_str)
            mj = pi * bj * bj
            print("圆面积为:", mj)
        except:
            print("输入有误")


if __name__ == '__main__':
    yuanMianJi()
