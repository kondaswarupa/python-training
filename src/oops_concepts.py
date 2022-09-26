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




vehicle_obj = Vehicle('BMW', 'C Series', 'Truck')

print(vehicle_obj.brand)
print(vehicle_obj.model)
print(vehicle_obj.type)

vehicle_obj.fuel_up()
vehicle_obj.drive()



class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model, type)
        self.battery_size = 85
        self.charge_level = 0

    def charge(self):
        self.charge_level = 100
        print('The vehicle is now charged.')


electric_vehicle = ElectricVehicle('Tesla', 'Tata', 'Mahindra')
electric_vehicle.charge()
electric_vehicle.drive()


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

class Battery:
    def __init__(self, size=85):
        self.size = size
        self.charge_level = 0

    def get_range(self):
        if self.size == 85:
            return 260
        elif self.size == 100:
            return 315

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model, type)
        self.battery = Battery()

    def charge(self):
        self.battery.charge_level = 100
        print('The vehicle is fully charged.')

electric_vehicle = ElectricVehicle('Tesla', 'CyberTruck', 'Truck')
electric_vehicle.charge()
print(electric_vehicle.battery.get_range())
electric_vehicle.drive()
print('\r')



from vehicle_objects import Vehicle, ElectricVehicle
a_mini = Vehicle('Cooper','Mini','Car')
a_mini.fuel_up()
a_mini.drive()
a_tesla = ElectricVehicle('Telsa','ModelX','Electric')
a_tesla.charge()
a_tesla.drive()

#import vehicle
a_mini = Vehicle('Cooper', 'Mini', 'Car')
a_mini.fuel_up()
a_mini.drive()
a_tesla = ElectricVehicle('Tesla', 'Model X', 'Electric')
a_tesla.charge()
a_tesla.drive()

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass
class ElectricVehicle(Vehicle):
    def drive(self):
        print("Driving Electric Vehicle")
class PetrolVehicle(Vehicle):
    def drive(self):
        print("Driving Petrol Vehicle")
#------------------------------------------
electric_vehicle= ElectricVehicle()
electric_vehicle.drive()
petrol_vehicle = PetrolVehicle()
petrol_vehicle.drive()


import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


import logging
# logger = logging.getLogger(__name__)
# logger.setLevel('DEBUG')
logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')


def myfun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myfun(first='python', second ='Java', third='C++')


#def myfun(*args):
#   for value in args.__add__():
#       print("%s " %  (value))


#myfun[1,2,3]
#logger = logging.getLogger(__name__)
#logger.setLevel('info')
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info("Admin logged in")


import logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')

import logging
name = 'John'
logging.error('%s raised an error', name)

import logging
name = 'John'
logging.error(f'{name} raised an error')


import logging
a = 5
b = 0
try:
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)