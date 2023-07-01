# Setup class fan
class Fan():
    # Three constants name slow, medium, and fast
    slow = (1, " - Slow")
    medium = (2,  " - Medium")
    fast = (3,  " - Fast")
    # Four data fields setup as private members
    def __init__(self, speed = 1, power = False, radius = 5, color = "Blue"):
        self.__speed = speed
        self.__power = power
        self.__radius = radius
        self.__color = color
    # Speed of the fan
    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        self.__speed = speed
    # Boolean field to signify if the fan is on or off
    def get_power(self):
        return self.__power
    def set_power(self, on):
        self.__power = on
    # Radius of the fan
    def get_radius(self):
        return self.__radius
    def set_power(self, radius):
        self.__radius = radius
    # Color of the fan
    def get_color(self):
        return self.__color
    def set_power(self, color):
        self.__color = color
