import random

from colored import Fore

from comm.common import print_orange, print_purple, print_green, input_yellow2, print_red, print_blue

list = ['word', 'print', 'snick', 'other', 'game', 'white', 'milk', 'future', 'want', 'pilot', 'orange', 'yellow',
        'usually', 'both', 'become', 'grapefruit', 'teach', 'fruit', 'bike', 'station', 'underground', 'hour',
        'take', 'letter', 'always', 'lake', 'beach', 'enjoy', 'sunshine', 'sun', 'year', 'know', 'outing', 'hill',
        'find', 'diamond', 'room', 'life', 'their', 'bedroom', 'kitchen', 'think', 'hole', 'funny', 'hat',
        'interesting', 'never', 'favourite', 'apple', 'pear', 'pack', 'peach', 'strawberry', 'papaya', 'answer',
        'robot', 'bilberry', 'berry', 'core', 'ginkgo', 'tissue', 'chestnut', 'hickory', 'hello', 'foot', 'car', 'fun',
        'tea', 'guess', 'you', 'what', 'name', 'python', 'goodbye', 'hi', 'if', 'break', 'rainbow', 'blue', 'red',
        'green', 'city', 'number', 'list', 'map', 'hot', 'black', 'juice', 'in', 'on', 'under', 'lunch', 'pink',
        'anteater', 'chat', 'work', 'yes', 'duck', 'translate', 'turtle', 'maths', 'mineral', 'iron', 'stone',
        'uranium', 'coal', 'gold', 'hematite', 'calcite', 'amethyst', 'marble', 'alloy', 'magnetite', 'pyrite',
        'sulfur', 'emotional', 'ammonite', 'crystal', 'fluorite', 'mica', 'saponite', 'polybasic', 'plant', 'hydrangea',
        'lily', 'bamboo', 'cornflower', 'wintersweet', 'rose', 'pumpkin', 'cactus', 'cherry', 'agave', 'reed', 'tomato',
        'potato', 'mango', 'program']


def word_game2():
    print_orange('欢迎来到单词游戏2 !')
    e = 1
    error = 0
    correct = 0
    while True:
        old_word = random.choice(list)
        length = len(old_word) - 1
        empty = random.randint(0, length)
        new_word = old_word[:empty] + '( )' + old_word[empty + 1:]
        answer = old_word[empty:empty + 1]
        print_purple('--------------------------第 {} 题--------------------------'.format(e))
        print_green(new_word)
        obtain = input_yellow2('请填写括号里的字母(输入quit退出): ')
        if obtain == 'quit':
            print_orange('一共玩了 {} 题'.format(e - 1))
            print_red('一共错了 {} 题'.format(error))
            print_blue('一共对了 {} 题'.format(correct))
            break
        elif obtain == answer:
            print_blue('回答正确 !')
            correct = correct + 1
            e = e + 1
        else:
            print_red('回答错误, 答案是' + Fore.RGB(238, 187, 144) + answer)
            error = error + 1
            e = e + 1


if __name__ == '__main__':
    word_game2()
