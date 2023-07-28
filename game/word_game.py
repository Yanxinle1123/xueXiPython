import random

from comm.common import print_brown, input_green, input_yellow2, print_purple, print_red, print_yellow, print_green, \
    print_yellow2

word = ['香蕉', '苹果', '西瓜', '橙子', '哈密瓜', '草莓', '冬枣', '葡萄', '柚子', '榴莲', '脐橙', '金桔', '木瓜',
        '雪梨', '水蜜桃', '龙眼', '荔枝', '百香果', '无花果', '牛油果', '西柚', '柠檬', '猕猴桃', '山楂', '芒果',
        '石榴', '枇杷', '书本', '春天', '单词', '答案', '机器人', '人工智能', '电脑', '水杯', '纸巾', '盒子', '冰箱',
        '龙舌兰', '腊梅', '花瓶', '风扇']
answer = {'香蕉': 'banana', '苹果': 'apple', '西瓜': 'watermelon', '橙子': 'orange', '哈密瓜': 'Hami melon',
          '草莓': 'strawberry', '冬枣': 'winter jujube', '葡萄': 'grape', '柚子': 'grapefruit', '榴莲': 'durian',
          '脐橙': 'navel orange', '金桔': 'kumquat', '木瓜': 'papaya', '雪梨': 'snow pear', '水蜜桃': 'honey peach',
          '龙眼': 'longan', '荔枝': 'litchi', '百香果': 'passion fruit', '无花果': 'fig', '牛油果': 'avocado',
          '西柚': 'grapefruit', '柠檬': 'lemon', '猕猴桃': 'kiwifruit', '山楂': 'hawthorn', '芒果': 'mango',
          '石榴': 'pomegranate', '枇杷': 'loquat', '书本': 'book', '春天': 'spring', '单词': 'word', '答案': 'answer',
          '机器人': 'robot', '人工智能': 'artificial intelligence', '电脑': 'computer', '水杯': 'water cup',
          '纸巾': 'tissue', '盒子': 'box', '冰箱': 'refrigerator', '龙舌兰': 'agave', '腊梅': 'wintersweet',
          '花瓶': 'vase', '风扇': 'fan'}


def word_game():
    print_brown('这是一个单词游戏')
    r = 1
    n = 1
    defen = 0
    while True:
        shuru = input_yellow2('是否进入第 {} 局(y/n): '.format(r))
        if shuru == 'n':
            print('已退出')
            break
        w = 1
        while w <= 10:
            print_purple('----------第 {} 题----------'.format(n))
            danci = random.choice(word)
            print_green(danci)
            da_an = answer[danci]
            huoqu = input_green('请输入这个水果的单词(输入q退出): ')
            if huoqu == da_an:
                print_brown('回答正确 !')
                n = n + 1
                w = w + 1
                defen = defen + 10
            elif huoqu == 'q':
                print_yellow2('已退出')
                break
            else:
                print_red('回答错误,' + danci + '的英文是:' + da_an)
                n = n + 1
                w = w + 1
        print_yellow('第 {} 局结束, 你的得分为: {}'.format(r, defen))
        r = r + 1
        defen = 0
        n = 1


if __name__ == '__main__':
    word_game()
