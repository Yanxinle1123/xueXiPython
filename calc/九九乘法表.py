def mult_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            product = i * j
            print(f"{j} * {i} = {product}\t", end="")
        print()


if __name__ == '__main__':
    mult_table()
