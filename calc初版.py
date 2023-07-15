def JiSuanChuBan():
    print("这是一个可以计算的程序")
    while True:
        huoqu = input("请输入计算的符号,如+,-,*,/(输入q退出):")
        if huoqu == 'q':
            print("已退出")
            break
        elif huoqu == '+':
            shuzi_plus1_str = input("请输入第一个加数(输入q退出):")
            if shuzi_plus1_str == 'q':
                print("已退出")
                break
            shuzi_plus2_str = input("请输入第二个加数(输入q退出):")
            if shuzi_plus2_str == 'q':
                print("已退出")
                break
            try:
                shuzi1 = float(shuzi_plus1_str)
                shuzi2 = float(shuzi_plus2_str)
                jieguo = shuzi1 + shuzi2
                print("结果为:", jieguo)
            except:
                print("输入有误")
        elif huoqu == '-':
            shuzi_minus1_str = input("请输入第一个被减数(输入q退出):")
            if shuzi_minus1_str == 'q':
                print("已退出")
                break
            shuzi_minus2_str = input("请输入第二个减数(输入q退出):")
            if shuzi_minus2_str == 'q':
                print("已退出")
                break
            try:
                shuzi1 = float(shuzi_minus1_str)
                shuzi2 = float(shuzi_minus2_str)
                jieguo = shuzi1 - shuzi2
                print("结果为:", jieguo)
            except:
                print("输入有误")
        elif huoqu == '*':
            shuzi_mult1_str = input("请输入第一个乘数(输入q退出):")
            if shuzi_mult1_str == 'q':
                print("已退出")
                break
            shuzi_mult2_str = input("请输入第二个乘数(输入q退出):")
            if shuzi_mult2_str == 'q':
                print("已退出")
                break
            try:
                shuzi1 = float(shuzi_mult1_str)
                shuzi2 = float(shuzi_mult2_str)
                jieguo = shuzi1 * shuzi2
                print("结果为:", jieguo)
            except:
                print("输入有误")
        elif huoqu == '/':
            shuzi_div1_str = input("请输入第一个被除数(输入q退出):")
            if shuzi_div1_str == 'q':
                print("已退出")
                break
            shuzi_div2_str = input("请输入第二个除数(输入q退出):")
            if shuzi_div2_str == 'q':
                print("已退出")
                break
            try:
                shuzi1 = float(shuzi_div1_str)
                shuzi2 = float(shuzi_div2_str)
                jieguo = shuzi1 / shuzi2
                print("结果为:", jieguo)
            except:
                print("输入有误")
        elif huoqu != '+' or huoqu != '-' or huoqu != '*' or huoqu != '/' or huoqu != 'q':
            print("这是一个无效的字符")


if __name__ == '__main__':
    JiSuanChuBan()
