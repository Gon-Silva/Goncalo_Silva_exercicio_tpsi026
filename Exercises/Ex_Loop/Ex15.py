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
            print("          WRITE THE ASCII CODE          ")
            print("========================================")

# Show the ascii code
def show_ASCII_code(number):
    for i in range(number, number+ 20):
        if i > 255: 
            print(f"\n{Fore.MAGENTA} > {Fore.RED} ! ASCII LIMIT ! {Fore.WHITE}") 
            return
        print(f"{Fore.MAGENTA} > {Fore.WHITE} DEC: {Fore.BLUE}{i}{Fore.WHITE}; HEX: {Fore.BLUE}{hex(i)}{Fore.WHITE}; OCT: {Fore.BLUE}{oct(i)}{Fore.WHITE}; Binary: {Fore.BLUE}{bin(i)}{Fore.WHITE}; CHAR: {Fore.BLUE}{chr(i)}{Fore.WHITE};")

# Main Function
def main():
    clear_console()
    print_header(1)

    can_continue = True
    current_number = 0

    show_ASCII_code(current_number)

    while can_continue:
        print(f"\n{Fore.MAGENTA} > {Fore.WHITE}Do you want continue [YES or NO]")

        respond = input(f"{Fore.BLUE} >  {Fore.WHITE} ").lower()

        if respond == "yes" or respond == "y":
            current_number += 20
            show_ASCII_code(current_number)
        elif respond == "no" or respond == "n":
            print(f"{Fore.MAGENTA} > {Fore.WHITE} LEAVING THE PROGRAM ")
            can_continue = False
        else:
            print(f"{Fore.MAGENTA} > {Fore.RED} ! YES OR NO ! {Fore.WHITE}")

    print()

# Start the program
if __name__ == "__main__":
    main()