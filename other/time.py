import time


def shijian():
    while True:
        current_time = time.time()  # 获取当前时间的时间戳
        local_time = time.localtime(current_time)  # 将时间戳转换为本地时间的结构化形
        hour = local_time.tm_hour  # 获取当前的小时
        minute = local_time.tm_min  # 获取当前的分钟
        second = local_time.tm_sec  # 获取当前的秒钟
        print("现在时间是：{}时{}分{}秒".format(hour, minute, second))


if __name__ == '__main__':
    shijian()
