import requests
from bs4 import BeautifulSoup

# 发送HTTP请求，获取网页内容
url = 'http://www.gaosan.com/gaokao/239538.html'
response = requests.get(url)
html_content = response.content

# 解析HTML网页，获取水果单词
soup = BeautifulSoup(html_content, 'html.parser')
fruit_list = soup.find('div', {'id': 'data239538'}).find_all('p')
fruit_names = [fruit.text for fruit in fruit_list]
print(fruit_names)

# index = fruit_names.index("最")
# 输出水果单词
# last_list = fruit_names[index + 1:]
# last_str = ''
# last_china = ''
# for one in last_list:
#     if one.startswith('字母') or one.startswith('各种'):
#         continue
#     temp_array = one.lower().strip().split(' ')
#     if len(temp_array) > 1:
#         english = temp_array[0]
#         china = temp_array[1]
#         if not is_chinese_start(china):
#             continue
#         one_str = "'" + china + "':'" + english + "'"
#         last_str += one_str + ', '
#         last_china += "'" + china + "',"
#         print(one_str)
# print('last_str = \n' + last_str)
# print('last_china = \n' + last_china)
