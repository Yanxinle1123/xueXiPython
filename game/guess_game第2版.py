import random

from comm.common import tuichu


def tiShiFu(key):
    prefix = "---------"
    return (prefix + key + prefix)


def guess_game_ShengJiBan():
    number = random.randint(1, 100)
    print('现在是一个猜数游戏的升级版!')
    while True:
        huoqu_str = input('请输入一个1到100的数 (输入q退出) : ')
        tuichu(huoqu_str)
        try:
            huoqu = int(huoqu_str)
            if huoqu > number + 10:
                print(tiShiFu("太大了") + "这个数好大呀！加油，请继续猜\n")
            elif number + 10 >= huoqu > number:
                print(tiShiFu("接近了") + "在努力一点\n")
            elif number - 10 <= huoqu < number:
                print(tiShiFu("接近了") + "在努力一点\n")
            elif huoqu < number - 5:
                print(tiShiFu("太小了") + "这个数好小呀！加油，你一定可以猜中的\n")
            else:
                print("恭喜你！猜对了！新的一局开始了")
        except:
            print("输入有误")


if __name__ == '__main__':
    guess_game_ShengJiBan()
