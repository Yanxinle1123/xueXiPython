def PanDuanRunNian():
    print("这是一个可以判断是否是润年的程序")
    while True:
        huoqu_str = input("请输入年份(输入q或Q退出):")
        if huoqu_str == "q" or huoqu_str == "Q":
            print("已退出")
            break
        try:
            huoqu = int(huoqu_str)
            year = huoqu
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print(huoqu_str, "年是润年")
            else:
                print(huoqu_str, "年不是润年")
        except:
            print(huoqu_str, "不是年份")


if __name__ == "__main__":
    PanDuanRunNian()
