from colored import Fore
from googletrans import Translator


def trans():
    print(Fore.YELLOW + '')
    # 创建翻译器对象
    translator = Translator(service_urls=['translate.google.com'])
    # 支持的语言代码
    LANGUAGES = {
        'en': '英语',
        'zh-CN': '中文（简体）',
        'ja': '日语',
    }

    def translate(text, dest_lang):
        result = translator.translate(text, dest=dest_lang)
        # 输出翻译结果
        return result.text

    # 测试
    n = 1
    while True:
        try:
            # 输入要翻译的文本
            print('------------------------------第 {} 次------------------------------'.format(n))
            text = input('请输入要翻译的文本（输入 q 退出）：')
            if text == 'q':
                print('已退出')
                break
            # 获取目标语言
            print('支持的语言代码：')
            for code, lang in LANGUAGES.items():
                print(code, '-', lang)
            dest_lang = input('请输入目标语言代码：')
            # 翻译文本
            result = translate(text, dest_lang)
            # 输出翻译结果
            print('翻译结果：', result)
            n = n + 1
        except ValueError as e:
            print('错误：' + str(e))
            n = n + 1
        except Exception as e:
            print('错误：' + str(e))
            n = n + 1


if __name__ == '__main__':
    trans()
