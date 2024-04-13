from pathlib import Path


def count_words(path):
    """计算文件中包含的大概单词数"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        # 计算文件中的大概单词数:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
             'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
