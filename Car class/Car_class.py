# Setup class Car
class Car():
    # Car's attributes
    def __init__(self, year_model, make, speed = 0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
    # Car's methods
    def accelerate_car(self): # The accelerate method should add 5 to the speed data attribute each time it is called.
        return self.__speed + 5
    def brake_car(self): # The brake method should subtract 5 from the speed data attribute each time it is called.
        return self.__speed - 5
    def get_speed(self): # The get_speed method should return the current speed.
        return self.__speed
    