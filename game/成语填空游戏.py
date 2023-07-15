import random

from comm.common import slow_print


def ChengYuTianKong():
    list = ['铺天盖地', '心急如焚', '杯弓蛇影', '开卷有益', '随遇而安', '指鹿为马', '负荆请罪', '四面楚歌', '杯水车薪',
            '一叶知秋', '图穷匕见', '病入膏肓', '毛遂自荐', '邯郸学步', '杞人忧天', '画蛇添足', '守株待兔', '惊弓之鸟',
            '亡羊补牢', '自相矛盾', '难兄难弟', '狐假虎威', '刻舟求剑', '东施效颦', '自欺欺人', '张冠李戴', '不知所云',
            '乘风破浪', '瓜田李下', '指桑骂槐', '本末倒置', '提纲挈领', '请君入瓮', '约法三章', '狡兔三窟', '将计就计',
            '平易近人', '宽宏大度', '冰清玉洁', '持之以恒', '锲而不舍', '废寝忘食', '大义凛然', '临危不俱', '光明磊落',
            '不屈不挠', '鞠躬尽瘁', '死而后已', '恩重如山', '深情厚谊', '手足情深', '形影不离', '血浓于水', '志同道合',
            '风雨同舟', '赤诚相待', '肝胆相照', '生死相依', '无懈可击', '锐不可当', '雷厉风行', '震耳欲聋', '惊心动魄',
            '铺天盖地', '势如破竹', '气贯长虹', '万马奔腾', '如履平地', '循序渐进', '日积月累', '温故知新', '勤能补拙',
            '笨鸟先飞', '学无止境', '学海无涯', '滴水穿石', '发奋图强', '美不胜收', '蔚为壮观', '富丽堂皇', '金碧辉煌',
            '玉宇琼楼', '美妙绝伦', '巧夺天工', '锦上添花', '粉妆玉砌', '别有洞天', '万象更新', '抱头鼠窜', '螳臂挡车',
            '名不正则言不顺', '兵在精而不在多', '皇天不负有心人', '新官上任三把火', '强将手下无弱兵', '磨刀不误砍柴工',
            '朝里无人莫做官', '初生牛犊不怕虎', '识时务者为俊杰', '无事不登三宝殿', '一寸光阴一寸金', '跳进黄河洗不清',
            '古今中外', '名垂青史', '司空见惯', '百步穿杨', '一呼百应', '生搬硬套', '见利忘义', '力不从心', '如鱼得水',
            '百折不挠', '不耻下问', '不可救药', '沧海桑田', '东山再起', '开门见山', '情同手足', '随波逐流', '有口难言']
    slow_print('***成语填空游戏***\n')
    while True:
        print('1.低等\n2.中等\n3.高等')
        shuru = input('请选择难度,输入数字或文字,输入q退出:')
        if shuru == 'q':
            print('已退出')
            break
        elif shuru == '1' or shuru == '低等':
            e = 1
            while True:
                print('下一局是低等难度第 {} 局'.format(e))
                huoqu = input('是否前往？输入其他字符前往，输入0退出:')
                if huoqu == '0':
                    print('已退出')
                    break
                n = 1
                score = 0
                while n <= 10:
                    print('\n--------------------第 {} 关--------------------'.format(n))
                    word = random.choice(list)
                    empty = random.randint(0, 3)
                    new = word[:empty] + '( )' + word[empty + 1:]
                    print(new)
                    white = input('请填写(只填括号里的字, 输入q退出):')
                    if white == 'q' or white == 'Q':
                        print('已退出')
                        break
                    elif white == word[empty]:
                        print('\n**********此关顺利通过**********\n')
                        score = score + 10
                    else:
                        print('\n**********未过关**********\n')
                        print('正确答案为: ', word[empty])
                    n = n + 1
                print('最终得分为: ', score, '分,现在,新的一局要开始了')
                e = e + 1
        elif shuru == '2' or shuru == '中等':
            e = 1
            while True:
                print('下一局是中等难度第 {} 局'.format(e))
                huoqu = input('是否前往？输入其他字符前往，输入0退出:')
                if huoqu == '0':
                    print('已退出')
                    break
                n = 1
                score = 0
                while n <= 10:
                    print('\n--------------------第 {} 关--------------------'.format(n))
                    word = random.choice(list)
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
                    new = word[:empty] + '( )' + word[empty + 1:empty2] + '( )' + word[empty2 + 1:]
                    print(new)

                    white = input('请填写第一个括号(只填括号里的字, 输入q退出):')
                    if white == 'q' or white == 'Q':
                        print('已退出')
                        break

                    white2 = input('请填写第二个括号(只填括号里的字, 输入q退出):')
                    if white2 == 'q' or white2 == 'Q':
                        print('已退出')
                        break

                    if white == word[empty] and white2 == word[empty2]:
                        print('\n**********此关顺利通过**********\n')
                        score = score + 10
                    else:
                        print('\n**********未过关**********\n')
                        print('第一个括号的正确答案为: ', word[empty], '\n第二个括号的正确答案为: ', word[empty2])
                    n = n + 1
                print('最终得分为: ', score, '分,现在,新的一局要开始了')
                e = e + 1
        elif shuru == '3' or shuru == '高等':
            e = 1
            while True:
                print('下一局是高等难度第 {} 局'.format(e))
                huoqu = input('是否前往？输入其他字符前往，输入0退出:')
                if huoqu == '0':
                    print('已退出')
                    break
                n = 1
                score = 0
                while n <= 10:
                    print('\n--------------------第 {} 关--------------------'.format(n))
                    word = random.choice(list)
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
                    number_list = [empty, empty2, empty3]
                    sorted_list = sorted(number_list)
                    empty = sorted_list[0]
                    empty2 = sorted_list[1]
                    empty3 = sorted_list[2]
                    new = word[:empty] + '( )' + word[empty + 1:empty2] + '( )' \
                          + word[empty2 + 1:empty3] + '( )' + word[empty3 + 1:]

                    print(new)
                    white1 = input('请填写第一个括号(只填括号里的字, 输入q退出)')
                    if white1 == 'q' or white1 == 'Q':
                        print('已退出')
                        break
                    white2 = input('请填写第二个括号(只填括号里的字, 输入q退出):')
                    if white2 == 'q' or white2 == 'Q':
                        print('已退出')
                        break
                    white3 = input('请填写第三个括号(只填括号里的字, 输入q退出):')
                    if white3 == 'q' or white3 == 'Q':
                        print('已退出')
                        break
                    if white1 == word[empty] and white2 == word[empty2] and white3 == word[empty3]:
                        print('\n**********此关顺利通过**********\n')
                        score = score + 10
                    else:
                        print('\n**********未过关**********\n')
                        print('第一个括号的正确答案为: ', word[empty], '\n第二个括号的正确答案为: ', word[empty2],
                              '\n第二个括号的正确答案为: ', word[empty3])
                    n = n + 1
                print('最终得分为: ', score, '分,现在,新的一局要开始了')
                e = e + 1
        else:
            print(shuru, '是一个无效的字符')


if __name__ == '__main__':
    ChengYuTianKong()
