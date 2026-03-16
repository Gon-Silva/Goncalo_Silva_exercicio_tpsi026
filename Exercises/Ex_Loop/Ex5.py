import os
import platform

# This function clean the console
# For this, I need to import modules like « os » and « platform »

    # os permit to interact with operating system
    # platform permit the program to understand what type of operating system the user is using

import readchar # Import the readchar library, this library only read a single char and keystrokes
from colorama import Fore, Back, Style # Import the colorama library

    # To use the readchar and colorama, it will be necessary use this command in command line

    # Before for you install this library I recommend upgrade python and install pip

    # Windows -> python -m pip install –upgrade python
    # Linux & MacOS -> pip install –upgrade python

    # readchar -> pip3 install readchar
    # colorama -> pip3 install reacolorama

import math

# Function to clean the console
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Function to print a header
def print_header(choice):
    match choice:
        case 1:
            print("========================================")
            print("     WRITE THE FIRST 10.000 NUMBERS     ")
            print("========================================")

# Check if the number is prime or compound
def check_prime_number(number):
    if number <= 1:
        color = Fore.WHITE
    elif number == 2 or number == 3:
        color = Fore.RED
    elif number % 2 == 0:
        color = Fore.WHITE
    else:
        for i in range(3, math.isqrt(number) + 1, 2):
            if number % i == 0:
                color = Fore.WHITE
                break
        else:
                color = Fore.RED

    return print(f"{color}{number} {Fore.WHITE}", end="")

# Main Function
def main():
    clear_console()
    print_header(1)

    for i in range(1, 10000):
        check_prime_number(i)
        if i % 10 == 0:
            print()

# Start the program
if __name__ == "__main__":
    main()