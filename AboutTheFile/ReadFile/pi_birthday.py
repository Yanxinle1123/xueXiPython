import sys
from pathlib import Path

fire = 'pi_million_digits.txt'

try:
    path = Path(fire)
    contents = path.read_text()

    lines = contents.splitlines()
    pi_string = ''
    for line in lines:
        pi_string += line.lstrip()

    birthday = input('请输入您的生日, 格式为 年-月-日 :')
    if birthday in pi_string:
        print('您的生日在圆周率中出现了!')
    else:
        print('您的生日在圆周率中没有出现')
except FileNotFoundError:
    sys.stderr.write(f'FileNotFoundError: 文件 {fire} 未找到\n')
