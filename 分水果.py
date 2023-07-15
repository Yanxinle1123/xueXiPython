remain = 100 - 20
monkey = remain * 0.25
remain = remain - monkey
deer = remain * 0.3
remain = remain - deer
bear = remain * 0.35
remain = remain - bear
fox = 20 + remain
print("猴子分到了", monkey, "千克水果")
print("小鹿分到了", deer, "千克水果")
print("小熊分到了", bear, "千克水果")
print("狐狸分到了", fox, "千克水果")
