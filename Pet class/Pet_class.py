# Setup Pet class
class Pet():
    # Pet's attributes
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
# Methods
    # This method returns the value of the _ _ name field.
    def get_name(self):
        return self.__name
    # This method returns the value of the _ _animal_type field.
    def get_animaltype(self):
        return self.__animal_type
    # This method returns the value of the _ _age field. 
    def get_age(self):
        return self.__age
    # This method assigns a value to the _ _name field.
    def set_name(self):
        self.__name = ""
    # This method assigns a value to the _ _animal_type field.
    def set_animaltype(self):
        self.__animal_type = ""
    # This method assigns a value to the _ _age field.
    def set_age(self):
        self.__age = 0