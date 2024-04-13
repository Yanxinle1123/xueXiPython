print("请输入两个数字, 程序将计算他们的商")
print("输入 q 可以退出")

while True:
    first_number = input("\n请输入第一个数字:")
    if first_number == 'q':
        break
    second_number = input("请输入第二个数字:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("除数不能为零")
    else:
        print(f"这两个数的商为 {answer}")
