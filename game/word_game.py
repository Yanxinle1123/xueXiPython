import random

from comm.common import orange_print, green_input, input_yellow2, purple_print, red_print, yellow_print, green_print, \
    yellow_print2

word = ['香蕉', '苹果', '西瓜', '橙子', '哈密瓜', '草莓', '冬枣', '葡萄', '柚子', '榴莲', '脐橙', '金桔', '木瓜',
        '雪梨', '水蜜桃', '龙眼', '荔枝', '百香果', '无花果', '牛油果', '西柚', '柠檬', '猕猴桃', '山楂', '芒果',
        '石榴', '枇杷', '书本', '春天', '单词', '答案', '机器人', '人工智能', '电脑', '水杯', '纸巾', '盒子', '冰箱',
        '龙舌兰', '腊梅', '花瓶', '风扇', '杏仁', '苹果', '杏子', '杨梅', '南美梨', '甘蔗渣', '香蕉', '水杨梅',
        '佛手柑', '桨果', '槟榔', '野桑果', '刺梅', '越桔', '野葡萄', '野李子', '美国甜瓜', '杨桃', '冬季甜瓜', '鼠李',
        '樱桃', '栗子', '椰子', '未熟苹果', '果心', '曼越桔', '金桔', '洋李子', '枣子', '果露', '榴莲', '无花果',
        '榛子', '鸡头果', '银杏', '醋栗', '葡萄', '葡萄柚子', '番石榴', '山楂', '山胡桃', '柠檬', '荔枝', '龙眼、桂圆',
        '批杷', '中国柑桔', '芒果', '山竹果', '果渣', '黄香瓜', '油桃', '核仁', '橄榄', '橙子', '桃子', '花生', '梨',
        '柿子', '凤梨', '开心果', '梅子', '石榴', '柚子', '大红苹果', '红毛丹', '覆盆子', '人参果', '片囊', '文旦',
        '芦栗', '桑果', '草莓', '甘蔗', '蜜柑桔', '广柑', '核桃', '冬梨', '马蹄、荸荠', '西瓜', '柠檬', '梨子', '香蕉',
        '葡萄', '李子', '橙子', '橘子', '乌饭果', '芒果', '无花果', '菠萝', '奇异果(弥猴桃)', '樱桃', '柚子', '酸橙',
        '枣子', '荔枝', '椰子', '无花果', '榴梿', '枇杷', '火龙果',
        ]
answer = {'哈密瓜': 'Hami melon',
          '草莓': 'strawberry', '冬枣': 'winter jujube', '榴莲': 'durian',
          '脐橙': 'navel orange', '木瓜': 'papaya', '雪梨': 'snow pear', '水蜜桃': 'honey peach',
          '龙眼': 'longan', '百香果': 'passion fruit', '牛油果': 'avocado',
          '西柚': 'grapefruit', '猕猴桃': 'kiwifruit', '书本': 'book', '春天': 'spring', '单词': 'word',
          '答案': 'answer',
          '机器人': 'robot', '人工智能': 'artificial intelligence', '电脑': 'computer', '水杯': 'water cup',
          '纸巾': 'tissue', '盒子': 'box', '冰箱': 'refrigerator', '龙舌兰': 'agave', '腊梅': 'wintersweet',
          '花瓶': 'vase', '风扇': 'fan', '杏仁': 'almond', '苹果': 'apple', '杏子': 'apricot', '杨梅': 'arbutus',
          '南美梨': 'avocado', '甘蔗渣': 'bagasse', '水杨梅': 'bennet', '佛手柑': 'bergamot',
          '桨果': 'berry', '槟榔': 'betelnut', '野桑果': 'bilberry', '刺梅': 'blackberry', '越桔': 'blueberry',
          '野葡萄': 'bryony', '野李子': 'bullace', '美国甜瓜': 'cantaloupe', '杨桃': 'carambola', '冬季甜瓜': 'casaba',
          '鼠李': 'cascara', '栗子': 'chestnut', '未熟苹果': 'codlin',
          '果心': 'core', '曼越桔': 'cranberry', '金桔': 'cumquat', '洋李子': 'damson', '果露': 'dew',
          '榛子': 'filbert', '鸡头果': 'foxnut', '银杏': 'ginkgo',
          '醋栗': 'gooseberry', '葡萄柚子': 'grapefruit', '番石榴': 'guava', '山楂': 'haw',
          '山胡桃': 'hickory', '龙眼、桂圆': 'longan', '批杷': 'loquat',
          '中国柑桔': 'mandarin', '山竹果': 'mangosteen', '果渣': 'marc', '黄香瓜': 'melon',
          '油桃': 'nectarine', '核仁': 'nucleus', '橄榄': 'olive', '桃子': 'peach', '花生': 'peanut',
          '梨': 'pear', '柿子': 'persimmon', '凤梨': 'pineapple', '开心果': 'pistachio', '梅子': 'plum',
          '石榴': 'pomegranate', '大红苹果': 'quarenden', '红毛丹': 'rambutan', '覆盆子': 'raspberry',
          '人参果': 'sapodilla', '片囊': 'segment', '文旦': 'shaddock', '芦栗': 'sorgo', '桑果': 'sorosis',
          '甘蔗': 'sugarcane', '蜜柑桔': 'tangerline', '广柑': 'tangor', '核桃': 'walnut',
          '冬梨': 'warden', '马蹄、荸荠': 'water-chestnut', '西瓜': 'watermelon', '柠檬': 'lemon', '梨子': 'pear',
          '香蕉': 'banana', '葡萄': 'grape', '李子': 'plum', '橙子': 'orange', '橘子': 'tangerine',
          '乌饭果': 'blueberry', '芒果': 'mango', '菠萝': 'pineapple', '奇异果(弥猴桃)': 'kiwi',
          '樱桃': 'cherry', '柚子': 'pumelo', '酸橙': 'lime', '枣子': 'dates', '荔枝': 'lychee', '椰子': 'coconut',
          '无花果': 'fig', '榴梿': 'durin', '枇杷': 'loquat', '火龙果': 'pitaya',
          }


def word_game():
    orange_print('这是一个单词游戏')
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
            purple_print('----------第 {} 题----------'.format(n))
            danci = random.choice(word)
            green_print(danci)
            da_an = answer[danci]
            huoqu = green_input('请输入这个词语的单词(输入q退出): ')
            if huoqu == da_an:
                orange_print('回答正确 !')
                n = n + 1
                w = w + 1
                defen = defen + 10
            elif huoqu == 'q':
                yellow_print2('已退出')
                break
            else:
                red_print('回答错误,' + danci + '的英文是:' + da_an)
                n = n + 1
                w = w + 1
        yellow_print('第 {} 局结束, 你的得分为: {}'.format(r, defen))
        r = r + 1
        defen = 0
        n = 1


if __name__ == '__main__':
    word_game()
