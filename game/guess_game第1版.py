import random

from comm.common import tuichu


def guess_game():
    number = random.randint(0, 9)
    print('现在是一个猜数游戏!')
    while True:
        guess_str = input('请输入一个数 (输入q退出) : ')
        tuichu(guess_str)
        try:
            guess = int(guess_str)
            if guess == number:
                print("恭喜你！猜对了！新的一局开始了")
                number = random.randint(0, 9)
            elif guess < number:
                print("这个数小了")
            else:
                print("这个数大了")
        except:
            print("输入有误")


if __name__ == '__main__':
    guess_game()
