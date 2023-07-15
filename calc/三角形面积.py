def SanJiaoXingMianJi():
    print("这是一个可以计算三角形面积的程序")
    while True:
        di_str = input("请输入三角形底的长度(输入q或Q退出)：")
        if di_str == 'q' or di_str == 'Q':
            print("已退出")
            break
        gao_str = input("请输入三角形高的高度(输入q或Q退出)：")
        if gao_str == 'q' or gao_str == 'Q':
            print("已退出")
            break
        try:
            di = float(di_str)
            gao = float(gao_str)
            mianji = di * gao / 2
            print("三角形面积为:", mianji)
        except:
            print("输入有误")


if __name__ == '__main__':
    SanJiaoXingMianJi()
