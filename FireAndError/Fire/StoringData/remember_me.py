import json
from pathlib import Path


def get_stored_username(path):
    """如果用户名已经存储, 返回它"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """提示用户输入用户名"""
    username = input("请输入你的名字:")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """问候用户, 并说出他的名字"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"欢迎回来, {username}")
    else:
        username = get_new_username(path)
        print(f"你的名字已经被保存下来了, {username}")


if __name__ == '__main__':
    greet_user()
