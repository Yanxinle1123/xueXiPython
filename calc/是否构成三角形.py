def sanjiaoxing():
    print('现在是一个可以计算三条边是否构成三角形的程序')
    while True:
        a_str = input('请输入第一条边长度(输入q退出) :')
        if a_str == 'q':
            print('已退出')
            break
        b_str = input('请输入第二条边长度 :')
        c_str = input('请输入第三条边长度 :')
        try:
            a = float(a_str)
            b = float(b_str)
            c = float(c_str)
            if a + b > c and a + c > b and b + c > a:
                print('能构成三角形')
            else:
                print('不能构成三角形')
        except:
            print('输入有误')


if __name__ == '__main__':
    sanjiaoxing()
