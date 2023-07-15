import os

while True:
    # 获取用户输入的命令
    command = input("$ ")

    # 如果用户输入exit，则退出终端
    if command == "exit":
        break

    # 执行命令并输出结果
    result = os.popen(command).read()
    print(result)
