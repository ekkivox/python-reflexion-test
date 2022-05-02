from operator import contains
from colorama import Fore as f
import keyboard
from time import sleep
import random
from os import system

system("cls")


try:
    with open("log.log", "r") as last_time:
        print(f"Your last time was > {last_time.read()} ms")
except:
    print("Your last time was > None")

input(f"{f.LIGHTBLUE_EX}<!> Press enter to start...{f.RESET}")

def start():
    system("cls")
    print(f"{f.LIGHTRED_EX}<!> Press space when you see the text turn green.{f.RESET}")

    sleep(random.randrange(1,10))

    system("cls")
    print(f"{f.LIGHTGREEN_EX}<!> Press space now.{f.RESET}")
    timer = True

    curr = float(0.0)

    while timer:
        curr += float(0.1)

        if keyboard.is_pressed("space"):
            system("cls")
            timer = False
            print(f"<!> Your time was {round(curr, 2)} ms")

            with open("log.log", "w") as last_time:
                last_time.write(str(round(curr, 2)))


start()
input("press enter")