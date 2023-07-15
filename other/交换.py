def JiaoHuanWeiZhi():
    print("这是一个可以交换两个汉字、数字或符号的程序")
    while True:
        huoqu1 = input("请输入第一个汉字、数字或符号(输入q退出):")
        if huoqu1 == 'q':
            print("已退出")
            break
        huoqu2 = input("请输入第二个汉字、数字或符号(输入q退出):")
        if huoqu2 == 'q':
            print("已退出")
            break
        print("交换前:")
        print("第一个汉字、数字或符号为", huoqu1)
        print("第二个汉字、数字或符号为", huoqu2)
        x = huoqu1
        huoqu1 = huoqu2
        huoqu2 = x
        print("交换后:")
        print("第一个汉字、数字或符号为", huoqu1)
        print("第二个汉字、数字或符号为", huoqu2)


if __name__ == '__main__':
    JiaoHuanWeiZhi()
