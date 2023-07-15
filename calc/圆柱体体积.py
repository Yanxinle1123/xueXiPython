def yuanZhuTiTiJi():
    print("这是一个可以计算圆柱体体积的程序")
    while True:
        pi = 3.14
        banjing_str = input("请输入底面半径(输入q退出):")
        if banjing_str == 'q':
            print("已退出")
            break
        gao_str = input("请输入高(输入q退出):")
        if gao_str == 'q':
            print("已退出")
            break
        try:
            banjing = float(banjing_str)
            gao = float(gao_str)
            tj = pi * banjing * banjing * gao
            print("体积为:", tj)
        except:
            print("输入有误，请从输入一遍")


if __name__ == '__main__':
    yuanZhuTiTiJi()
