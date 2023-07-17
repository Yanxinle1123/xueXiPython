import random

from googletrans import Translator

import time
from comm.common import slow_print


def python():
    print('指令说明:')
    print('1. time,date(显示当前时间)')
    print('2. game(显示游戏)')
    print('3. calc(计算用户输入的公式)')
    print('4. area(计算面积)')
    print('5. volume(计算体积)')
    print('6. quit,exit,q(退出)')
    print('7. ead(加密和解密)')
    print('8. trans(翻译)')
    print('9. /(查询指令)')
    while True:
        huoqu = input('>>>')
        if huoqu == '/':
            print('1. time,date(显示当前时间)')
            print('2. game(显示游戏)')
            print('3. calc(计算用户输入的公式)')
            print('4. area(计算面积)')
            print('5. volume(计算体积)')
            print('6. quit,exit,q(退出)')
            print('7. ead(加密和解密)')
            print('8. trans(翻译)')
            print('9. /(查询指令)')
        elif huoqu == 'quit' or huoqu == 'exit' or huoqu == 'q':
            break
        elif huoqu == 'time' or huoqu == 'date':
            current_time = time.time()
            local_time = time.localtime(current_time)
            hour = local_time.tm_hour
            minute = local_time.tm_min
            second = local_time.tm_sec
            print("现在时间是：{}时{}分{}秒".format(hour, minute, second))
        elif huoqu == 'game':
            print('已显示游戏')
            while True:
                shuru = input('1. guess_game\n2.stone_game\n3. idioms\n4.ap_game\n请选择(输入数字,输入q退出)>>>')
                if shuru == 'q':
                    print('已退出')
                    break
                elif shuru == '1':
                    number = random.randint(1, 100)
                    print('现在是一个猜数游戏')
                    while True:
                        huoqu_str = input('请输入一个1到100的数 (输入q退出) : ')
                        if huoqu_str == 'q':
                            print("已退出猜数游戏")
                            break
                        try:
                            huoqu = int(huoqu_str)
                            if huoqu > number + 10:
                                print("\n---------太大了---------\n这个数好大呀！加油，请继续猜\n")
                            elif number + 10 >= huoqu > number:
                                print("\n---------接近了---------\n在努力一点\n")
                            elif number - 10 <= huoqu < number:
                                print("\n---------接近了---------\n在努力一点\n")
                            elif huoqu < number - 5:
                                print("\n---------太小了---------\n这个数好小呀！加油，你一定可以猜中的\n")
                            else:
                                print("恭喜你！猜对了！新的一局开始了")
                        except:
                            print("输入有误")
                elif shuru == '2':
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
                elif shuru == '3':
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
                        new = word[:empty] + '( )' + word[empty + 1:empty2] + '( )' + word[
                                                                                      empty2 + 1:empty3] + '( )' + word[
                                                                                                                   empty3 + 1:]
                        ret_list.append(word[empty])
                        ret_list.append(word[empty2])
                        ret_list.append(word[empty3])
                        return new

                    def cheng_yu_tian_kong():
                        src_list = ['铺天盖地', '心急如焚', '杯弓蛇影', '开卷有益', '随遇而安', '指鹿为马', '负荆请罪',
                                    '四面楚歌',
                                    '杯水车薪', '一叶知秋', '图穷匕见', '病入膏肓', '毛遂自荐', '邯郸学步', '杞人忧天',
                                    '画蛇添足',
                                    '守株待兔', '惊弓之鸟', '亡羊补牢', '自相矛盾', '难兄难弟', '狐假虎威', '刻舟求剑',
                                    '东施效颦',
                                    '自欺欺人', '张冠李戴', '不知所云', '乘风破浪', '瓜田李下', '指桑骂槐', '本末倒置',
                                    '提纲挈领',
                                    '请君入瓮', '约法三章', '狡兔三窟', '将计就计', '平易近人', '宽宏大度', '冰清玉洁',
                                    '持之以恒',
                                    '锲而不舍', '废寝忘食', '大义凛然', '临危不惧', '光明磊落', '不屈不挠', '鞠躬尽瘁',
                                    '死而后已',
                                    '恩重如山', '深情厚谊', '手足情深', '形影不离', '血浓于水', '志同道合', '风雨同舟',
                                    '赤诚相待',
                                    '肝胆相照', '生死相依', '无懈可击', '锐不可当', '雷厉风行', '震耳欲聋', '惊心动魄',
                                    '铺天盖地',
                                    '势如破竹', '气贯长虹', '万马奔腾', '如履平地', '循序渐进', '日积月累', '温故知新',
                                    '勤能补拙',
                                    '笨鸟先飞', '学无止境', '学海无涯', '滴水穿石', '发奋图强', '美不胜收', '蔚为壮观',
                                    '富丽堂皇',
                                    '金碧辉煌', '玉宇琼楼', '美妙绝伦', '巧夺天工', '锦上添花', '粉妆玉砌', '别有洞天',
                                    '万象更新',
                                    '抱头鼠窜', '螳臂挡车', '名不正则言不顺', '兵在精而不在多', '皇天不负有心人',
                                    '新官上任三把火',
                                    '强将手下无弱兵', '磨刀不误砍柴工', '朝里无人莫做官', '初生牛犊不怕虎',
                                    '识时务者为俊杰',
                                    '无事不登三宝殿', '一寸光阴一寸金', '跳进黄河洗不清', '古今中外', '名垂青史',
                                    '司空见惯', '百步穿杨',
                                    '一呼百应', '生搬硬套', '见利忘义', '力不从心', '如鱼得水', '百折不挠', '不耻下问',
                                    '不可救药',
                                    '沧海桑田', '东山再起', '开门见山', '情同手足', '随波逐流', '有口难言']
                        slow_print('***成语填空游戏***\n')
                        while True:
                            print('1.低等\n2.中等\n3.高等')
                            shuru = input('请选择难度,输入数字或文字,输入q退出:')
                            if shuru == 'q':
                                print('已退出')
                                break
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
                elif shuru == '4':
                    di = ['悯农', '静夜思', '江畔独步寻花', '关山月']
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

        elif huoqu == 'calc':
            print(
                '1. 计算器\n2. 日期计算器\n3. 计算水仙花数\n4. 计算是否是闰年\n5. 计算是否构成三角形\n6. 温度转换\n7. 年龄计算器')
            shuru = input('请选择(输入数字)>>>')
            if shuru != '1' and shuru != '2' and shuru != '3' and shuru != '4' and shuru != '5' and shuru != '6' and shuru != '7':
                print('输入有误')
            elif shuru == '1':
                while True:
                    equation = input("请输入计算公式,不能带有[]和{}(输入q退出) :")
                    if equation == 'q':
                        print("已退出计算器")
                        break
                    try:
                        result = eval(equation)
                        print('计算结果为: ', result)
                    except:
                        print("输入有误")
            elif shuru == '2':
                while True:
                    try:
                        now_date = date.today()
                        year_str = input('请输入年(输入q退出):')
                        if year_str == 'q' or year_str == 'Q':
                            print("已退出")
                            break
                        year = int(year_str)
                        month = int(input('请输入月:'))
                        day = int(input('请输入日:'))
                        new_date = date(year, month, day)
                        if now_date >= new_date:
                            print('\n*****当前日期为:', now_date, '*****')
                            print('-----距离  {} 年 {} 月 {} 日----'.format(year, month, day))
                            print('已经过去:', (now_date - new_date).days, '天\n')
                        else:
                            print('\n*****当前日期为:', now_date, '*****')
                            print('-----距离  {} 年 {} 月 {} 日----'.format(year, month, day))
                            print('还差:', (new_date - now_date).days, '天\n')
                    except:
                        print('输入有误')
            elif shuru == '3':
                while True:
                    number_str = input("请输入任意三位数的正整数(输入q退出):")
                    if number_str == 'q':
                        print("已退出")
                        break
                    try:
                        number = int(number_str)
                        if number < 100 or number > 999:
                            print("水仙花数是一个三位数的正整数")
                        ge = number % 10
                        shi = number // 10 % 10
                        bai = number // 100
                        zuizhongshu = ge ** 3 + shi ** 3 + bai ** 3
                        if number == zuizhongshu:
                            print(number, "是水仙花数")
                        else:
                            print(number, "不是水仙花数")
                    except:
                        print("输入有误")
            elif shuru == '4':
                while True:
                    huoqu_str = input("请输入年份(输入q或Q退出):")
                    if huoqu_str == "q" or huoqu_str == "Q":
                        print("已退出")
                        break
                    try:
                        huoqu = int(huoqu_str)
                        year = huoqu
                        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                            print(huoqu_str, "年是润年")
                        else:
                            print(huoqu_str, "年不是润年")
                    except:
                        print(huoqu_str, "不是年份")
            elif shuru == '5':
                while True:
                    a_str = input('请输入第一条边长度(输入q退出) :')
                    if a_str == 'q':
                        print('已退出')
                        break
                    b_str = input('请输入第二条边长度 :')
                    c_str = input('请输入第三条边长度 :')
                    try:
                        a = float(a_str)
                        b = float(b_str)
                        c = float(c_str)
                        if a + b > c and a + c > b and b + c > a:
                            print('能构成三角形')
                        else:
                            print('不能构成三角形')
                    except:
                        print('输入有误')
            elif shuru == '6':
                print("现在是一个可以把华氏度转成摄氏度\n也可以把摄氏度转成华氏度的程序")
                while True:
                    try:
                        print("----------转换方式----------\n1. 华氏度转摄氏度\n2. 摄氏度转华氏度")
                        huoqu = input("请输入转换方式, 输入编号或文字(输入q退出):")
                        if huoqu == 'q':
                            print("已退出")
                            break
                        elif huoqu == '华氏度转摄氏度' or huoqu == '1':
                            f = eval(input('请输入华氏度:'))
                            c = (f - 32) / 1.8
                            print("对应的摄氏度为:", c)
                        elif huoqu == '摄氏度转华氏度' or huoqu == '2':
                            c = eval(input('请输入摄氏度:'))
                            f = 1.8 * c + 32
                            print("对应的华氏度为:", f)
                        else:
                            print("输入有误")
                    except:
                        print("输入有误")
            elif shuru == '7':
                print("现在一个年龄计算器")
                while True:
                    try:
                        print(
                            "----------计算方式----------\n1. 计算秒龄\n2. 计算分龄\n3. 计算时龄\n4. 计算天龄\n5. 计算周龄\n6. 计算月龄\n7. 计算年龄")
                        way = input("请输入计算方式, 输入编号或文字(输入q退出):")
                        if way == 'q':
                            print("已退出")
                            break
                        date = input("请输入出生日期(如 2005-01-20 ):")
                        now = time.time()
                        live = time.mktime(time.strptime(date, '%Y-%m-%d'))
                        second = now - live
                        if way == '1' or way == '计算秒龄':
                            print("你已经活了", second, "秒")
                        elif way == '2' or way == '计算分龄':
                            minute = int(second / 60)
                            print("你已经活了", minute, "分")
                        elif way == '3' or way == '计算时龄':
                            hour = int(second / 3600)
                            print("你已经活了", hour, "时")
                        elif way == '4' or way == '计算天龄':
                            day = int(second / 3600 / 24)
                            print("你已经活了", day, "天")
                        elif way == '5' or way == '计算周龄':
                            week = int(second / 3600 / 24 / 7)
                            print("你已经活了", week, "周")
                        elif way == '6' or way == '计算月龄':
                            month = int(second / 3600 / 24 / 31)
                            print("你已经活了", month, "月")
                        elif way == '7' or way == '计算年龄':
                            year = round(second / 3600 / 24 / 365, 2)
                            print("你已经活了", year, "年")
                        else:
                            print("输入有误")
                    except:
                        print("输入有误")
        elif huoqu == 'area':
            while True:
                huoqu = input(
                    "输入1计算三角形面积\n输入2计算正方形面积\n输入3计算长方形面积\n输入4计算圆的面积\n输入5计算梯形面积\n输入q退出:")
                if huoqu == 'q':
                    print("已退出")
                    break
                if huoqu == '1':
                    di_str = input("请输入三角形底边的长度(输入q退出):")
                    if di_str == 'q':
                        print("已退出")
                        break
                    gao_str = input("请输入三角形高的高度(输入q退出):")
                    if gao_str == 'q':
                        print("已退出")
                        break
                    try:
                        di = float(di_str)
                        gao = float(gao_str)
                        mj = di * gao / 2
                        print("三角形的面积为:", mj)
                    except:
                        print("输入有误")
                if huoqu == '2':
                    bianchang_str = input("请输入正方形的边长(输入q退出):")
                    if bianchang_str == 'q':
                        print("已退出")
                        break
                    try:
                        bianchang = float(bianchang_str)
                        mianj = bianchang * bianchang
                        print("正方形的面积为:", mianj)
                    except:
                        print("输入有误")
                if huoqu == '3':
                    chang_str = input("请输入长方形长的长度(输入q退出):")
                    if chang_str == 'q':
                        print("已退出")
                        break
                    kuan_str = input("请输入长方形宽的宽度(输入q退出):")
                    if kuan_str == 'q':
                        print("已退出")
                        break
                    try:
                        chang = float(chang_str)
                        kuan = float(kuan_str)
                        mji = chang * kuan
                        print("长方形的面积为:", mji)
                    except:
                        print("输入有误")
                if huoqu == '4':
                    pi = 3.14
                    banjing_str = input("请输入圆的半径(输入q退出):")
                    if banjing_str == 'q':
                        print("已退出")
                        break
                    try:
                        banjing = float(banjing_str)
                        mianji = pi * banjing * banjing
                        print("圆的面积为:", mianji)
                    except:
                        print("输入有误")
                if huoqu == '5':
                    shangdi_str = input("请输入梯形的上底(输入q退出):")
                    if shangdi_str == 'q':
                        print("已退出")
                        break
                    xiadi_str = input("请输入梯形的下底(输入q退出):")
                    if xiadi_str == 'q':
                        print("已退出")
                        break
                    gao_str = input("请输入梯形的高(输入q退出):")
                    if gao_str == 'q':
                        print("已退出")
                        break
                    try:
                        shangdi = float(shangdi_str)
                        xiadi = float(xiadi_str)
                        gao = float(gao_str)
                        mianji = (shangdi + xiadi) * gao / 2
                        print("梯形的面积为:", mianji)
                    except:
                        print("输入有误")
        elif huoqu == 'volume':
            while True:
                huoqu = input(
                    "输入1计算正方体体积\n输入2计算长方体体积\n输入3计切面圆柱体体积\n输入4计算球体积\n输入q退出:")
                if huoqu == 'q':
                    print("已退出")
                    break
                if huoqu == '1':
                    bianchang_str = input("请输入正方体的边长(输入q退出):")
                    if bianchang_str == 'q':
                        print("已退出")
                        break
                    try:
                        bianchang = float(bianchang_str)
                        tj = bianchang * bianchang * bianchang
                        print("正方体体积为:", tj)
                    except:
                        print("输入有误")
                if huoqu == '2':
                    chang_str = input("请输入长方体的长度(输入q退出):")
                    if chang_str == 'q':
                        print("已退出")
                        break
                    kuan_str = input("请输入长方体的宽度(输入q退出):")
                    if kuan_str == 'q':
                        print("已退出")
                        break
                    gao_str = input("请输入长方体的高度(输入q退出):")
                    if gao_str == 'q':
                        print("已退出")
                        break
                    try:
                        chang = float(chang_str)
                        kuan = float(kuan_str)
                        gao = float(gao_str)
                        tij = chang * kuan * gao
                        print("长方体体积为:", tij)
                    except:
                        print("输入有误")
                if huoqu == '3':
                    pi = 3.14
                    banjing_str = input("请输入底面半径(输入q退出):")
                    if banjing_str == 'q':
                        print("已退出")
                        break
                    gao_str = input("请输入高(输入q退出):")
                    if gao_str == 'q':
                        print("已退出")
                        break
                    try:
                        banjing = float(banjing_str)
                        gao = float(gao_str)
                        tj = pi * banjing * banjing * gao
                        print("体积为:", tj)
                    except:
                        print("输入有误，请从输入一遍")
                if huoqu == '4':
                    pi = 3.14
                    banjin_str = input("请输入球的半径(输入q退出)：")
                    if banjin_str == 'q':
                        print("已退出")
                        break
                    try:
                        banjin = float(banjin_str)
                        tj = (4 / 3) * pi * banjin * banjin * banjin
                        print("球的体积为:", tj)
                    except:
                        print("输入错误")
        elif huoqu == 'ead':
            def encrypt(text, shift):
                encrypted_text = ""
                for char in text:
                    char_code = ord(char)
                    if 0x4E00 <= char_code <= 0x9FFF or char.isascii():
                        encrypted_text += chr((char_code + shift) % 0x10FFFF)
                    else:
                        encrypted_text += char
                return encrypted_text

            def decrypt(text, shift):
                decrypted_text = ""
                for char in text:
                    char_code = ord(char)
                    if 0x4E00 <= char_code <= 0x9FFF or char.isascii():
                        decrypted_text += chr((char_code - shift) % 0x10FFFF)
                    else:
                        decrypted_text += char
                return decrypted_text

            def play():
                print("现在是一个可以加密和解密的程序")
                while True:
                    huoqu = input("请输入要加密的内容(输入q退出)：")
                    if huoqu == 'q' or huoqu == '退出' or huoqu == 'tuichu':
                        print("已退出")
                        break
                    try:
                        shift_value = 3

                        encrypted_text = encrypt(huoqu, shift_value)
                        print("密文：", encrypted_text)

                        miwen = input("请输入要解密的内容：")
                        decrypted_text = decrypt(miwen, shift_value)
                        print("明文:", decrypted_text)
                        print("---" * 10)
                        print("再来一次吧")
                    except:
                        print("程序运行异常,请重新输入")

            if __name__ == "__main__":
                play()
        elif huoqu == 'trans':
            def translate_text(text, src_lang, dest_lang):
                # 创建翻译器对象
                translator = Translator(service_urls=['translate.google.com'])

                # 翻译文本
                result = translator.translate(text, src=src_lang, dest=dest_lang)

                # 返回翻译结果
                return result.text

            def validate_language(lang):
                # 验证语言选项
                valid_options = ['zh-CN', 'en']

                if lang in valid_options:
                    return True
                else:
                    return False

            # 主循环
            while True:
                print("请选择翻译方向：")
                print("1. 中文翻译为英文")
                print("2. 英文翻译为中文")
                print("输入 q 退出")

                option = input("请选择选项: ")

                if option == "1":
                    src_lang = 'zh-CN'
                    dest_lang = 'en'
                elif option == "2":
                    src_lang = 'en'
                    dest_lang = 'zh-CN'
                elif option.lower() == "q":
                    print("程序已退出。")
                    break
                else:
                    print("无效的选项，请重新输入。")
                    continue

                text = input("请输入要翻译的文本：")

                try:
                    translated_text = translate_text(text, src_lang, dest_lang)
                    print("翻译结果：", translated_text)
                except Exception as e:
                    print("翻译发生错误:", str(e))

                print()  # 输出空行以提升可读性
        else:
            print('指令', huoqu, '无效')
            print('建议输入 / 查询指令')


if __name__ == '__main__':
    python()
