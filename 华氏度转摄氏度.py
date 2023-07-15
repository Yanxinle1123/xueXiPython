def HuaShiDuZhuanSheShiDuAndSheShiDuZhuanHuaShiDu():
    print("现在是一个可以把华氏度转成摄氏度\n也可以把摄氏度转成华氏度的程序")
    while True:
        try:
            print("----------转换方式----------\n1. 华氏度转摄氏度\n2. 摄氏度转华氏度")
            huoqu = input("请输入转换方式, 输入编号或文字(输入q退出):")
            if huoqu == 'q':
                print("已退出")
                break
            elif huoqu == '华氏度转摄氏度' or huoqu == '1':
                f = eval(input('请输入华氏度:'))
                c = (f - 32) / 1.8
                print("对应的摄氏度为:", c)
            elif huoqu == '摄氏度转华氏度' or huoqu == '2':
                c = eval(input('请输入摄氏度:'))
                f = 1.8 * c + 32
                print("对应的华氏度为:", f)
            else:
                print("输入有误")
        except:
            print("输入有误")


if __name__ == '__main__':
    HuaShiDuZhuanSheShiDuAndSheShiDuZhuanHuaShiDu()
