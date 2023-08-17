import time

import pyautogui

time.sleep(4)

# 将翻译后的英文文本分行存储到列表中
text = ['Do You Not See the Yellow River\'s Waters Rise Up to the Skies,',
        'And Rush Down to the Sea, Never to Return?',
        'Do You Not See the Bright Hall\'s Mirrors Reflecting White Hair,',
        'As Morning\'s Black Tresses Turn to Evening\'s Snowflakes?',
        'While Life is Good, One Should Enjoy It to the Fullest,',
        'And Not Let the Golden Goblet Stand Empty Before the Moon.',
        'By Nature I am Talented and Capable,',
        'Even if I Squander My Fortune, It Will Come Back to Me.',
        'Slaughtering Sheep and Butchering Cattle are Sources of Joy,',
        'And We Shall Drink Three Hundred Cups in Celebration.',
        'Cen and Danish, Sons of Heaven, Let Us Drink Without Restraint,',
        'And I Shall Sing a Song, Hoping You Will Listen.',
        'Jade Dishes and Golden Bells are Not Enough to Show Luxury,',
        'May We Drink and Be Drunk Without Waking Up.',
        'Since Ancient Times, Saints and Sages Have All Died,',
        'Only Drinkers\' Names Remain.',
        'Chen and Wang Once Banqueted in the Peaceful Joy Palace,',
        'A Thousand Cups of Wine, Laughter and Jokes.',
        'Why Speak of Little Wealth, O Host,',
        'Just Pour and Serve Me, and Let Me Toast.',
        'Five Horses and a Thousand Gold Pieces for a Fur Coat,',
        'Come, Boy, and Exchange Them for Fine Wine,',
        'And Together We Shall Vanquish Eternal Sorrows.']

# 循环输出每一行文本
for line in text:
    pyautogui.typewrite(line)
    pyautogui.press('enter')
