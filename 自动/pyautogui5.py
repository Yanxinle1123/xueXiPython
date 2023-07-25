import pyautogui

p = pyautogui
p.moveTo(830, 944)
p.click()
for i in range(5):
    p.write('a')
    p.press('space')
