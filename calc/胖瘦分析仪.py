def pang_shou_fen_xi_yi():
    print('这是一个可以分析胖瘦的程序')
    while True:
        try:
            weight = input('请输入体重(公斤,输入q退出): ')
            if weight == 'q' or weight == 'Q':
                print('已退出')
                break
            weight = eval(weight)
            height = eval(input('请输入身高(米): '))
            bmi = weight / pow(height, 2)
            print('BMI 值为:', bmi)
            guoji = ''
            guonei = ''
            if bmi < 18.5:
                guoji = '偏瘦'
                guonei = '偏瘦'
                print("在国际属于: {0}, 在国外属于: {1}".format(guoji, guonei))
            elif 18.5 <= bmi <= 23.9:
                guoji = '正常'
                guonei = '正常'
                print("在国际属于: {0}, 在国外属于: {1}".format(guoji, guonei))
            elif 24.0 <= bmi <= 24.9:
                guoji = '正常'
                guonei = '偏胖'
                print("在国际属于: {0}, 在国外属于: {1}".format(guoji, guonei))
            elif 25.0 <= bmi <= 26.9:
                guoji = '偏胖'
                guonei = '偏胖'
                print("在国际属于: {0}, 在国外属于: {1}".format(guoji, guonei))
            elif 27.0 <= bmi <= 29.9:
                guoji = '偏胖'
                guonei = '肥胖'
                print("在国际属于: {0}, 在国外属于: {1}".format(guoji, guonei))
            elif 30.0 <= bmi <= 34.9:
                guoji = '肥胖'
                guonei = '重度肥胖'
                print('在国际属于: {0}, 在国外属于: {1}'.format(guoji, guonei))
            elif 35.0 <= bmi <= 39.9:
                guoji = '重度肥胖'
                guonei = '重度肥胖'
                print('在国际属于: {0}, 在国外属于: {1}'.format(guoji, guonei))
            else:
                print('极重度肥胖')
        except:
            print('输入有误')


if __name__ == '__main__':
    pang_shou_fen_xi_yi()
