from car1 import Car

car = Car('audi', 'a4', 2024)
print(car.get_descriptive_name())

car.odometer_reading = 23
car.read_odometer()
