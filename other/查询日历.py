import calendar


def rili():
    while True:
        huoqu = input('请输入需要查询的年份(输入q退出) :')
        if huoqu == 'q':
            print('已退出')
            break
        try:
            huoqu = int(huoqu)
            year = calendar.calendar(huoqu)
            print(year)
        except:
            print('已退出')


if __name__ == '__main__':
    rili()
