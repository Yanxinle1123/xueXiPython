import requests
from bs4 import BeautifulSoup

# 发送HTTP请求，获取网页内容
url = 'https://www.futuu.com/post/1184.html'
response = requests.get(url)
html_content = response.content

# 解析HTML网页，获取水果单词
soup = BeautifulSoup(html_content, 'html.parser')
fruit_list = soup.find('div', {'class': "entry-content clearfix"}).find_all('p')
fruit_names = [fruit.text for fruit in fruit_list]

combined_list = []  # 创建一个空列表用于存储合并后的结果
for one in fruit_names:
    if one.startswith('成') or one.startswith('下'):
        continue
    temp_array = one.lower().strip().split(' ')
    temp_array = [word for word in temp_array if '+' not in word]  # 去掉带有加号的元素
    temp_array = [word for word in temp_array if word]  # 去掉空的列表
    combined_list.extend(temp_array)  # 将temp_array中的元素添加到combined_list中

print(combined_list)
