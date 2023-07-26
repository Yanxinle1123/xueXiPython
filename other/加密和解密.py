from colored import Fore


def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        char_code = ord(char)
        if 0x4E00 <= char_code <= 0x9FFF or char.isascii():
            encrypted_text += chr((char_code + shift) % 0x10FFFF)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        char_code = ord(char)
        if 0x4E00 <= char_code <= 0x9FFF or char.isascii():
            decrypted_text += chr((char_code - shift) % 0x10FFFF)
        else:
            decrypted_text += char
    return decrypted_text


def ead():
    print(Fore.RGB(255, 170, 0) + "现在是一个可以加密和解密的程序")
    n = 1
    while True:
        print(Fore.RGB(125, 250, 85) + '------------------------------第 {} 次------------------------------'.format(n))
        huoqu = input("请输入要加密的内容(输入q退出):")
        if huoqu == 'q' or huoqu == '退出' or huoqu == 'tuichu':
            print(Fore.RGB(255, 170, 0) + "已退出")
            break
        try:
            shift_value = 3
            encrypted_text = encrypt(huoqu, shift_value)
            print(Fore.RGB(225, 255, 0) + "密文：", encrypted_text)
            miwen = input(Fore.RGB(125, 250, 85) + "请输入要解密的内容(输入q退出):")
            if miwen == 'q':
                print(Fore.RGB(255, 170, 0) + "已退出")
                break
            decrypted_text = decrypt(miwen, shift_value)
            print(Fore.RGB(225, 255, 0) + "明文:", decrypted_text)
            n = n + 1
        except:
            print(Fore.RGB(225, 0, 50) + "输入有误")


if __name__ == "__main__":
    ead()
