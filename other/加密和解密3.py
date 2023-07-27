import random

from colored import Fore

chengshu = random.randint(10, 60)

list = []
if len(list) == 0:
    list.clear()
else:
    chushu_str = list[0]
    chushu = int(chushu_str)


def encrypt(text):
    encrypted_text = ""
    for char in text:
        code = ord(char)
        encrypted_code = str(code * chengshu)
        encrypted_text += encrypted_code + ","
    return encrypted_text[:-1], encrypted_text.count(",")


def decrypt(text):
    encrypted_codes = text.split(",")
    decrypted_text = ''
    for encrypted_code in encrypted_codes:
        code = (int(encrypted_code)) // chengshu
        decrypted_text += chr(code)
    return decrypted_text


def ead3():
    print(Fore.RGB(255, 170, 0) + '这是一个可以加密解密的程序')
    r = 1
    while True:
        print(Fore.RGB(125, 250,
                       85) + '----------------------------------------第 {} 次----------------------------------------'.format(
            r))
        huoqu = input('请输入要加密的内容(输入q退出):')
        list.clear()
        if huoqu == 'q':
            print(Fore.RGB(255, 170, 0) + "已退出")
            break
        try:
            encrypted_text, length = encrypt(huoqu)
            print(Fore.RGB(225, 255, 0) + "密文长度:", length)
            print(Fore.RGB(255, 170, 0) + '密钥:', chengshu)
            print(Fore.RGB(50, 150, 225) + "密文:", encrypted_text)
            miwen = input(Fore.RGB(125, 250, 85) + "请输入要解密的内容(输入q退出): ")
            if miwen == 'q':
                print(Fore.RGB(255, 170, 0) + "已退出")
                break
            miyao = input('请输入密钥:')
            list.append(miyao)
            decrypted_text = decrypt(miwen)
            print(Fore.RGB(225, 255, 0) + "明文:", decrypted_text)
            list.clear()
            r = r + 1
        except:
            print(Fore.RGB(225, 0, 50) + "输入有误")


if __name__ == '__main__':
    ead3()
