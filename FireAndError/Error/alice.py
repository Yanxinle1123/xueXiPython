from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"抱歉, 文件 {path} 不存在")
else:
    # 计算文件大概包含多少个单词
    words = contents.split()
    num_words = len(words)
    print(f"文件 {path} 中大概包含 {num_words} 个单词")
