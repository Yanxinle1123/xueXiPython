s = [1.34, 1.27, 1.39, 1.41, 1.21]
n = len(s)
print("排序前：", s)
for i in range(0, n - 1):
    for j in range(0, n - 1 - i):
        if s[j] > s[j + 1]:
            t = s[j]
            s[j] = s[j + 1]
            s[j + 1] = t
print("排序后：", s)
