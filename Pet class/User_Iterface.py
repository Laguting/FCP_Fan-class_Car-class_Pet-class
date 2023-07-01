from Pet_class import Pet
# Setup User  Interface
class User_Interface():
    pet_changeatt = Pet()
    # Name of the user's pet
    name = input("\33[32m\33[1m Please input your pet's name: \33[0m")
    pet_changeatt.set_name(name)
    # Animal type of the user's pet
    animal_type = input("\33[33m\33[1m What type of animal is your pet?: \33[0m")
    pet_changeatt.set_name(animal_type)
    # Age of the user's pet
    age = input("\33[32m\33[1m Please input your pet's age: \33[0m")
    pet_changeatt.set_name(age)