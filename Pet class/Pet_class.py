# Setup Pet class
class Pet():
    # Pet's attributes
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
# Methods
    # This method assigns a value to the _ _name field.
    def set_name(self, name):
        self.__name = name
    # This method assigns a value to the _ _animal_type field.
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    # This method assigns a value to the _ _age field.
    def set_age(self, age):
        self.__age = age
        # This method returns the value of the _ _ name field.
    def get_name(self):
        return self.__name
    # This method returns the value of the _ _animal_type field.
    def get_animal_type(self):
        return self.__animal_type
    # This method returns the value of the _ _age field. 
    def get_age(self):
        return self.__age