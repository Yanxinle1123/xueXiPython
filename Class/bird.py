class Bird:
    def __init__(self, name, color, start_point, end_point):
        self.name = name
        self.color = color
        self.start_point = start_point
        self.end_point = end_point

    def __str__(self):
        return f"这是一只鸟，名字是{self.name}，它是{self.color}的，它要从{self.start_point}飞到{self.end_point}"

    def fly(self):
        print(f"{self.name}用翅膀飞")

    def eat(self):
        print(f"{self.name}饿了")


class Goose(Bird):

    def eat(self):
        super().eat()
        print(f"{self.name}吃到了鱼\n")


class Sparrow(Bird):

    def eat(self):
        super().eat()
        print(f"{self.name}吃到了蚯蚓")


bird = Goose('天鹅', '白色', '池塘', '草地')
print(bird)
bird.eat()

bird = Sparrow('麻雀', '灰色', '河边', '树上')
print(bird)
bird.eat()
