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
            print(" WRITE THE FIRST 1.000 NUMBERS 10 by 10 ")
            print("========================================")

# Main Function
def main():
    clear_console()
    print_header(1)

    for i in range(10, 1001, 10):
        print(f"{i} ", end="")
        if i % 100 == 0:
            print()

# Start the program
if __name__ == "__main__":
    main()