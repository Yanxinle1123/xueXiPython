import requests
from bs4 import BeautifulSoup

# 发送HTTP请求，获取网页内容
fanyi = 'hello'
url = f'https://cn.linguee.com/%E4%B8%AD%E6%96%87-%E8%8B%B1%E8%AF%AD/search?source=%E8%8B%B1%E8%AF%AD&query=/{fanyi}'
response = requests.get(url)
html_content = response.content
print(f'url={url}')
# 解析HTML网页
soup = BeautifulSoup(html_content, 'html.parser')
fruit_list = soup.find_all('a', class_='dictLink featured')

print(f'fruit_list={fruit_list}')

# 遍历解析
for fruit in fruit_list:
    print(f'one_text={fruit.text}')
