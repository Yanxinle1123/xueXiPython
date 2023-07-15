def mianj():
    print("现在一个可以计算三角形面积、正方形面积、长方形面积和圆面积的程序")
    while True:
        huoqu = input(
            "输入1计算三角形面积\n输入2计算正方形面积\n输入3计算长方形面积\n输入4计算圆的面积\n输入5计算梯形面积\n输入q退出:")
        if huoqu == 'q':
            print("已退出")
            break
        if huoqu == '1':
            di_str = input("请输入三角形底边的长度(输入q退出):")
            if di_str == 'q':
                print("已退出")
                break
            gao_str = input("请输入三角形高的高度(输入q退出):")
            if gao_str == 'q':
                print("已退出")
                break
            try:
                di = float(di_str)
                gao = float(gao_str)
                mj = di * gao / 2
                print("三角形的面积为:", mj)
            except:
                print("输入有误")
        if huoqu == '2':
            bianchang_str = input("请输入正方形的边长(输入q退出):")
            if bianchang_str == 'q':
                print("已退出")
                break
            try:
                bianchang = float(bianchang_str)
                mianj = bianchang * bianchang
                print("正方形的面积为:", mianj)
            except:
                print("输入有误")
        if huoqu == '3':
            chang_str = input("请输入长方形长的长度(输入q退出):")
            if chang_str == 'q':
                print("已退出")
                break
            kuan_str = input("请输入长方形宽的宽度(输入q退出):")
            if kuan_str == 'q':
                print("已退出")
                break
            try:
                chang = float(chang_str)
                kuan = float(kuan_str)
                mji = chang * kuan
                print("长方形的面积为:", mji)
            except:
                print("输入有误")
        if huoqu == '4':
            pi = 3.14
            banjing_str = input("请输入圆的半径(输入q退出):")
            if banjing_str == 'q':
                print("已退出")
                break
            try:
                banjing = float(banjing_str)
                mianji = pi * banjing * banjing
                print("圆的面积为:", mianji)
            except:
                print("输入有误")
        if huoqu == '5':
            shangdi_str = input("请输入梯形的上底(输入q退出):")
            if shangdi_str == 'q':
                print("已退出")
                break
            xiadi_str = input("请输入梯形的下底(输入q退出):")
            if xiadi_str == 'q':
                print("已退出")
                break
            gao_str = input("请输入梯形的高(输入q退出):")
            if gao_str == 'q':
                print("已退出")
                break
            try:
                shangdi = float(shangdi_str)
                xiadi = float(xiadi_str)
                gao = float(gao_str)
                mianji = (shangdi + xiadi) * gao / 2
                print("梯形的面积为:", mianji)
            except:
                print("输入有误")


if __name__ == '__main__':
    mianj()
