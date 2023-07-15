import math


def JianChaSuanShuTi():
    print("这是一个可以检查你的算数结果是否正确的程序")
    while True:
        huoqu1 = input("请输入要检查的算术题的运算公式(输入q退出):")
        if huoqu1 == 'q':
            print("已退出")
            break
        huoqu2_str = input("请输入你计算出来的结果(输入q退出):")
        if huoqu2_str == 'q':
            print("已退出")
            break
        try:
            huoqu2 = float(huoqu2_str)
            jieguo = eval(huoqu1)
            if math.isclose(jieguo, huoqu2):
                print("结果正确!")
            else:
                print("结果错误, 正确结果为:", jieguo)
        except:
            print("输入有误")
        huoqu3 = input("还要继续检查吗？输入1退出,输入其他字母或数字继续:")
        if huoqu3 == '1':
            print("已退出")
            break


if __name__ == '__main__':
    JianChaSuanShuTi()
