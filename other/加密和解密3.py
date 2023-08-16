import random

from colored import Fore

from comm.common import orange_print, green_input, blue_print, red_print, purple_print


def encrypt(text, chengshu, jiashu):
    encrypted_text = ""
    for char in text:
        code = ord(char)
        encrypted_code = str(code * chengshu + jiashu)
        encrypted_text += encrypted_code + ","
    return encrypted_text[:-1], encrypted_text.count(",")


def decrypt(text, miyao, miyao2):
    encrypted_codes = text.split(",")
    decrypted_text = ''
    for encrypted_code in encrypted_codes:
        code = (int(encrypted_code) - miyao2) // miyao
        decrypted_text += chr(code)
    return decrypted_text


def ead3():
    orange_print('这是一个可以加密解密的程序')
    r = 1
    while True:
        chengshu = random.randint(50, 1000)
        jiashu = random.randint(50, 100)
        purple_print(
            '----------------------------------------第 {} 次----------------------------------------'.format(r))
        huoqu = green_input('请输入要加密的内容(输入q退出):')
        if huoqu == 'q':
            orange_print("已退出")
            break
        try:
            encrypted_text, length = encrypt(huoqu, chengshu, jiashu)
            print(Fore.RGB(225, 255, 0) + "密文长度: ", length)
            print(Fore.RGB(255, 170, 0) + '密钥 1: ', chengshu)
            print('密钥 2: ', jiashu)
            blue_print("密文: " + encrypted_text)
            miwen = input(Fore.RGB(125, 250, 85) + "请输入要解密的内容(输入q退出): ")
            if miwen == 'q':
                orange_print("已退出")
                break
            miyao = input('请输入密钥 1: ')
            miyao2 = input('请输入密钥 2: ')
            decrypted_text = decrypt(miwen, int(miyao), int(miyao2))
            print(Fore.RGB(225, 255, 0) + "明文: ", decrypted_text)
            r = r + 1
        except:
            red_print("输入有误")


if __name__ == '__main__':
    ead3()
