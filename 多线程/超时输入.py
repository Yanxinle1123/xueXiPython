import threading


def input_with_timeout(prompt, timeout):
    print(prompt, end=" ", flush=True)
    input = []

    def timed_input(input):
        try:
            input.append(input(""))
        except:
            pass

    t = threading.Thread(target=timed_input, args=(input,))
    t.start()
    timer = threading.Timer(timeout, stop_thread, args=[t])
    timer.start()
    t.join(timeout)
    if input:
        return input[0]
    else:
        return None


def stop_thread(thread):
    thread.cancel()


try:
    output = input_with_timeout("请输入:", 10)
    if output:
        print("你的输入是:", output)
    else:
        print("抱歉,时间已用完!")
except KeyboardInterrupt:
    print("\n程序被中断!")
finally:
    threading.Timer(0, lambda: None).start()  # 确保所有线程正确退出
