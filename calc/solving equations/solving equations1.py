from comm.common import *

list = []


def solving_equations1():
    orange_print('这是一个可以解一些比较低等的方程的程序,例如x-3=2等')
    while True:
        try:
            list.clear()
            huoqu = yellow_input2('请输入一个方程 (输入q退出，方程中只能有一个未知数) :')
            if huoqu == 'q':
                orange_print('已退出')
                break
            list.append(huoqu)
            formula = list[0]
            variable1 = formula[0]
            variable2 = formula[1]
            symbol = formula[1]
            new_formula = formula[2:]
            char = '='
            number1_str = new_formula[:new_formula.index(char)]
            number1 = float(number1_str)
            number1_len = int(len(number1_str))
            variable3 = formula[number1_len + 2]
            number2 = float(new_formula[number1_len + 1:])
            if variable1.isdigit():
                red_print('方程的未知数不能为数字')
                continue
            if variable2 == '=':
                red_print("方程输入有误")
            if variable3 != '=':
                red_print('方程输入有误')
            if symbol == '+':
                result = number2 - number1
                print(variable1, '=', result)
            elif symbol == '-':
                result = number1 + number2
                print(variable1, '=', result)
            elif symbol == '*':
                result = number2 / number1
                print(variable1, '=', result)
            elif symbol == '/':
                result = number2 * number1
                print(variable1, '=', result)
        except:
            red_print('方程输入有误')


if __name__ == '__main__':
    solving_equations1()
