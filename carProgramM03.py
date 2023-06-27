class Vehicle:

   def __init__(self, vehicle_type):

       self.vehicle_type = vehicle_type

class Automobile(Vehicle):

   def __init__(self, vehicle_type, year, make, model, doors, roof):

       super().__init__(vehicle_type)

       self.year = year

       self.make = make

       self.model = model

       self.doors = doors

       self.roof = roof

def create_car():

   vehicle_type = input("Enter the vehicle type: ")

   year = input("Enter the year of the vehicle: ")

   make = input("Enter the make of the vehicle: ")

   model = input("Enter the model of the vehicle: ")

   doors = input("Enter the number of doors (2 or 4): ")

   roof = input("Enter the type of roof (solid or sun roof): ")

   vehicle1 = Automobile(vehicle_type, year, make, model, doors, roof)

   return vehicle1

def display(vehicle1):

   print("Vehicle type:", vehicle1.vehicle_type)

   print("Year:", vehicle1.year)

   print("Make:", vehicle1.make)

   print("Model:", vehicle1.model)

   print("Number of doors:", vehicle1.doors)

   print("Type of roof:", vehicle1.roof)

vehicle1 = create_car()

print("Vehicle Information:" )
display(vehicle1)