def jisuan():
    print("现在是一个计算器")
    i = 0
    while i < 10:
        print("----", end='')
        i = i + 1
    print()
    while True:
        huoqu_str = input("请输入计算公式,不能带有[]和{}(输入q退出) :")
        if huoqu_str == 'q':
            print("已退出计算器")
            break
        try:
            if huoqu_str.find("^") > -1:
                huoqu = huoqu_str.replace("^", "**")
            else:
                huoqu = huoqu_str

            jieguo = eval(huoqu)
            print('计算结果为:', jieguo)
        except:
            print("输入错误，请检查并重新输入：")


if __name__ == '__main__':
    jisuan()
