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