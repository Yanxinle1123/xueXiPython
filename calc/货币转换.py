def huo_bi_zhuan_huan():
    print('这是一个可以转换货币的程序')
    while True:
        try:
            huoqu = input(
                '1.美元转人名币\n2.人民币转美元\n3.港币转人名币\n4.人名币转港币\n5.美元转港币\n6.港币转美元\n请选择转换方式(输入数字,输入q退出):')
            if huoqu == 'q' or huoqu == 'Q':
                print('已退出')
                break
            elif huoqu == '1':
                shuru = float(input('请输入美元:'))
                jieguo = shuru / 6.48
                print('对应的人名币为:', jieguo)
            elif huoqu == '2':
                shuru = float(input('请输入人名币:'))
                jieguo = shuru * 6.48
                print('对应的美元为:', jieguo)
            elif huoqu == '3':
                shuru = float(input('请输入港币:'))
                jieguo = shuru * 0.83
                print('对应的人名币为:', jieguo)
            elif huoqu == '4':
                shuru = float(input('请输入人名币:'))
                jieguo = shuru / 0.83
                print('对应的港币为:', jieguo)
            elif huoqu == '5':
                shuru = float(input('请输入美元:'))
                jieguo = shuru / 0.128
                print('对应的港币为:', jieguo)
            elif huoqu == '6':
                shuru = float(input('请输入港币:'))
                jieguo = shuru * 0.128
                print('对应的美元为:', jieguo)
            else:
                print(huoqu, '不是一个选择')
        except:
            print('输入有误')


if __name__ == '__main__':
    huo_bi_zhuan_huan()
