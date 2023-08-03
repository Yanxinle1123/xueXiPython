import random

from colored import Fore

from comm.common import print_orange, print_purple, print_green, input_yellow2, print_red, print_blue, input_green

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
list2 = ['word', 'print', 'snick', 'other', 'game', 'white', 'milk', 'future', 'want', 'pilot', 'orange', 'yellow',
         'usually', 'both', 'become', 'grapefruit', 'teach', 'fruit', 'bike', 'station', 'underground', 'hour', 'take',
         'letter', 'always', 'lake', 'beach', 'enjoy', 'sunshine', 'year', 'know', 'outing', 'hill', 'find', 'diamond',
         'room', 'life', 'their', 'bedroom', 'kitchen', 'think', 'hole', 'funny', 'interesting', 'never', 'favourite',
         'apple', 'pear', 'pack', 'peach', 'strawberry', 'papaya', 'answer', 'robot', 'bilberry', 'berry', 'core',
         'ginkgo', 'tissue', 'chestnut', 'hickory', 'hello', 'foot', 'tea', 'guess', 'you', 'what', 'name', 'python',
         'goodbye', 'break', 'rainbow', 'blue', 'green', 'city', 'number', 'list', 'map', 'hot', 'black', 'juice',
         'under', 'lunch', 'pink', 'anteater', 'chat', 'work', 'yes', 'duck', 'translate', 'turtle', 'maths', 'mineral',
         'iron', 'stone', 'uranium', 'coal', 'gold', 'hematite', 'calcite', 'amethyst', 'marble', 'alloy', 'magnetite',
         'pyrite', 'sulfur', 'emotional', 'ammonite', 'crystal', 'fluorite', 'mica', 'saponite', 'polybasic', 'plant',
         'hydrangea', 'lily', 'bamboo', 'cornflower', 'wintersweet', 'rose', 'pumpkin', 'cactus', 'cherry', 'agave',
         'reed', 'tomato', 'potato', 'mango', 'program']


def word_game2():
    print_orange('欢迎来到单词游戏2 !')
    while True:
        obtain1 = input_green('1.低等\n'
                              '2.中等\n'
                              '3.高等\n'
                              '请选择难度等级(输入q退出, 输入数字): ')
        if obtain1 == 'q':
            print_orange('已退出')
            break
        elif obtain1 == '1':
            e = 1
            error = 0
            correct = 0
            while True:
                old_word = random.choice(list)
                length = len(old_word) - 1
                empty = random.randint(0, length)
                new_word = old_word[:empty] + '( )' + old_word[empty + 1:]
                answer = old_word[empty:empty + 1]
                print_purple("--------------------------第 {} 题--------------------------".format(e))
                print_green(new_word)
                obtain = input_yellow2('请填写括号里的字母(输入quit退出): ')
                if obtain == 'quit':
                    print_orange("一共玩了 {} 题".format(e - 1))
                    print_red("一共错了 {} 题".format(error))
                    print_blue("一共对了 {} 题".format(correct))
                    break
                elif obtain == answer:
                    print_blue("回答正确 !")
                    correct = correct + 1
                    e = e + 1
                else:
                    print_red('回答错误, 答案是' + Fore.RGB(238, 187, 144) + answer)
                    error = error + 1
                    e = e + 1
        elif obtain1 == '2':
            e = 1
            error = 0
            correct = 0
            while True:
                old_word = random.choice(list2)
                empty = random.randint(0, 3)
                empty2 = random.randint(0, 3)
                if empty == empty2:
                    while True:
                        empty2 = random.randint(0, 3)
                        if empty != empty2:
                            break
                if empty > empty2:
                    temp = empty
                    empty = empty2
                    empty2 = temp
                new_word = old_word[:empty] + '( )' + old_word[empty + 1:empty2] + '( )' + old_word[empty2 + 1:]
                answer1 = old_word[empty]
                answer2 = old_word[empty2]
                print_purple('--------------------------第 {} 题--------------------------'.format(e))
                print_green(new_word)
                obtain1 = input_yellow2('请填写第一个括号里的字母(输入quit退出): ')
                if obtain1 == 'quit':
                    print_orange('一共玩了 {} 题'.format(e - 1))
                    print_red('一共错了 {} 题'.format(error))
                    print_blue('一共对了 {} 题'.format(correct))
                    break
                obtain2 = input('请填写第二个括号里的字母: ')
                if obtain1 == answer1 and obtain2 == answer2:
                    print_blue('回答正确 !')
                    correct = correct + 1
                    e = e + 1
                else:
                    print_red('回答错误, 第一个括号里的字母是' + Fore.RGB(238, 187, 144) + answer1)
                    print_red('第二个括号里的字母是' + Fore.RGB(238, 187, 144) + answer2)
                    error = error + 1
                    e = e + 1
        elif obtain1 == '3':
            e = 1
            error = 0
            correct = 0
            while True:
                old_word = random.choice(list2)
                empty = random.randint(0, 3)
                empty2 = random.randint(0, 3)
                empty3 = random.randint(0, 3)
                if empty == empty2 or empty2 == empty3 or empty == empty3:
                    while True:
                        empty = random.randint(0, 3)
                        empty2 = random.randint(0, 3)
                        empty3 = random.randint(0, 3)
                        if empty != empty2 and empty2 != empty3 and empty != empty3:
                            break
                new_word = old_word[:empty] + '( )' + old_word[empty + 1:empty2] + '( )' + old_word[
                                                                                           empty2 + 1:empty3] + '( )' + old_word[
                                                                                                                        empty3 + 1:]
                answer1 = old_word[empty]
                answer2 = old_word[empty2]
                answer3 = old_word[empty3]
                print_purple('--------------------------第 {} 题--------------------------'.format(e))
                print_green(new_word)
                obtain1 = input_yellow2('请填写第一个括号里的字母(输入quit退出): ')
                if obtain1 == 'quit':
                    print_orange('一共玩了 {} 题'.format(e - 1))
                    print_red('一共错了 {} 题'.format(error))
                    print_blue('一共对了 {} 题'.format(correct))
                    break
                obtain2 = input('请填写第二个括号里的字母: ')
                obtain3 = input('请填写第三个括号里的字母: ')
                if obtain1 == answer1 and obtain2 == answer2 and obtain3 == answer3:
                    print_blue('回答正确 !')
                    correct = correct + 1
                    e = e + 1
                else:
                    print_red('回答错误, 第一个括号里的字母是' + Fore.RGB(238, 187, 144) + answer1)
                    print_red('第二个括号里的字母是' + Fore.RGB(238, 187, 144) + answer2)
                    print_red('第三个括号里的字母是' + Fore.RGB(238, 187, 144) + answer3)
                    error = error + 1


if __name__ == '__main__':
    word_game2()
