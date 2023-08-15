def mult_table2():
    i = 1
    while i < 10:
        j = 1
        while j <= i:  # 更改条件为 j <= i
            print('%d * %d = %d' % (j, i, j * i), end='\t\t')  # 使用制表符（\t）分隔每个元素
            j += 1
        print('')
        i += 1


if __name__ == '__main__':
    mult_table2()
