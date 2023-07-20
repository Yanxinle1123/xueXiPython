import calendar


def chaxun():
    while True:
        try:
            print('* * * * * 查 询 器 * * * * *')
            print('          1.母亲节')
            print('          2.父亲节')
            huoqu = input('请选择(输入数字, 输入q退出):')
            if huoqu == 'q':
                print('已退出')
                break
            elif huoqu == '1':
                year = int(input('请输入年份:'))
                list = calendar.monthcalendar(year, 5)
                week = list[1]
                monther_day = week[6]
                print('********** {} 年的母亲节**********'.format(year))
                print('         5 月 {} 号, 星期日'.format(monther_day))
                print('\n**********参考月份**********\n')
                print(calendar.month(year, 5))
            elif huoqu == '2':
                year = int(input('请输入年份:'))
                list = calendar.monthcalendar(year, 6)
                week = list[2]
                father_day = week[6]
                print('********** {} 年的父亲节**********'.format(year))
                print('         6 月 {} 号, 星期日'.format(father_day))
                print('\n**********参考月份**********\n')
                print(calendar.month(year, 6))
            else:
                print('输入有误')
        except:
            print('输入有误')


if __name__ == '__main__':
    chaxun()
