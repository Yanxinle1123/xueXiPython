import time

import numpy as np
from Levenshtein import distance
from colored import Fore

from calc.calc import calculator
from calc.pi的后50位 import pi50wei
from calc.九九乘法表 import mult_table
from calc.华氏度转摄氏度 import HuaShiDuZhuanSheShiDuAndSheShiDuZhuanHuaShiDu
from calc.年龄计算器 import NianNingJiSuanQi
from calc.日期计算器 import daycalc
from calc.是否是闰年 import PanDuanRunNian
from calc.是否构成三角形 import sanjiaoxing
from calc.水仙花数 import QiuShuiXianHuaShu
from calc.计算体积 import tiJi
from calc.计算面积 import mianj
from calc.货币转换 import huo_bi_zhuan_huan
from comm.common import print_yellow, print_yellow2, input_yellow2, print_red
from game.guess_game第2版 import guess_game_ShengJiBan
from game.keyboard_game import keyboard_game
from game.stone_game2 import stone
from game.word_game import word_game
from game.古诗填空 import gushiyouxi
from game.成语填空游戏 import cheng_yu_tian_kong
from other.RainbowHELLO import rainbowHELLO
from other.RainbowHI import rainbowHI
from other.computer import computer
from other.goodbye import goodbye
from other.hello import hello
from other.thanks import thankyou
from other.位置 import address
from other.加密和解密 import ead
from other.加密和解密3 import ead3
from other.时间 import shijian
from other.查询日历 import rili
from other.翻译 import trans


def python():
    hello()
    time.sleep(0.5)
    print_yellow2('\033[1m指令说明:')
    print('1. time, date(显示当前时间)')
    print('2. game(显示游戏)')
    print('3. calc(计算用户输入的公式)')
    print('4. area(计算面积)')
    print('5. volume(计算体积)')
    print('6. quit, exit, q, goodbye(退出)')
    print('7. ead(加密和解密)')
    print('8. trans(翻译)')
    print('9. computer(操作系统信息)')
    print('10. pi(获取圆周率)')
    print('11. address(获取当前经纬度)')
    print('12. calendar(查询日历)')
    print('13. mult-table(查询九九乘法表)')
    print('14. /(查询指令)')
    a = 1
    while True:
        huoqu = input_yellow2('>>>')
        if huoqu == '/':
            print('1. time, date(显示当前时间)')
            print('2. game(显示游戏)')
            print('3. calc(计算用户输入的公式)')
            print('4. area(计算面积)')
            print('5. volume(计算体积)')
            print('6. quit, exit, q, goodbye(退出)')
            print('7. ead(加密和解密)')
            print('8. trans(翻译)')
            print('9. computer(操作系统信息)')
            print('10. pi(获取圆周率的后50位数字)')
            print('11. address(获取当前经纬度)')
            print('12. calendar(查询日历)')
            print('13. mult-table(查询九九乘法表)')
            print('14. /(查询指令)')
        elif huoqu == 'hello':
            rainbowHI()
            print_yellow('')
        elif huoqu == 'hi':
            rainbowHELLO()
            print_yellow('')
        elif huoqu == 'computer':
            computer()
        elif huoqu == 'calendar':
            rili()
        elif huoqu == 'address':
            address()
        elif huoqu == 'quit' or huoqu == 'exit' or huoqu == 'q':
            while True:
                shuru = input('你喜欢这个程序吗(y/n) :')
                if shuru == 'y' or shuru == 'n':
                    thankyou()
                    break
                else:
                    print('输入有误')
            print('')
            goodbye()
            break
        elif huoqu == 'goodbye':
            goodbye()
            break
        elif huoqu == 'pi':
            pi50wei()
        elif huoqu == 'mult-table':
            mult_table()
        elif huoqu == 'time' or huoqu == 'date':
            shijian()
        elif huoqu == 'game':
            print('已显示游戏')
            while True:
                shuru = input_yellow2(
                    '1. guess_game\n2.stone_game\n3. idioms\n4.ap_game\n5.word_game\n6.keyboard_game\n请选择(输入数字, 输入q退出)>>>')
                if shuru == 'q':
                    print('已退出')
                    break
                elif shuru == '1':
                    guess_game_ShengJiBan()
                elif shuru == '2':
                    stone()
                elif shuru == '3':
                    cheng_yu_tian_kong()
                elif shuru == '4':
                    gushiyouxi()
                elif shuru == '5':
                    word_game()
                elif shuru == '6':
                    keyboard_game()
                else:
                    print('输入有误')
        elif huoqu == 'calc':
            while True:
                print(
                    '1. 计算器\n2. 日期计算器\n3. 计算水仙花数\n4. 计算是否是闰年\n5. 计算是否构成三角形\n6. 温度转换\n7. 年龄计算器\n8. 货币转换')
                shuru = input('请选择(输入数字, 输入q退出)>>>')
                if shuru == '1':
                    calculator()
                elif shuru == '2':
                    daycalc()
                elif shuru == '3':
                    QiuShuiXianHuaShu()
                elif shuru == '4':
                    PanDuanRunNian()
                elif shuru == '5':
                    sanjiaoxing()
                elif shuru == '6':
                    HuaShiDuZhuanSheShiDuAndSheShiDuZhuanHuaShiDu()
                elif shuru == '7':
                    NianNingJiSuanQi()
                elif shuru == '8':
                    huo_bi_zhuan_huan()
                elif shuru == 'q':
                    print('已退出')
                    break
                else:
                    print('输入有误')
        elif huoqu == 'area':
            mianj()
        elif huoqu == 'volume':
            tiJi()
        elif huoqu == 'ead':
            while True:
                shuru = input_yellow2('你要那种加密方法(1.凯撒密码, 2.UTF-8编码, q.退出):')
                if shuru == '1':
                    ead()
                elif shuru == '2':
                    ead3()
                elif shuru == 'q':
                    break
                else:
                    print_red('选项有误')
        elif huoqu == 'trans':
            trans()
        else:
            def find_closest_word(user_input, words):
                min_distance = np.inf
                closest = None
                for word in words:
                    d = distance(user_input.lower(), word.lower())
                    if d < min_distance:
                        min_distance = d
                        closest = word
                return closest

            print('\n\033[1m\033[31m指令', Fore.RGB(225, 255, 0) + huoqu, '\033[31m\033[1m无效\033[0m',
                  Fore.RGB(125, 250, 85) + '               {} ↵ '.format(a))
            print('\033[31m\033[1m建议输入 / 查询指令\033[0m')
            words = ["time", "date", "address", "game", "calc", "area", "q", "quit", "exit", "ead", "pi", "volume",
                     "trans", "goodbye", "calendar", 'mult-table']
            closest = find_closest_word(huoqu, words)
            print(Fore.RED + f"\033[1m与", Fore.RGB(225, 255, 0) + huoqu, Fore.RED + '\033[1m最接近的指令是',
                  Fore.RGB(225, 255, 0) + closest)
            a = a + 1
            print_yellow('')


if __name__ == '__main__':
    python()
