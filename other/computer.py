import platform

print(
    '-------------------------------------------------------电脑信息-------------------------------------------------------')
print("操作系统名称：", platform.system())
print("操作系统版本：", platform.release())
print("操作系统详细版本：", platform.version())
print("硬件架构：", platform.machine())
print("处理器名称：", platform.processor())
print("操作系统位数：", platform.architecture()[0])
print("Python 版本：", platform.python_version())
print("Python 编译器：", platform.python_compiler())
print("Python 构建信息：", platform.python_build())
print(
    '---------------------------------------------------------------------------------------------------------------------')
