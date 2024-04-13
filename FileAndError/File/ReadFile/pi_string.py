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

    print(f'文件内容 (小数点后50位) : {pi_string[:52]}...')
    print(f'此文件 (整个) 包含{len(pi_string)}个字符')
except FileNotFoundError:
    sys.stderr.write(f'FileNotFoundError: 文件 {fire} 未找到\n')
