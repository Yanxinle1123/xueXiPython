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


def play():
    print("现在是一个可以加密和解密的程序")
    while True:
        huoqu = input("请输入要加密的内容(输入q退出)：")
        if huoqu == 'q' or huoqu == '退出' or huoqu == 'tuichu':
            print("已退出")
            break
        try:
            shift_value = 3

            encrypted_text = encrypt(huoqu, shift_value)
            print("密文：", encrypted_text)

            miwen = input("请输入要解密的内容：")
            decrypted_text = decrypt(miwen, shift_value)
            print("明文:", decrypted_text)
            print("---" * 10)
            print("再来一次吧")
        except:
            print("程序运行异常,请重新输入")


if __name__ == "__main__":
    play()
