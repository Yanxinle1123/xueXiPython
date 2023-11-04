from pathlib import Path

path = Path('pi_digits')
contents = path.read_text()
contents = contents.rstrip()
print(contents)
