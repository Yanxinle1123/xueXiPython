def JunFen():
    while True:
        total = 0
        count = 0
        msg = 1
        while msg == 1:
            count += 1
            num = int(input("第" + str(count) + "次输入数字："))
            total += num
            msg = int(input("是否继续输入数字(继续请输入1，结束请输入0):"))
        print("一共输入", count, "次数字，", "总和为：", total, "平均值为：", total / count)


if __name__ == '__main__':
    JunFen()
