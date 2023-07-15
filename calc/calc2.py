def jicuanqi():
    print("这里是一个计算程序")
    while True:
        huoqu = input("请输入计算公式 (输入t退出): ")
        if huoqu == 't':
            print("已退出计算器")
            break
        try:
            jieguo = eval(huoqu)
            print('计算结果为:', jieguo)
        except:
            print("输入错误")


if __name__ == '__main__':
    jicuanqi()
