from comm.common import ord2, chr2, orange_print, purple_print, red_print, green_input, yellow_print, blue_print, \
    cyan_input


class Encrypt:
    def __init__(self, encrypted_text):
        self.encrypted_text = encrypted_text

    def encrypt(self):
        symmetry = {"0": "z", "1": "o", "2": "t", "3": "r", "4": "f", "5": "i", "6": "s", "7": "e", "8": "g",
                    "9": "n"}
        encrypted_text = []
        text = ord2(self.encrypted_text)
        for char in text:
            if char == ' ':  # 如果字符是空格，保留空格
                encrypted_text.append(char)
            else:
                encrypted_text += symmetry[str(char)]
        encrypted_text = ''.join(encrypted_text)
        return encrypted_text


class Decrypt:
    def __init__(self, decrypted_text):
        self.decrypted_text = decrypted_text

    def decrypt(self):
        symmetry = {"0": "z", "1": "o", "2": "t", "3": "r", "4": "f", "5": "i", "6": "s", "7": "e", "8": "g",
                    "9": "n"}
        decrypted_text = []
        for char in self.decrypted_text:
            if char == ' ':  # 如果字符是空格，保留空格
                decrypted_text.append(char)
            else:
                decrypted_text += [str(k) for k, v in symmetry.items() if v == char]
        decrypted_text = ''.join(decrypted_text)
        return chr2(decrypted_text)


def ead5():
    a = 1
    while True:
        try:
            purple_print(f"------------------------------------第 {a} 次------------------------------------")
            encrypted_text = green_input("请输入需要加密的字符(输入q退出): ")
            if encrypted_text == 'q':
                orange_print("已退出")
                break
            encrypt = Encrypt(encrypted_text)
            yellow_print(f"密文: {encrypt.encrypt()}")
            decrypted_text = cyan_input("请输入需要解密的字符(输入q退出): ")
            if decrypted_text == 'q':
                orange_print("已退出")
                break
            decrypt = Decrypt(decrypted_text)
            blue_print(f"明文: {decrypt.decrypt()}")
            a += 1
        except:
            red_print("输入错误")


orange_print("这是一个可以加密和解密的程序")
ead5()
