import re
import select
import sys
import time

import colored
import requests
from bs4 import BeautifulSoup
from colored import Fore


def tuichu(input_str, tishi='已退出', tuichu_str='q'):
    if input_str == tuichu_str:
        orange_print(tishi)
        sys.exit()


class TimeoutExpired(Exception):
    pass


def input_timeout(prompt, timeout=9):
    print(Fore.RGB(225, 255, 0) + prompt, end=" ", flush=True)
    fds = [sys.stdin]
    result = []
    r, _, _ = select.select(fds, [], [], timeout)
    if not r:
        raise TimeoutExpired()

    input_str = sys.stdin.readline().rstrip()
    result.append(input_str)
    return result[0]


def stop_thread(thread):
    thread.cancel()


def slow_print(text, delay=0.23):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # 换行


def slow_input(text, delay=0.23):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    return input()  # 换行


def tuichu2(input_str, tishi='已退出', tuichu_str='n'):
    if input_str == tuichu_str:
        print(tishi)
        sys.exit()


def slow_print2(text, delay=0.25):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def red_print(input_str):
    print(Fore.RGB(225, 0, 50) + input_str)


def orange_print(input_str):
    print(Fore.RGB(255, 170, 0) + input_str)


def yellow_print(input_str):
    print(Fore.CYAN + Fore.GREEN + Fore.RED + Fore.GREEN + Fore.BLUE + Fore.YELLOW + input_str)


def yellow_print2(input_str):
    print(Fore.RGB(225, 255, 0) + input_str)


def green_print(input_str):
    print(Fore.RGB(125, 250, 85) + input_str)


def cyan_print(input_str):
    print(Fore.CYAN + input_str)


def blue_print(input_str):
    print(Fore.RGB(50, 150, 225) + input_str)


def purple_print(input_str):
    print(Fore.RGB(171, 91, 187) + input_str)


def red_input(input_str):
    result = input(Fore.RGB(225, 0, 50) + input_str)
    return result


def orange_input(input_str):
    result = input(Fore.RGB(255, 170, 0) + input_str)
    return result


def yellow_input(input_str):
    result = input(Fore.CYAN + Fore.GREEN + Fore.RED + Fore.GREEN + Fore.BLUE + Fore.YELLOW + input_str)
    return result


def yellow_input2(input_str):
    result = input(Fore.RGB(225, 255, 0) + input_str)
    return result


def green_input(input_str):
    result = input(Fore.RGB(125, 250, 85) + input_str)
    return result


def cyan_input(input_str):
    result = input(Fore.CYAN + input_str)
    return result


def blue_input(input_str):
    result = input(Fore.RGB(50, 150, 225) + input_str)
    return result


def purple_input(input_str):
    result = input(Fore.RGB(171, 91, 187) + input_str)
    return result


def is_chinese_start(s):
    return s and 0x4E00 <= ord(s[0]) <= 0x9FA0


def is_chinese_start(s):
    return s and 0x4E00 <= ord(s[0]) <= 0x9FA0


def hex_to_rgb(hex_value_print):
    hex_value = hex_value_print.upper()
    if '#' in hex_value:
        hex_value = hex_value.lstrip('#')
    r = int(hex_value[0:2], 16)
    g = int(hex_value[2:4], 16)
    b = int(hex_value[4:6], 16)
    rgb = f"{r}, {g}, {b}"  # 将 r、g、b 组合成一个逗号分隔的字符串
    return rgb


def rgb_to_hex(rgb_print):
    rgb = rgb_print.upper()
    if isinstance(rgb, str):
        rgb = tuple(map(int, rgb.split(',')))  # 如果输入是字符串，则将其分割为整数值的元组

    r, g, b = rgb
    if r > 255 or g > 255 or b > 255:
        raise ValueError
    elif r < 0 or g < 0 or b < 0:
        raise TypeError
    hex_value = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex_value


def rainbow_print(text):
    colors = [colored.Fore.RGB(225, 0, 50), Fore.RGB(255, 170, 0), colored.Fore.RGB(225, 255, 0),
              colored.Fore.RGB(125, 250, 85), colored.Fore.CYAN, colored.Fore.RGB(50, 150, 225)]
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        print(color + char, end='')


def rainbow_slow_print(text, delay=0.23):
    colors = [colored.Fore.RGB(225, 0, 50), Fore.RGB(255, 170, 0), colored.Fore.RGB(225, 255, 0),
              colored.Fore.RGB(125, 250, 85), colored.Fore.CYAN, colored.Fore.RGB(50, 150, 225)]
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        print(color + char, end='')
        time.sleep(delay)


def rainbow_input(input_str):
    colors = [colored.Fore.RGB(225, 0, 50), Fore.RGB(255, 170, 0), colored.Fore.RGB(225, 255, 0),
              colored.Fore.RGB(125, 250, 85), colored.Fore.CYAN, colored.Fore.RGB(50, 150, 225)]
    for i, char in enumerate(input_str):
        color = colors[i % len(colors)]
        print(color + char, end='')
    return input()


def rainbow_slow_input(input_str, delay=0.23):
    colors = [colored.Fore.RGB(225, 0, 50), Fore.RGB(255, 170, 0), colored.Fore.RGB(225, 255, 0),
              colored.Fore.RGB(125, 250, 85), colored.Fore.CYAN, colored.Fore.RGB(50, 150, 225)]
    for i, char in enumerate(input_str):
        color = colors[i % len(colors)]
        print(color + char, end='')
        time.sleep(delay)
    return input()


def ord2(text):
    encrypted_text = ""
    for char in text:
        code = ord(char)
        encrypted_code = str(code)
        encrypted_text += encrypted_code + " "
    return encrypted_text[:-1]


def chr2(text):
    encrypted_codes = text.split(' ')
    decrypted_text = ''
    for encrypted_code in encrypted_codes:
        code = (int(encrypted_code))
        decrypted_text += chr(code)
    return decrypted_text


def list_start(list, symbol):
    for item in list:
        if isinstance(item, str) and item.startswith(symbol):
            return item
        else:
            raise ValueError


def weather():
    url = "http://www.weather.com.cn/weather/101280601.shtml"
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78"}
        response = requests.get(url, headers=headers)  # 发起请求
        data = response.content.decode("utf-8")  # 获得响应体并解码
        soup = BeautifulSoup(data, "lxml")
        lis = soup.select("ul[class='t clearfix'] li")
        x = 0
        for li in lis:
            try:
                date = li.select('h1')[0].text
                weather = li.select('p[class="wea"]')[0].text
                if x == 0:  # 为今天只有一个温度做判断 <i>14℃</i>
                    x += 1
                    temp = li.select('p[class="tem"] i')[0].text
                else:
                    temp = li.select('p[class="tem"] span')[0].text + " ~ " + li.select('p[class="tem"] i')[0].text
                print(date, weather, temp)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)


def lat_and_lon():
    # 使用ipinfo.io的API获取当前IP地址的地理位置信息
    url = 'https://ipinfo.io/json'
    response = requests.get(url)
    data = response.json()

    # 从返回的JSON数据中提取经纬度信息
    coordinates = data['loc'].split(',')
    latitude = coordinates[0]
    longitude = coordinates[1]

    # 返回经纬度
    return latitude, longitude


def trans(fanyi):
    url = f'https://cn.linguee.com/%E4%B8%AD%E6%96%87-%E8%8B%B1%E8%AF%AD/search?source=auto&query=/{fanyi}'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    fruit_list = soup.find_all('a', class_='dictLink featured')
    for _ in fruit_list:
        return fruit_list


def value1(value):
    if isinstance(value, str):
        num = 'str'
    elif isinstance(value, int):
        num = 'int'
    elif isinstance(value, float):
        num = 'float'
    else:
        raise ValueError
    return num


def value2(value):
    global num
    if value.isdigit():
        num = int(value)
    elif re.match(r'^[-+]?(\d+(\.\d*)?|\.\d+)$', value):
        num = float(value)
    return num


def value3(value):
    if value.isdigit():
        num = 'int'
    elif re.match(r'^[-+]?(\d+(\.\d*)?|\.\d+)$', value):
        num = 'float'
    else:
        num = 'str'
    return num


def value4(value):
    ret = str(value)
    if '.' in ret and ret.count('.') == 1:
        temp_array = ret.split('.')
        one = temp_array[0]
        two = temp_array[1]
        if one.isdigit() and two.isdigit():
            xiao_shu = int(two)
            if xiao_shu == 0:
                ret = int(one)
            else:
                ret = float(value)
    elif ret.isdigit():
        ret = int(ret)

    return ret


def other(value, zifu):
    pattern = rf'[^0-9{zifu}]'  # 匹配非数字和非小数点的字符
    result = re.findall(pattern, value)
    return ''.join(result)


def other2(value, zifu):
    value = str(value)
    zifu = str(zifu)
    pattern = rf'[^{zifu}]'  # 匹配非数字和非小数点的字符
    result = re.findall(pattern, value)
    return ''.join(result)


def is_same_characters(string):
    unique_chars = set(string)  # 将字符串转换为集合，去除重复字符
    return len(unique_chars) == 1  # 如果集合中只有一个独特的字符，则返回 True，否则返回 False


def check_same_elements(lst):
    return len(set(lst)) == 1 and len(lst) == len(set(map(str, lst)))


def last(value):
    value = str(value)
    last = value[-1]
    return last


#  1. 如果结果的小数部分是一个循环的话，就在第一次循环的最后一个数字后打6个 '.' ，
#     比如小数部分是 '123123123' ，那就简化成 '123......'
#  2. 如果不是的话，就直接用eval()来算
def calculate(value):
    value = str(value)
    table1 = []
    table1.clear()
    if '/' not in value:
        outcome = str(value4(eval(value)))
        return outcome
    elif '/' in value:
        zifu = other(value, '.')
        if last(zifu) == '/':
            old_outcome = str(value4(eval(value)))
            print(f'old_outcome = {old_outcome}|v = {eval(value)}')
            if '.' not in old_outcome:
                return old_outcome
            else:
                if len(old_outcome) <= 4:
                    return old_outcome
                old_outcome2 = old_outcome[:-2]
                character = '.'
                index = old_outcome2.index(character)  # 获取字符在字符串中的索引位置
                decimal_part = old_outcome2[index + 1:]  # 使用切片操作符获取右边部分
                integer_part = old_outcome2[:index]
                zifu = '...'
                if is_same_characters(decimal_part):
                    outcome = str(integer_part + '.' + decimal_part[0] + zifu)
                    return outcome
                else:
                    return old_outcome


def delete_str(value, delete):
    value = str(value)
    wei_zhi1 = value.find(delete)
    wei_zhi2 = wei_zhi1 + len(delete)
    jieguo = value[:wei_zhi1] + value[wei_zhi2:]
    return jieguo


def MoveRight(string, char):
    string = str(string)
    char = str(char)

    # 找到字符在字符串中的位置
    index = string.find(char)

    # 如果字符不存在或在字符串末尾，则无需移动
    if index == -1 or index == len(string) - 1:
        return string

    # 将字符向右移动一个位置
    moved_string = string[:index] + string[index + 1] + string[index] + string[index + 2:]
    return moved_string


def MoveLeft(string, char):
    string = str(string)
    char = str(char)

    # 找到字符在字符串中的位置
    index = string.find(char)

    # 如果字符不存在或在字符串开头，则无需移动
    if index == -1 or index == 0:
        return string

    # 将字符向左移动一个位置
    moved_string = string[:index - 1] + string[index] + string[index - 1] + string[index + 1:]
    return moved_string


def erase(string, char):
    string = str(string)
    char = str(char)

    # 找到字符在字符串中的位置
    index = string.find(char)

    # 如果字符不存在或在字符串开头，则无需删除
    if index == -1 or index == 0:
        return string

    # 删除第二个参数左边的一个字符
    erased_string = string[:index - 1] + string[index:]
    return erased_string
