def jisuan():
    print(" ——————————————————")
    print("|这是一个高级计算程序 |")
    print(" ——————————————————")
    print("   作者：颜心乐")
    print("用法举例")
    print("9+7")
    print("5^8")
    print("10/2")
    print("456757-575")
    print("7*(90+89)+1")
    print("8**9")
    print("现在开始了！")
    i = 0
    while i < 10:
        print("----", end='')
        i = i + 1
    print()
    while True:
        huoqu_str = input("请输入一个计算公式(输入q或x退出)：")
        if huoqu_str == 'q' or huoqu_str == 'x':
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
