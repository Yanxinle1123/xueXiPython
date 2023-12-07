from comm.common import green_input, orange_print, yellow_print, blue_print, red_print, ord2, chr2


def ead4():
    try:
        while True:
            def encrypt(text):
                encrypted_text = []
                text = ord2(text)
                for char in text:
                    if char == ' ':  # 如果字符是空格，保留空格
                        encrypted_text.append(char)
                    else:
                        encrypted_text += symmetry[str(char)]
                encrypted_text = ''.join(encrypted_text)
                return encrypted_text

            def decrypt(text):
                decrypted_text = []
                for char in text:
                    if char == ' ':  # 如果字符是空格，保留空格
                        decrypted_text.append(char)
                    else:
                        decrypted_text += [str(k) for k, v in symmetry.items() if v == char]
                decrypted_text = ''.join(decrypted_text)
                return chr2(decrypted_text)

            symmetry = {"0": "z", "1": "o", "2": "t", "3": "r", "4": "f", "5": "i", "6": "s", "7": "e", "8": "g",
                        "9": "n"}
            value1 = green_input('请输入要加密的字符串(输入q退出):')
            if value1 == 'q':
                orange_print('已退出')
                break
            ciphertext = str(encrypt(value1))
            yellow_print(f'密文:{ciphertext}')
            value2 = green_input('请输入要解密的字符串(输入q退出):')
            if value2 == 'q':
                orange_print('已退出')
                break
            blue_print(f'明文:{decrypt(value2)}')
    except:
        red_print('输入有误')


if __name__ == "__main__":
    ead4()
