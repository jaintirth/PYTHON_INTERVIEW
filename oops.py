class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand                # to make private use __ before name of attribute,
        self.__model = model                  # only be accessed using getter method
        Car.total_car += 1                  # name of class can be used instead of self keyword 

    def fuel_type(self):                    # example of polymorphism , fuel type has different implementations in both
        return "Petrol or Diesal"           # car and electric car
    
    def get_brand(self):                   # getter method used to to access brand private attribute by an object
        return self.__brand
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    @staticmethod
    def general_description():            # static method does not require self keyword
        return "Cars are means of transport"       # they are helper func so we can use them without object instance
                                                # by calling using Class Name directly

    @property                       # it turns a method into getter for a managed attribute
    def model(self):                # allow controlled access, hiding implementation details
        return self.__model                   # getter


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)           # to inherit brand, model from Car 
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_car = Car("Tata", "Nexon")
# print(my_car.brand)
# print(my_car.full_name())

tesla_car = ElectricCar("Tesla", "Model S", "85 kWh")
# print(tesla_car.model)

my_new_car = Car("MG", "EV")
# print(my_new_car.get_brand())

# print(Car.total_car)

print(Car.general_description())
print(my_car.model)


print(isinstance(tesla_car, Car))
print(isinstance(tesla_car, Car))

class Battery():
    def battery_info(self):
        return "This is the battery"

class Engine():
    def engine_info(self):
        return "This is the engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model Y")
print(my_new_tesla.engine_info())


# MRO (Method Resolution Order is usefull when a class has multiple inheritance , 
# here the MRO will be Robot -> Mover -> Logger -> Object)


class Mover:
    def start(self):
        print("Mover: starting motors")
    def stop(self):
        print("Mover: stopping motors")
    def status(self):
        return "Mover: ready"

class Logger:
    def log(self, msg):
        print(f"LOG >> {msg}")
    def status(self):
        return "Logger: idle"

class Robot(Mover, Logger):
    def start(self):
        # Use both behaviors deliberately
        self.log("Robot start requested")
        super().start()  # follows MRO: calls Mover.start first
        self.log("Robot started")

    def stop(self):
        self.log("Robot stop requested")
        super().stop()   # follows MRO: calls Mover.stop first
        self.log("Robot stopped")

    def report(self):
        # Which status() runs?
        return super().status()  # due to MRO, this resolves to Mover.status

r = Robot()
r.start()
print(r.report())
r.stop()


print("----------------------------------")

# another example to understand MRO
class Base:
    def __init__(self):
        print("Base init")

class Left(Base):
    def __init__(self):
        print("Left init (before)")
        super().__init__()
        print("Left init (after)")

class Right(Base):
    def __init__(self):
        print("Right init (before)")
        super().__init__()
        print("Right init (after)")

class Child(Left, Right):
    def __init__(self):
        print("Child init (before)")
        super().__init__()  # walks Left -> Right -> Base once
        print("Child init (after)")

Child()
