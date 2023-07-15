def stone():
    import random

    print("欢迎来到石头剪刀布游戏！(输入tc退出)")
    options = ["石头", "剪刀", "布"]
    victory_cases = {
        "石头": "剪刀",
        "剪刀": "布",
        "布": "石头"
    }
    choice_map = {
        "1": "石头",
        "2": "剪刀",
        "3": "布",
        "石头": "石头",
        "剪刀": "剪刀",
        "布": "布"
    }
    while True:
        is_quit = input("现在，新的一局开始了！(是否要退出？输入tc退出，输入其他继续)")
        if is_quit == 'tc' or is_quit == 'tuichu' or is_quit == '退出':
            print("已退出石头剪刀布游戏")
            break
        if is_quit == 'QiangZhiTuiChu' or is_quit == '强制退出':
            break
        player_score = 0
        computer_score = 0
        for i in range(1, 6):
            print("第%d轮：" % i)
            computer_choice = random.choice(options)
            player_choice_key = input("请选择：1=石头、2=剪刀、3=布\n")
            if player_choice_key == 'q':
                is_quit = 'q'
                break

            player_choice = ""
            if player_choice_key in choice_map:
                player_choice = choice_map[player_choice_key]

            while player_choice not in options:
                player_choice_key = input("你的选择有误，请重新选择：1=石头、2=剪刀、3=布\n")
                if player_choice_key == 'q':
                    is_quit = 'q'
                    break

                if player_choice_key in choice_map:
                    player_choice = choice_map[player_choice_key]

            if is_quit == 'q':
                print("已退出石头剪刀布游戏")
                break

            print("电脑选择了：%s" % computer_choice)
            if player_choice == computer_choice:
                print("本轮平局")
            elif victory_cases[player_choice] == computer_choice:
                print("恭喜你！你本轮赢了！")
                player_score += 1
            else:
                print("很遗憾，你本轮输了")
                computer_score += 1

        if is_quit == 'q':
            print("已退出石头剪刀布游戏")
            break

        print("游戏结束，你的得分为%d，电脑得分为%d" % (player_score, computer_score))
        if player_score == computer_score:
            print("本局平局")
        elif player_score > computer_score:
            print("恭喜你，你胜利了！")
        else:
            print("很遗憾，你输了")


if __name__ == '__main__':
    stone()
