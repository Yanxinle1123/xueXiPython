import time


def NianNingJiSuanQi():
    print("现在一个年龄计算器")
    while True:
        try:
            print(
                "----------计算方式----------\n1. 计算秒龄\n2. 计算分龄\n3. 计算时龄\n4. 计算天龄\n5. 计算周龄\n6. 计算月龄\n7. 计算年龄")
            way = input("请输入计算方式, 输入编号或文字(输入q退出):")
            if way == 'q':
                print("已退出")
                break
            date = input("请输入出生日期(如 2005-01-20 ):")
            now = time.time()
            live = time.mktime(time.strptime(date, '%Y-%m-%d'))
            second = now - live
            if way == '1' or way == '计算秒龄':
                print("你已经活了", second, "秒")
            elif way == '2' or way == '计算分龄':
                minute = int(second / 60)
                print("你已经活了", minute, "分")
            elif way == '3' or way == '计算时龄':
                hour = int(second / 3600)
                print("你已经活了", hour, "时")
            elif way == '4' or way == '计算天龄':
                day = int(second / 3600 / 24)
                print("你已经活了", day, "天")
            elif way == '5' or way == '计算周龄':
                week = int(second / 3600 / 24 / 7)
                print("你已经活了", week, "周")
            elif way == '6' or way == '计算月龄':
                month = int(second / 3600 / 24 / 31)
                print("你已经活了", month, "月")
            elif way == '7' or way == '计算年龄':
                year = round(second / 3600 / 24 / 365, 2)
                print("你已经活了", year, "年")
            else:
                print("输入有误")
        except:
            print("输入有误")


if __name__ == '__main__':
    NianNingJiSuanQi()
