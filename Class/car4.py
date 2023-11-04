from car2 import ElectricCar

leaf = ElectricCar('nissan', 'leaf', 2024)
print(leaf.get_descriptive_name())
leaf.battery.describe_battery()
leaf.battery.get_range()
