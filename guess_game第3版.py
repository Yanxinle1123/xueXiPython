import random


def guess_number_game():
    number = random.randint(1, 100)  # 生成1到100之间的随机整数
    print("猜数字游戏开始！")
    print("你有10次机会猜测数字。输入 q 退出游戏。")

    attempts = 0
    while attempts < 10:
        guess = input("请输入一个数字：")

        if guess.lower() == "q":
            print("游戏结束。正确的数字是", number)
            return

        try:
            guess = int(guess)
        except ValueError:
            print("无效的输入，请输入一个数字。")
            continue

        attempts += 1

        if guess < number:
            print("猜小了！")
        elif guess > number:
            print("猜大了！")
        else:
            print("恭喜你猜对了！")

    print("次数已用尽。正确的数字是", number)


guess_number_game()
