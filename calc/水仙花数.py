def QiuShuiXianHuaShu():
    print("现在是一个可以求水仙花数的程序")
    while True:
        number_str = input("请输入任意三位数的正整数(输入q退出):")
        if number_str == 'q':
            print("已退出")
            break
        try:
            number = int(number_str)
            if number < 100 or number > 999:
                print("水仙花数是一个三位数的正整数")
            ge = number % 10
            shi = number // 10 % 10
            bai = number // 100
            zuizhongshu = ge ** 3 + shi ** 3 + bai ** 3
            if number == zuizhongshu:
                print(number, "是水仙花数")
            else:
                print(number, "不是水仙花数")
        except:
            print("输入有误")


if __name__ == '__main__':
    QiuShuiXianHuaShu()
