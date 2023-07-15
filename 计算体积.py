def tiJi():
    print("现在一个可以计算正方体体积、长方体体积、圆柱体的体积和球体积的程序")
    while True:
        huoqu = input("输入1计算正方体体积，输入2计算长方体体积，输入3计切面圆柱体体积，输入4计算球体积，输入q退出:")
        if huoqu == 'q':
            print("已退出")
            break
        if huoqu == '1':
            bianchang_str = input("请输入正方体的边长(输入q退出):")
            if bianchang_str == 'q':
                print("已退出")
                break
            try:
                bianchang = float(bianchang_str)
                tj = bianchang * bianchang * bianchang
                print("正方体体积为:", tj)
            except:
                print("输入有误")
        if huoqu == '2':
            chang_str = input("请输入长方体的长度(输入q退出):")
            if chang_str == 'q':
                print("已退出")
                break
            kuan_str = input("请输入长方体的宽度(输入q退出):")
            if kuan_str == 'q':
                print("已退出")
                break
            gao_str = input("请输入长方体的高度(输入q退出):")
            if gao_str == 'q':
                print("已退出")
                break
            try:
                chang = float(chang_str)
                kuan = float(kuan_str)
                gao = float(gao_str)
                tij = chang * kuan * gao
                print("长方体体积为:", tij)
            except:
                print("输入有误")
        if huoqu == '3':
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
        if huoqu == '4':
            pi = 3.14
            banjin_str = input("请输入球的半径(输入q退出)：")
            if banjin_str == 'q':
                print("已退出")
                break
            try:
                banjin = float(banjin_str)
                tj = (4 / 3) * pi * banjin * banjin * banjin
                print("球的体积为:", tj)
            except:
                print("输入错误")


if __name__ == '__main__':
    tiJi()
