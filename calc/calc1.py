def calculator():
    print("现在是一个计算器")
    while True:
        equation = input("请输入计算公式,不能带有[]和{}(输入q退出) :")
        if equation == 'q':
            print("已退出计算器")
            break
        try:
            result = eval(equation)
            print('计算结果为: ', result)
        except:
            print("输入有误，请检查并重新输入。")


if __name__ == '__main__':
    calculator()
