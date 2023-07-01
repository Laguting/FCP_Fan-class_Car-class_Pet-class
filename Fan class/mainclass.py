# Laguting, Maricon Jane G.
# BSCpE 1-4
# Task: follow the instructions for test fan exercise in module 6: encapssulation and abstraction
from Fan_class import Fan
from Designs import designs
class Testfan():
    # designs
    de_1 = designs("","","")
    print(de_1.get_brand()) # Display of the brand
    print(de_1.show_welcome()) # Welcome the user
    print(de_1.loading_bar()) # show the initiation of the fan
    # test fans
    fan_1 = Fan(speed = Fan.fast, power = True, radius = 10, color="Yellow")
    print("\33[31m\33[1m --------Fan 1---------- \33[0m")
    print("\33[32m Speed: ", fan_1.get_speed())
    print("\33[33m Power: ", fan_1.get_power())
    print("\33[34m Radius: ", fan_1.get_radius())
    print("\33[35m Color: ", fan_1.get_color())
    
