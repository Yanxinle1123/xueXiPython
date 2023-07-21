def pingjunfen():
    while True:
        fenshu1 = float(input("请输入数字:"))
        fenshu2 = float(input('请输入数字:'))
        fenshu3 = float(input('请输入数字:'))
        junfen = (fenshu1 + fenshu2 + fenshu3) / 3
        print("平均数为：", junfen)


if __name__ == '__main__':
    pingjunfen()
