from colorama import Fore

from calc.calc import calculator
from calc.华氏度转摄氏度 import HuaShiDuZhuanSheShiDuAndSheShiDuZhuanHuaShiDu
from calc.年龄计算器 import NianNingJiSuanQi
from calc.日期计算器 import daycalc
from calc.是否是闰年 import PanDuanRunNian
from calc.是否构成三角形 import sanjiaoxing
from calc.水仙花数 import QiuShuiXianHuaShu
from calc.计算体积 import tiJi
from calc.计算面积 import mianj
from calc.货币转换 import huo_bi_zhuan_huan
from game.guess_game第2版 import guess_game_ShengJiBan
from game.stone_game2 import stone
from game.古诗填空 import gushiyouxi
from game.成语填空游戏 import cheng_yu_tian_kong
from other.computer import computer
from other.time import shijian
from other.加密和解密 import ead
from other.翻译 import trans


def python():
    print(
        Fore.YELLOW + '------------------------------------------------------------综合程序------------------------------------------------------------')
    print(Fore.CYAN + '')
    print('指令说明:', 0.08)
    print('1. time,date(显示当前时间)', 0.08)
    print('2. game(显示游戏)', 0.08)
    print('3. calc(计算用户输入的公式)', 0.08)
    print('4. area(计算面积)', 0.08)
    print('5. volume(计算体积)', 0.08)
    print('6. quit,exit,q(退出)', 0.08)
    print('7. ead(加密和解密)', 0.08)
    print('8. trans(翻译)', 0.08)
    print('9. computer(操作系统信息)', 0.08)
    print('10. /(查询指令)', 0.08)
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
            print('9. computer(操作系统信息)')
            print('10. /(查询指令)')
        elif huoqu == 'computer':
            computer()
        elif huoqu == 'quit' or huoqu == 'exit' or huoqu == 'q':
            print(
                Fore.YELLOW + '-------------------------------------------------------------------------------------------------------------------------------')
            break
        elif huoqu == 'time' or huoqu == 'date':
            shijian()
        elif huoqu == 'game':
            print('已显示游戏')
            while True:
                shuru = input('1. guess_game\n2.stone_game\n3. idioms\n4.ap_game\n请选择(输入数字,输入q退出)>>>')
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
        elif huoqu == 'calc':
            print(
                '1. 计算器\n2. 日期计算器\n3. 计算水仙花数\n4. 计算是否是闰年\n5. 计算是否构成三角形\n6. 温度转换\n7. 年龄计算器\n8. 货币转换')
            shuru = input('请选择(输入数字)>>>')
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
            else:
                print('输入有误')
        elif huoqu == 'area':
            mianj()
        elif huoqu == 'volume':
            tiJi()
        elif huoqu == 'ead':
            ead()
        elif huoqu == 'trans':
            trans()
        else:
            print(Fore.RED + '\n指令', huoqu, '无效')
            print('建议输入 / 查询指令')
            print(Fore.CYAN + '')


if __name__ == '__main__':
    python()
