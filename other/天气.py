import requests
from bs4 import BeautifulSoup


def weather():
    url = "http://www.weather.com.cn/weather/101280601.shtml"
    weather_data = []
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78"}
        response = requests.get(url, headers=headers)  # 发起请求
        data = response.content.decode("utf-8")  # 获得响应体并解码
        soup = BeautifulSoup(data, "lxml")
        lis = soup.select("ul[class='t clearfix'] li")
        x = 0
        for li in lis:
            try:
                date = li.select('h1')[0].text
                weather = li.select('p[class="wea"]')[0].text
                if x == 0:  # 为今天只有一个温度做判断 <i>14℃</i>
                    x += 1
                    temp = li.select('p[class="tem"] i')[0].text
                else:
                    temp = li.select('p[class="tem"] span')[0].text + " ~ " + li.select('p[class="tem"] i')[0].text
                weather_data.append({
                    'date': date,
                    'weather': weather,
                    'temperature': temp
                })
            except Exception as err:
                print(f"Error parsing data for one of the days: {err}")
    except Exception as err:
        print(f"Error fetching weather data: {err}")
    return weather_data


if __name__ == "__main__":
    weather_info = weather()
    print(weather_info)
    for day in weather_info:
        print(f"{day['date']}: {day['weather']}, 温度: {day['temperature']}")
