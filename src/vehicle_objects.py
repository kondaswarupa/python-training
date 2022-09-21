class Vehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 16
        self.fuel_level = 0

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print('Gas tank is now full.')

    def drive(self):
        print(f'The {self.model} is now driving.')

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model, type)
        self.battery_size = 85
        self.charge_level = 0

    def charge(self):
        self.charge_level = 100
        print('The vehicle is now charged.')

    def fuel_up(self):
        print('This vehicle has no fuel tank!')

# Polymorphism
class PetrolVehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.vehicle_type = 'Petrol'
        self.gas_tank_size = '2litres'

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print(f'Fuel tank is now full for {self.vehicle_type} type vehicle.')

    def drive(self):
        print(f'The {self.model} of {self.vehicle_type} type is now driving.')

class DieselVehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.vehicle_type = 'Diesel'
        self.gas_tank_size= '2litres'

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print(f'Fuel tank is now full for {self.vehicle_type} type vehicle.')

    def drive(self):
        print(f'The {self.model} of {self.vehicle_type} type is now driving.')


petrol_vehicle = PetrolVehicle('Hyundai', 'Verna', '1.6SX')
diesel_vehicle = DieselVehicle('Hyundai', 'Verna', '1.6D')

for vehicle in (petrol_vehicle, diesel_vehicle):
    vehicle.fuel_up()
    vehicle.drive()
    print('\r')


from math import pi
class Shape:
   def __init__(self, name):
        self.name = name
   def area(self):
        pass
   def fact(self):
        return "I am a two-dimensional shape."
   def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

a = Square(4)
b = Circle(7)
print(b)
print(a)
print(b.fact())
print(a.fact())
print(b.area())
print(a.area())

## Encapsulation

class PetrolVehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model		#	Public Member (Accessible within or outside class)
        self._type = type		#	Protected Member (Accessible within the class and subclasses)
        self.__vehicle_type = 'Petrol'	#	Private Member (Accessible withing the class)

## Public method to access private members

class PetrolVehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.__vehicle_type = 'Petrol'
        self.gas_tank_size = 20
    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print(f'Fuel tank is now full for {self.__vehicle_type} type vehicle.')

petrol_vehicle = PetrolVehicle('Verna', 'Fludic', '1.6SX')
print('\r')
petrol_vehicle.fuel_up()

##  Name Mangling to access private members
## _classname__dataMember

print(petrol_vehicle.brand)
print(petrol_vehicle._PetrolVehicle__vehicle_type)
print('\r')
## getters and setters

class PetrolVehicle:

    __brand= 'BMW'
    def getbrand (self):
        return self.__brand

    def setbrand (self,brand):
        self.__brand= brand + '\ni10 series'

a= PetrolVehicle()

print(a.getbrand())
a.setbrand("Hyundai")
print(a.getbrand())

