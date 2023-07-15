from datetime import date


def daycalc():
    print('这是一个可以计算当前日期距离指定日期有多少天的程序')
    while True:
        try:
            now_date = date.today()
            year_str = input('请输入年(输入q退出):')
            if year_str == 'q' or year_str == 'Q':
                print("已退出")
                break
            year = int(year_str)
            month = int(input('请输入月:'))
            day = int(input('请输入日:'))
            new_date = date(year, month, day)
            if now_date >= new_date:
                print('\n*****当前日期为:', now_date, '*****')
                print('-----距离  {} 年 {} 月 {} 日----'.format(year, month, day))
                print('已经过去:', (now_date - new_date).days, '天\n')
            else:
                print('\n*****当前日期为:', now_date, '*****')
                print('-----距离  {} 年 {} 月 {} 日----'.format(year, month, day))
                print('还差:', (new_date - now_date).days, '天\n')
        except:
            print('输入有误')


if __name__ == '__main__':
    daycalc()
