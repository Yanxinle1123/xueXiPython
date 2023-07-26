import platform
import socket

import psutil


def computer():
    ip = socket.gethostbyname("www.google.com")
    print(
        '------------------------------------------------------------电脑信息------------------------------------------------------------')
    print("操作系统名称: ", platform.system())
    print("操作系统版本: ", platform.release())
    print("操作系统详细版本: ", platform.version())
    print("硬件架构: ", platform.machine())
    print("处理器名称: ", platform.processor())
    print("操作系统位数: ", platform.architecture()[0])
    print("Python 版本: ", platform.python_version())
    print("Python 编译器: ", platform.python_compiler())
    print("Python 构建信息: ", platform.python_build())
    print("主机名称: ", socket.gethostname())
    print("本机 IP 地址: ", socket.gethostbyname(socket.gethostname()))
    print("CPU 使用率: ", psutil.cpu_percent())
    print("内存使用率: ", psutil.virtual_memory().percent)
    print("根目录磁盘使用率: ", psutil.disk_usage('/').percent)
    print("远程主机IP地址:", ip)
    print(
        '-------------------------------------------------------------------------------------------------------------------------------')


if __name__ == '__main__':
    computer()
