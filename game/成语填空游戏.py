import random

from comm.common import slow_print, tuichu


def huoqu_new_dideng(src_list, ret_list):
    word = random.choice(src_list)
    empty = random.randint(0, 3)
    new = word[:empty] + '( )' + word[empty + 1:]
    ret_list.append(word[empty])
    return new


def huoqu_new_zhongdeng(src_list, ret_list):
    word = random.choice(src_list)
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
    ret_list.append(word[empty])
    ret_list.append(word[empty2])
    return new


def huoqu_new_gaodeng(src_list, ret_list):
    word = random.choice(src_list)
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
    new = word[:empty] + '( )' + word[empty + 1:empty2] + '( )' + word[empty2 + 1:empty3] + '( )' + word[empty3 + 1:]
    ret_list.append(word[empty])
    ret_list.append(word[empty2])
    ret_list.append(word[empty3])
    return new


def cheng_yu_tian_kong():
    src_list = ['铺天盖地', '心急如焚', '杯弓蛇影', '开卷有益', '随遇而安', '指鹿为马', '负荆请罪', '四面楚歌',
                '杯水车薪', '一叶知秋', '图穷匕见', '病入膏肓', '毛遂自荐', '邯郸学步', '杞人忧天', '画蛇添足',
                '守株待兔', '惊弓之鸟', '亡羊补牢', '自相矛盾', '难兄难弟', '狐假虎威', '刻舟求剑', '东施效颦',
                '自欺欺人', '张冠李戴', '不知所云', '乘风破浪', '瓜田李下', '指桑骂槐', '本末倒置', '提纲挈领',
                '请君入瓮', '约法三章', '狡兔三窟', '将计就计', '平易近人', '宽宏大度', '冰清玉洁', '持之以恒',
                '锲而不舍', '废寝忘食', '大义凛然', '临危不俱', '光明磊落', '不屈不挠', '鞠躬尽瘁', '死而后已',
                '恩重如山', '深情厚谊', '手足情深', '形影不离', '血浓于水', '志同道合', '风雨同舟', '赤诚相待',
                '肝胆相照', '生死相依', '无懈可击', '锐不可当', '雷厉风行', '震耳欲聋', '惊心动魄', '铺天盖地',
                '势如破竹', '气贯长虹', '万马奔腾', '如履平地', '循序渐进', '日积月累', '温故知新', '勤能补拙',
                '笨鸟先飞', '学无止境', '学海无涯', '滴水穿石', '发奋图强', '美不胜收', '蔚为壮观', '富丽堂皇',
                '金碧辉煌', '玉宇琼楼', '美妙绝伦', '巧夺天工', '锦上添花', '粉妆玉砌', '别有洞天', '万象更新',
                '抱头鼠窜', '螳臂挡车', '名不正则言不顺', '兵在精而不在多', '皇天不负有心人', '新官上任三把火',
                '强将手下无弱兵', '磨刀不误砍柴工', '朝里无人莫做官', '初生牛犊不怕虎', '识时务者为俊杰',
                '无事不登三宝殿', '一寸光阴一寸金', '跳进黄河洗不清', '古今中外', '名垂青史', '司空见惯', '百步穿杨',
                '一呼百应', '生搬硬套', '见利忘义', '力不从心', '如鱼得水', '百折不挠', '不耻下问', '不可救药',
                '沧海桑田', '东山再起', '开门见山', '情同手足', '随波逐流', '有口难言']
    slow_print('***成语填空游戏***\n')
    while True:
        print('1.低等\n2.中等\n3.高等')
        shuru = input('请选择难度,输入数字或文字,输入q退出:')
        tuichu(shuru)
        is_dideng = shuru == '1' or shuru == '低等'
        is_zhong_deng = shuru == '2' or shuru == '中等'
        is_gao_deng = shuru == '3' or shuru == '高等'
        if not is_dideng and not is_zhong_deng and not is_gao_deng:
            print(shuru, '是一个无效的字符,请重新选择难度!\n')
            continue
        e = 1
        while True:
            nandu = '低'
            if is_zhong_deng:
                nandu = '中'
            elif is_gao_deng:
                nandu = '高'
            print('下一局是{}等难度第 {} 局'.format(nandu, e))
            huoqu = input('是否前往？输入其他字符前往，输入0退出:')
            if huoqu == '0':
                break

            n = 1
            score = 0
            while n <= 10:
                print('\n--------------------第 {} 关--------------------'.format(n))
                ret_list = []
                input_list = []
                new = ""
                if is_dideng:
                    new = huoqu_new_dideng(src_list, ret_list)
                elif is_zhong_deng:
                    new = huoqu_new_zhongdeng(src_list, ret_list)
                elif is_gao_deng:
                    new = huoqu_new_gaodeng(src_list, ret_list)
                print(new)
                is_break = False
                for k, v in enumerate(ret_list, start=1):
                    white = input('请填写第' + str(k) + '个括号(只填括号里的字, 输入q退出):')
                    if white == 'q':
                        is_break = True
                        break
                    input_list.append(white)
                if is_break:
                    break
                if input_list == ret_list:
                    print('\n**********此关顺利通过**********\n')
                    score = score + 10
                else:
                    print('\n**********未过关**********\n')
                    for k, i in enumerate(ret_list, start=1):
                        print('第' + str(k) + '个括号的正确答案为:' + i)
                n = n + 1
            print('最终得分为: ', score, '分,现在,新的一局要开始了')
            e = e + 1


if __name__ == '__main__':
    cheng_yu_tian_kong()
