from datetime import datetime


def shijian():
    now = datetime.now()
    print("现在是 {} 年 {} 月 {} 日 {} 时 {} 分 {} 秒".format(now.year, now.month, now.day, now.hour, now.minute,
                                                              now.second))


if __name__ == '__main__':
    shijian()
