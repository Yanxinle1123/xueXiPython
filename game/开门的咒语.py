def kaimenyouxi():
    print("你来到了一个山洞前，山洞里有很多珠宝，可是想打开山洞的大门，就必须说出正确的咒语，快猜一猜吧！")
    while True:
        huoqu = input("请输入咒语（输入q退出）：")
        if huoqu == 'q':
            print("已离开大门")
            break
        if huoqu == "芝麻开门":
            print("咒语正确！")
            print("宝藏已开启")
            print("   ****   ****")
            print("  **************")
            print("  **************")
            print("    ***********")
            print("      *******")
            print("        ***")
            break
        if huoqu != "芝麻开门":
            print("咒语错误!")


if __name__ == '__main__':
    kaimenyouxi()
