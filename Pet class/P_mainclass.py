# Laguting, Maricon Jane G.
# BSCpE 1-4
# Task: follow the instructions for pet class exercise in module 6: encapssulation and abstraction
from Designs import designs
from User_Iterface import user_interface
class tesPet():
# Designs
    de_1 = designs("","","","")
    print(de_1.get_brand()) # Display of the brand
    print(de_1.show_welcome()) # Welcome the user
    print(de_1.loading_bar()) # show the initiation of the program
# User input
    # Name of the user
    ui_inputs = user_interface("","","","")
    ask_usr = input("\33[34m\33[1m What is your name?: \33[0m")
    print(ui_inputs.get_pet_name())
    print(ui_inputs.get_pet_animal_type())
    print(ui_inputs.get_pet_age())
# Display the inputs
    print("\33[31m\33[1m                                                                     ", ask_usr, "'s pet identification:  \33[0m")
    print(ui_inputs.display_inputs())
# Close the program
    print(de_1.closing_fan())