from Pet_class import Pet
change = Pet("","","")
# Setup User  Interface
class user_interface():
    def __init__(self, pet_name, pet_animal_type, pet_age, display):
        self.__pet_name = pet_name
        self.__pet_animal_type = pet_animal_type
        self.__pet_age = pet_age
        self.__display_inputs = display
    # Name of the user's pet
    def get_pet_name(self):
        name = input("\33[32m\33[1m Please input your pet's name: \33[0m")
        change.set_name(name)
        return self.__pet_name
    # Animal type of the user's pet
    def get_pet_animal_type(self):
        animal_type = input("\33[33m\33[1m What type of animal is your pet?: \33[0m")
        change.set_animal_type(animal_type)
        return self.__pet_animal_type
    # Age of the user's pet
    def get_pet_age(self):
        age = input("\33[35m\33[1m Please input your pet's age: \33[0m")
        change.set_age(age)
        return self.__pet_age
    def display_inputs(self):
        print("\33[32m                                                                           Name: ", change.get_name())
        print("\33[33m                                                                           Animal type: ", change.get_animal_type())
        print("\33[34m                                                                           Age: ", change.get_age())
        return self.__display_inputs
