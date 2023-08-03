from comm.common import red_print, input_yellow2, orange_print

list = []


def palindrome():
    orange_print('这是一个可以判断三个字符正着读和反着读是否一样的程序')
    while True:
        try:
            list.clear()
            huoqu = input_yellow2('请输入三个字符(输入q退出):')
            if huoqu == 'q':
                orange_print('已退出')
                break
            list.append(huoqu)
            word = list[0]
            ge = word[2]
            bai = word[0]
            if ge == bai:
                print(huoqu, '正着读和反着读一样')
            else:
                print(huoqu, '正着读和反着读不一样')
        except:
            red_print('字符个数不是三')


if __name__ == '__main__':
    palindrome()
