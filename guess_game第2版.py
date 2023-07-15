import random


def guess_game_ShengJiBan():
    number = random.randint(1, 100)
    print('现在是一个猜数游戏的升级版!')
    while True:
        huoqu_str = input('请输入一个1到100的数 (输入q退出) : ')
        if huoqu_str == 'q':
            print("已退出猜数游戏")
            break
        try:
            huoqu = int(huoqu_str)
            if huoqu > number + 10:
                print("\n---------太大了---------\n这个数好大呀！加油，请继续猜\n")
            elif number + 10 >= huoqu > number:
                print("\n---------接近了---------\n在努力一点\n")
            elif number - 10 <= huoqu < number:
                print("\n---------接近了---------\n在努力一点\n")
            elif huoqu < number - 5:
                print("\n---------太小了---------\n这个数好小呀！加油，你一定可以猜中的\n")
            else:
                print("恭喜你！猜对了！新的一局开始了")
        except:
            print("输入有误")


if __name__ == '__main__':
    guess_game_ShengJiBan()
