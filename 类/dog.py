class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name}现在坐下了')

    def roll_over(self):
        print(f'{self.name}现在在打滚')


my_dog = Dog('威力', 6)
your_dog = Dog('卢斯', 3)
print(f"我的狗的名字是{my_dog.name}")
print(f"我的狗有{my_dog.age}岁了")
my_dog.sit()
print(f"他的狗的名字是{your_dog.name}")
print(f"他的狗有{your_dog.age}岁了")
your_dog.roll_over()
