import requests
from bs4 import BeautifulSoup

list = []
for i in range(2, 21):
    # 发送HTTP请求，获取网页内容
    url = 'https://chengyu.bmcx.com/nhu3w_' + str(i) + '__chengyulist/'
    response = requests.get(url)
    html_content = response.content

    # 解析HTML网页
    soup = BeautifulSoup(html_content, 'html.parser')
    fruit_list = soup.find('div', {'id': 'main_content'}).find_all('a')
    fruit_names = [fruit.text for fruit in fruit_list]
    index1 = fruit_names.index("成语填空")
    index2 = fruit_names.index("首页")
    new_names = fruit_names[index1 + 1:index2]
    list.extend(new_names)
    # print(new_names)
print(list)
