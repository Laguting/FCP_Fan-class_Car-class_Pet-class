# Laguting, Maricon Jane G.
# BSCpE 1-4
# Task: follow the instructions for pet class exercise in module 6: encapssulation and abstraction
from Designs import designs
from Pet_class import Pet
class tesPet():
# Designs
    de_1 = designs("","","","")
    print(de_1.get_brand()) # Display of the brand
    print(de_1.show_welcome()) # Welcome the user
    print(de_1.loading_bar()) # show the initiation of the program
# User input
    usr_pet = Pet()
    # Name of the user
    ask_usr = input("\33[34m\33[1m What is your name?: 33[0m")
    print("\33[31m\33[1m                                                               ", ask_usr "'s pet is a:  \33[0m")
    print("\33[32m                                                                           Name: ", usr_pet.get_name())
    print("\33[33m                                                                           Animal type: ", usr_pet.get_animaltype())
    print("\33[34m                                                                           Age: ", usr_pet.get_age())
# Close the program
    print(de_1.closing_fan())