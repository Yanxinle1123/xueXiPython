from googletrans import Translator


def translate_text(text, src='zh-cn', dest='en'):
    translator = Translator()
    translation = translator.translate(text, src=src, dest=dest)

    return translation.text


if __name__ == '__main__':
    chinese_text = "你好，世界！"
    english_text = translate_text(chinese_text)
    print(f"Chinese: {chinese_text}")
    print(f"English: {english_text}")

    # 反向翻译
    english_text = "Hello, world!"
    chinese_text = translate_text(english_text, src='en', dest='zh-cn')
    print(f"English: {english_text}")
    print(f"Chinese: {chinese_text}")
