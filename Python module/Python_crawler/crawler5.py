import requests
from bs4 import BeautifulSoup


def tianqi():
    url = "http://www.weather.com.cn/weather/101280601.shtml"
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78"}
        response = requests.get(url, headers=headers)  # 发起请求
        data = response.content.decode("utf-8")  # 获得响应体并解码
        soup = BeautifulSoup(data, "html.parser")
        lis = soup.find('ul', class_='t clearfix').find_all('li')
        x = 0
        for li in lis:
            try:
                date = li.find('h1').text
                weather = li.find('p', class_='wea').text
                if x == 0:  # 为今天只有一个温度做判断 <i>14℃</i>
                    x += 1
                    temp = li.find('p', class_='tem').find('i').text
                else:
                    temp = li.find('p', class_='tem').find('span').text + " ~ " + li.find('p', class_='tem').find(
                        'i').text

                wind = f"风力{li.find('p', class_='win').find('i').text}"
                print(date, weather, temp, wind)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    tianqi()
