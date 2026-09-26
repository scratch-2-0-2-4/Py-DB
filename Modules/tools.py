import os
import time

loading_list = ["|", "/", "-", "\\"]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading(x) :
    for i in range(x):
        for x in loading_list:
            clear()
            print(f"Chargement... {x}")
            time.sleep(0.1)
    
    clear()