import datetime
from datetime import datetime

today = datetime.now()
weekday = today.weekday()
if weekday == '0':
    day = '星期一'
elif weekday == '1':
    day = '星期二'
elif weekday == '2':
    day = '星期三'
elif weekday == '3':
    day = '星期四'
elif weekday == '4':
    day = '星期五'
elif weekday == '5':
    day = '星期六'
else:
    day = '星期天'


def shijian():
    now = datetime.now()
    print("{}年 {}月{}日 {} {}时{}分{}秒".format(now.year, now.month, now.day, day, now.hour, now.minute,
                                                 now.second))


if __name__ == '__main__':
    shijian()
