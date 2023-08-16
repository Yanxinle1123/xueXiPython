import requests
from bs4 import BeautifulSoup

# 发送HTTP请求，获取网页内容
fanyi = 'hello'
url = f'https://fanyi.baidu.com/#auto/zh/{fanyi}'
response = requests.get(url)
html_content = response.content
print(url)
# 解析HTML网页
soup = BeautifulSoup(html_content, 'html.parser')
fruit_list = soup.find('div', {'class': "main main-outer"}).find('div', {'class': 'main main-inner'}).find('div', {
    'class': 'inner'}).find('div', {'class': 'translate-wrap'}).find('div', {'class': 'translateio'}).find('div', {
    'class': 'translate-main clearfix'}).find('div', {'class': 'trans-right'}).find('div',
                                                                                    {'class': 'output-wrap'}).find(
    'div', {'class': 'output-mod ordinary-wrap'}).find('div', {'class': 'output-bd'}).find('p', {
    'class': "ordinary-output target-output clearfix"})
print(fruit_list)
