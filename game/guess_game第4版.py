import random
import sys


def produce_guess_number(mix, max, info=False):
    random_number = random.randint(int(mix), int(max))
    if info:
        print(random_number)
    return random_number


def judge_guess_number(random_number, guess_number):
    if random_number > guess_number:
        return 'big', random_number - guess_number
    elif random_number < guess_number:
        return 'small', guess_number - random_number
    elif random_number == guess_number:
        return 'equal', True


def start_game():
    print('这是一个猜数游戏')
    print('我们会让你猜一个1~10之内的数字')
    while True:
        random_number = produce_guess_number(1, 10, info=True)
        while True:
            guess_number = input('请输入你猜的数字(输入q退出): ')
            if guess_number == 'q':
                print('游戏退出')
                sys.exit(0)
            result_one, result_two = judge_guess_number(random_number, int(guess_number))
            if result_one == 'big':
                if result_two >= 5:
                    print('你猜的数字大了')
                elif result_two <= 4:
                    print('你猜的数字离正确结果很近了')
            elif result_one == 'small':
                if result_two >= 5:
                    print('你猜的数字小了')
                elif result_two <= 4:
                    print('你猜的数字离正确结果很近了')
            elif result_one == 'equal':
                print('恭喜你猜对了')
                print('再玩一局吧')


if __name__ == '__main__':
    start_game()
    sys.exit(0)
