from googletrans import Translator


def translate_text(text, src_lang, dest_lang):
    # 创建翻译器对象
    translator = Translator(service_urls=['translate.google.com'])

    # 翻译文本
    result = translator.translate(text, src=src_lang, dest=dest_lang)

    # 返回翻译结果
    return result.text


def validate_language(lang):
    # 验证语言选项
    valid_options = ['zh-CN', 'en']

    if lang in valid_options:
        return True
    else:
        return False


# 主循环
while True:
    print("请选择翻译方向：")
    print("1. 中文翻译为英文")
    print("2. 英文翻译为中文")
    print("输入 q 退出")

    option = input("请选择选项: ")

    if option == "1":
        src_lang = 'zh-CN'
        dest_lang = 'en'
    elif option == "2":
        src_lang = 'en'
        dest_lang = 'zh-CN'
    elif option.lower() == "q":
        print("程序已退出。")
        break
    else:
        print("无效的选项，请重新输入。")
        continue

    text = input("请输入要翻译的文本：")

    try:
        translated_text = translate_text(text, src_lang, dest_lang)
        print("翻译结果：", translated_text)
    except Exception as e:
        print("翻译发生错误:", str(e))

    print()  # 输出空行以提升可读性
