class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 25

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'这辆车行驶了 {self.odometer_reading} 公里')


car = Car('audi', 'a4', 2024)
print(f'这辆车是 {car.get_descriptive_name()}')
car.read_odometer()
