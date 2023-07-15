def zhengFangti():
    print("这是一个可以计算正方体体积的程序")
    while True:
        bc_str = input("请输入正方体的边长(输入q退出):")
        if bc_str == 'q':
            print("已退出")
            break
        gao_str = input("请输入正方体的高(输入q退出):")
        if gao_str == 'q':
            print("已退出")
            break
        try:
            bc = float(bc_str)
            gao = float(gao_str)
            tj = bc * bc * gao
            print("正方体的体积为:", tj)
        except:
            print("输入有误")


if __name__ == '__main__':
    zhengFangti()
