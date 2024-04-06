from name_function import get_formatted_name

print("输入 q 退出\n")
while True:
    first = input("请输入名: ")
    if first == "q":
        print("已退出")
        break
    last = input("请输入姓: ")
    if last == "q":
        print("已退出")
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\t你的名字是: {formatted_name}\n")
