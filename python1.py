def tree():
    while True:
        n_str = input("请输入行数(输入q退出)：")
        if n_str == 'q':
            print("已退出")
            break
        try:
            t = int(n_str)
            for i in range(1, t + 1):
                print("*" * i)
        except:
            print("输入错误")


if __name__ == '__main__':
    tree()
