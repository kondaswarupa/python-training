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

import vehicle
a_mini = Vehicle('Cooper', 'Mini', 'Car')
a_mini.fuel_up()
a_mini.drive()
a_tesla = ElectricVehicle('Tesla', 'Model X', 'Electric')
a_tesla.charge()
a_tesla.drive()

