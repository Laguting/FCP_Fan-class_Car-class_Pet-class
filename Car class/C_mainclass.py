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
    print(de_1.loading_bar()) # show the initiation of the program
# Test Car
    car_obj = Car (2021,"A3THER", 0)
    print("\33[31m\33[1m                                                                      -------------CAR's:------------------ \33[0m")
    print("\33[34m                                                                           Year Model: ", car_obj.get_yearmodel())
    print("\33[35m                                                                           Made By: ", car_obj.get_make())
    #  After each call to the accelerate method, get the current speed of the car and display it.
    print("\33[31m\33[1m                                                                      --------CAR's ACCELERATION---------- \33[0m")
    for i in range(5):
        car_obj.accelerate_car()
        print("\33[32m                                                                           Current Speed: ", car_obj.get_speed())
    # Then call the brake method five times. After each call to the brake method, get the current speed of the car and display it.
    print("\33[31m\33[1m                                                                      ------------CAR's BRAKE------------- \33[0m")
    for i in range (5):
        car_obj.brake_car()
        print("\33[33m                                                                           Current Speed: ", car_obj.get_speed())
# Close the program
    print(de_1.closing_fan())