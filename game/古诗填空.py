import random

di = ['悯农', '静夜思', '江畔独步寻花', '关山月']


def gushiyouxi():
    print('********************古诗填空********************')
    while True:
        print('1.低等\n2.高等')
        shuru = input('请选择难度,输入数字或文字,输入q退出:')
        if shuru == 'q':
            print('已退出')
            break
        elif shuru == '1' or shuru == '低等':
            while True:
                print('现在是低等难度')
                word = random.choice(di)
                if word == '悯农':
                    print('悯农')
                    print('锄禾日当午，')
                    huoqu = input('下句(要输标点符号):')
                    if huoqu != '汗滴禾下土。':
                        print('答错了,是  汗滴禾下土。')
                    print('谁知盘中餐，')
                    huoqu1 = input('下句(要输标点符号):')
                    if huoqu1 != '粒粒皆辛苦。':
                        print('答错了,是  粒粒皆辛苦。')
                        break
                    else:
                        break
                elif word == '静夜思':
                    print('静夜思')
                    print('床前明月光，')
                    huoqu2 = input('下句(要输标点符号):')
                    if huoqu2 != '疑是地上霜。':
                        print('答错了,是  疑是地上霜。')
                    print('举头望明月，')
                    huoqu3 = input('下句(要输标点符号):')
                    if huoqu3 != '低头思故乡。':
                        print('答错了,是  低头思故乡。')
                        break
                elif word == '江畔独步寻花':
                    print('江畔独步寻花')
                    print('黄师塔前江水东，')
                    huoqu4 = input('下句(要输标点符号):')
                    if huoqu4 != '春光懒困倚微风。':
                        print('答错了,是  春光懒困倚微风。')
                    print('桃花一簇开无主，')
                    huoqu5 = input('下句(要输标点符号):')
                    if huoqu5 != '可爱深红爱浅红？':
                        print('答错了,是 可爱深红爱浅红？')
                        break
                else:
                    print('关山月')
                    print('明月出天山，')
                    huoqu6 = input('下句(要输标点符号):')
                    if huoqu6 != '苍茫云海间。':
                        print('答错了,是  苍茫云海间。')
                    print('长风几万里，')
                    huoqu7 = input('下句(要输标点符号):')
                    if huoqu7 != '吹度玉门关。':
                        print('答错了,是 吹度玉门关。')
                        break
        elif shuru == '2' or shuru == '高等':
            print('将进酒')
            print('君不见黄河之水天上来，奔流到海不复回。')
            huoqu7 = input('下句(要输标点符号):')
            if huoqu7 != '君不见高堂明镜悲白发，朝如青丝暮成雪。':
                print('答错了,是 君不见高堂明镜悲白发，朝如青丝暮成雪。')
            print('人生得意须尽欢，莫使金樽空对月。')
            huoqu8 = input('下句(要输标点符号):')
            if huoqu8 != '天生我材必有用，千金散尽还复来。':
                print('答错了,是 天生我材必有用，千金散尽还复来。')
            print('烹羊宰牛且为乐，会须一饮三百杯。')
            huoqu9 = input('下句(要输标点符号):')
            if huoqu9 != '岑夫子，丹丘生，将进酒，杯莫停。':
                print('答错了,是 岑夫子，丹丘生，将进酒，杯莫停。')
            print('与君歌一曲，请君为我倾耳听。')
            huoqua1 = input('下句(要输标点符号):')
            if huoqua1 != '钟鼓馔玉不足贵，但愿长醉不复醒。':
                print('答错了,是 钟鼓馔玉不足贵，但愿长醉不复醒。')
            print('古来圣贤皆寂實，惟有饮者留其名。')
            huoqua2 = input('下句(要输标点符号):')
            if huoqua2 != '陈王昔时宴平乐，斗酒十千您欢谑。':
                print('答错了,是 陈王昔时宴平乐，斗酒十千您欢谑。')
            huoqua3 = input('下句(要输标点符号):')
            if huoqua3 != '主人何为言少钱，径须沽取对君酌。':
                print('答错了,是 主人何为言少钱，径须沽取对君酌。')
            print('五花马，千金裘，')
            huoqua4 = input('下句(要输标点符号):')
            if huoqua4 != '呼儿将出换美酒，与尔同销万古愁。':
                print('答错了,是 呼儿将出换美酒，与尔同销万古愁。')
                break
        else:
            print(shuru, '是一个无效字符')


if __name__ == '__main__':
    gushiyouxi()
