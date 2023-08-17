from comm.common import *


def translated():
    orange_print('这是一个可以翻译的程序')
    c = 1
    a = 1
    while True:
        green_print(f'-------------------------------- 第 {c} 次 --------------------------------')
        huoqu = yellow_input2('请输入要翻译的内容(输入q退出):')
        if huoqu == 'q':
            orange_print('已退出')
            break
        fanyi = huoqu
        url = f'https://cn.linguee.com/%E4%B8%AD%E6%96%87-%E8%8B%B1%E8%AF%AD/search?source=auto&query=/{fanyi}'
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        fruit_list = soup.find_all('a', class_='dictLink featured')
        print(url)
        for fruit in fruit_list:
            purple_print(f'翻译结果{a}:')
            print(f'{fruit.text}')
            a += 1
        c += 1


if __name__ == '__main__':
    translated()
