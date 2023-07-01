class Fan():
    slow = 1
    medium = 2
    fast = 3
    def __init__(self, speed = 1, power = False, radius = 5, color = "Blue"):
        self.__speed = speed
        self.__power = power
        self.__radius = radius
        self.__color = color
    
