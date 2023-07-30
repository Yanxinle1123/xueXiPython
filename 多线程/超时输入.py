import select
import sys


class TimeoutExpired(Exception):
    pass


def input_with_timeout(prompt, timeout=5):
    print(prompt, end=" ", flush=True)
    fds = [sys.stdin]
    result = []
    r, _, _ = select.select(fds, [], [], timeout)
    if not r:
        raise TimeoutExpired()

    input_str = sys.stdin.readline().rstrip()
    result.append(input_str)
    return result[0]


try:
    output = input_with_timeout("请输入：")
    print("你的输入是：", output)
except TimeoutExpired:
    print("\n时间用完，程序被终止！")
except KeyboardInterrupt:
    print("\n程序被中断！")
