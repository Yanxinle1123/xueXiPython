def yuanZhouChang():
    print("这是一个可以计算圆的周长的程序")
    while True:
        pi = 3.14
        banjing_str = input("请输入圆的半径(输入q退出):")
        if banjing_str == 'q':
            print("已退出")
            break
        try:
            banjing = float(banjing_str)
            zhouchang = pi * 2 * banjing
            print("周长为:", zhouchang)
        except:
            print("输入有误")


if __name__ == '__main__':
    yuanZhouChang()
