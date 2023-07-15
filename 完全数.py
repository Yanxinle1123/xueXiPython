def QiuWanQuanShu():
    print("现在是一个可以求完全数的程序")
    while True:
        lower_str = input("请输入范围最小数(输入q退出):")
        if lower_str == 'q':
            print("已退出")
            break
        upper_str = input("请输入范围最大数(输入q退出):")
        if upper_str == 'q':
            print("已退出")
            break
        try:
            lower = int(lower_str)
            upper = int(upper_str)
            print(str(lower) + "到" + str(upper) + "范围的完全数有:")
            for i in range(lower, upper + 1):
                s = 0
                for j in range(1, i):
                    if i % j == 0:
                        s += j
                if s == i:
                    print(i)
        except:
            print("输入有误")


if __name__ == '__main__':
    QiuWanQuanShu()
