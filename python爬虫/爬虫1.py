import requests
from bs4 import BeautifulSoup

# 发送HTTP请求，获取网页内容
url = 'https://www.thoughtco.com/fruits-vocabulary-word-list-1212122'
response = requests.get(url)
html_content = response.content

# 解析HTML网页，获取水果单词
soup = BeautifulSoup(html_content, 'html.parser')
fruit_list = soup.find('div', {'class': 'entry-content'}).find_all('li')
fruit_names = [fruit.text.strip() for fruit in fruit_list]

# 输出水果单词
print(fruit_names)
