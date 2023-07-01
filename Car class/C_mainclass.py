# Laguting, Maricon Jane G.
# BSCpE 1-4
# Task: follow the instructions for car class exercise in module 6: encapssulation and abstraction
from Car_class import Car
from Designs import designs
class testCar():
# Designs
    de_1 = designs("","","","")
    print(de_1.get_brand()) # Display of the brand
    print(de_1.show_welcome()) # Welcome the user
    print(de_1.loading_bar()) # show the initiation of the fan
# Test Car
# Close the program
    print(de_1.closing_fan())