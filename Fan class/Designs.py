from pyfiglet import Figlet
from termcolor import colored
from tqdm import tqdm
import time 
class designs():
# brand of the fan
    def __init__(self, brand, welcome, loading):
        self.__brand = brand
        self.__welcome = welcome
        self.__loading = loading
    def get_brand(self):
        fan_bd = Figlet(font = "SMslant", justify = "right")
        print()
        print("⚜ " * 89)
        print(colored(fan_bd.renderText("                                                               A3THER"), "yellow"))
        return self.__brand
# Welcome the user
    def show_welcome(self):
        s_a_c = Figlet(font = "starwars", justify = "right")
        print()
        print(colored(s_a_c.renderText("            W e l c o m e              "), "green"))
        print("\33[35m                                                 (\ (\ \33[0m")
        print("\33[35m                                                 („• ֊ •„) ♡ \33[0m")
        print("\33[35m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━O━O━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \33[0m")
        print("\33[35m                                                                            please wait.... \33[0m ")
        print()
        print("⚜ " * 89)
        print()
        return self.__welcome
# Loading bar
    def loading_bar(self):
        for i in tqdm (range (100), desc="Loading...\U0001F973"):
            time.sleep(0.05)
            pass
        print("\n\n")
        print("\33[32m\33[1m                                                               Thank you for your patience!˶^•ﻌ•^˵ \33[0m\n")
        print("⚜ " * 89)
        print()
        return self.__loading
