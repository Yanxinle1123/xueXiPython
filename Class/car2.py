"""一组用于表示燃油汽车和电动汽车的类"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'这辆车行驶了 {self.odometer_reading} 公里')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
        self.range = 0

    def describe_battery(self):
        print(f'这辆车有 {self.battery_size}-KWH 的电池容量')

    def get_range(self):
        if self.battery_size == 40:
            self.range = 150
        elif self.battery_size == 65:
            self.range = 225
        print(f'这辆车充满电后可以行驶约 {self.range} 公里')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

# leaf = ElectricCar('nissan', 'leaf', 2024)
# print(leaf.get_descriptive_name())
# leaf.battery.describe_battery()
# leaf.battery.get_range()
# print()
