import threading


def input_with_timeout(prompt, timeout=5):
    print(prompt, end=" ", flush=True)
    result = []

    def timed_input(result):
        result.append(input())

    timer = threading.Timer(timeout, lambda: None)
    timer.start()

    input_thread = threading.Thread(target=timed_input, args=(result,))
    input_thread.start()
    input_thread.join(timeout)

    timer.cancel()

    return result[0] if result else None


try:
    output = input_with_timeout("请输入:")
    if output:
        print("你的输入是:", output)
    else:
        print("抱歉,时间已用完!")
except KeyboardInterrupt:
    print("\n程序被中断!")
finally:
    threading.Timer(0, lambda: None).start()  # 确保所有线程正确退出
