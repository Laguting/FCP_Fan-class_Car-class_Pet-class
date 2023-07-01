from pyfiglet import Figlet
from termcolor import colored
from tqdm import tqdm
import time 
class designs():
    def __init__(self, brand, welcome, loading):
        self.__brand = brand
        self.__welcome = welcome
        self.__loading = loading
    def get_brand(self):
        fan_bd = Figlet(font = "digital", justify = "right")
        print()
        print("⚜ " * 89)
        print()
        print(colored(fan_bd.renderText("                                                       A3THER"), "yellow"))
        return self.__brand
# Welcome the user
