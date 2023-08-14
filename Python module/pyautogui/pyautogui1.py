import time

import pyautogui

time.sleep(2)

# 设置输出速度为0.1秒/字符
pyautogui.PAUSE = 0.01

# 将要输出的文本存储到字符串中
text = 'Hello, World!'

# 输出文本
pyautogui.typewrite(text)
