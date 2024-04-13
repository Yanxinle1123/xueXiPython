from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f'文件内容: {pi_string}')
print(f'此文件包含{len(pi_string)}个字符')
