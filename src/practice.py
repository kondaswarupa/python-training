print ("Hello")

def check_sum(nums,k):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] ==k:
                return print ("output is", i,j)



print (check_sum([2,11,7,5,4],9))

list=[1,2,3,4,5]
print("\nTuple using list:")

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
print('\r')


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

## Overriding parent methods
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

    def __init__(self,brand, model, type):
        super().__init__(brand,model,type)
        self.battery = Battery()


    def charge(self):
        self.battery.charge_level=100
        print('The Vehicle is fully charged.')

# Using the instance
electric_vehicle = ElectricVehicle ('Tesla','CyberTruck','Truck')
print('\r')
electric_vehicle.charge()
print(electric_vehicle.battery.get_range())
electric_vehicle.drive()
