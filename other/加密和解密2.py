from colored import Fore


def encrypt(text):
    encrypted_text = ""
    for char in text:
        code = ord(char)
        encrypted_code = str(code * 10 + 5)
        encrypted_text += encrypted_code + ","
    return encrypted_text[:-1], encrypted_text.count(",")


def decrypt(text):
    encrypted_codes = text.split(",")
    decrypted_text = ""
    for encrypted_code in encrypted_codes:
        code = (int(encrypted_code) - 5) // 10
        decrypted_text += chr(code)
    return decrypted_text


def ead2():
    print(Fore.RGB(255, 170, 0) + "现在是一个可以加密和解密的程序")
    r = 1
    while True:
        print(Fore.RGB(125, 250,
                       85) + '----------------------------------------第 {} 次----------------------------------------'.format(
            r))
        huoqu = input("请输入要加密的内容(输入q退出): ")
        if huoqu == 'q':
            print(Fore.RGB(255, 170, 0) + "已退出")
            break
        try:
            encrypted_text, length = encrypt(huoqu)
            print(Fore.RGB(225, 255, 0) + "密文长度：", length)
            print(Fore.RGB(50, 150, 225) + "密文：", encrypted_text)
            miwen = input(Fore.RGB(125, 250, 85) + "请输入要解密的内容(输入q退出): ")
            if miwen == 'q':
                print(Fore.RGB(255, 170, 0) + "已退出")
                break
            decrypted_text = decrypt(miwen)
            print(Fore.RGB(225, 255, 0) + "明文:", decrypted_text)
            r = r + 1
        except:
            print(Fore.RGB(225, 0, 50) + "输入有误")


if __name__ == '__main__':
    ead2()
