import json
from pathlib import Path

path = Path('username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"欢迎回来, {username}")
