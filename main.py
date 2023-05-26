import time
import os
import random

def clear():
    if os.name == "nt":
        # windows
        os.system("cls")
    else:
        # mac and linux
        os.system("clear")

def buffering(iterations=3):
    clear()

    buffering_string = "."

    for count in range(iterations):
        print(buffering_string)
        buffering_string += "."

        time.sleep(0.1)
        os.system("clear")

buffering()

# should be able to choose themes: countries, snacks, games, etc
print("Welcome to Terminodle! The wordle game inside your terminal.")

print("""

.___________. _______ .______      .___  ___.  __  .__   __.   ______    _______   __       _______ 
|           ||   ____||   _  \     |   \/   | |  | |  \ |  |  /  __  \  |       \ |  |     |   ____|
`---|  |----`|  |__   |  |_)  |    |  \  /  | |  | |   \|  | |  |  |  | |  .--.  ||  |     |  |__   
    |  |     |   __|  |      /     |  |\/|  | |  | |  . `  | |  |  |  | |  |  |  ||  |     |   __|  
    |  |     |  |____ |  |\  \----.|  |  |  | |  | |  |\   | |  `--'  | |  '--'  ||  `----.|  |____ 
    |__|     |_______|| _| `._____||__|  |__| |__| |__| \__|  \______/  |_______/ |_______||_______|

 """)

input("Enter any key to continue: ")

buffering()

mode = input("Select a theme. The only theme that is currently available is 'Food': ").lower()

word_list = []

if mode == "food":
    with open("./word-lists/food.txt") as food_list:
        for word in food_list:
            word_list.append(word)

word = random.choice(word_list).upper()