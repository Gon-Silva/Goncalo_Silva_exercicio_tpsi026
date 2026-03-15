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
            print("                SHOP                    ")
            print("========================================")

def check_discount(purchase):
    if purchase <= 200:
        return 0.1;
    elif purchase > 200 and purchase <= 500:
        return 0.15;
    elif purchase > 500:
        return 0.2

# Main Function
def main():

    start_program = True

    balance = 0.00

    while(start_program):
        clear_console()
        print_header(1)

        print(f"\n{Fore.MAGENTA} > {Fore.WHITE} Insert your name")
        name = input(f"\n  {Fore.BLUE} > {Fore.WHITE} ")

        print(f"\n{Fore.MAGENTA} > {Fore.WHITE} Insert your purchase")
        purchase = int(input(f"\n {Fore.BLUE} > {Fore.WHITE} "))

        if (purchase < 0):
            print(f" {Fore.MAGENTA} > {Fore.RED} ! INVALID INPUT ! {Fore.WHITE}")
            print(f" {Fore.MAGENTA} > {Fore.RED}Press any key to continue...{Fore.WHITE} ")
            readchar.readkey()  # This waits for a single keypress
        else:
            discount = check_discount(purchase)

            print(f"\n{Fore.MAGENTA} > {Fore.WHITE} Name of the client: {name}")
            print(f"{Fore.MAGENTA} > {Fore.WHITE} Purchase: {purchase:.2f}€")
            print(f"{Fore.MAGENTA} > {Fore.WHITE} Discount: {(purchase * discount):.2f}€")
            print(f"{Fore.MAGENTA} > {Fore.WHITE} Total payable: {(purchase - (purchase * discount)):.2f}€")

            start_program = False
            print("")

# Start the program
if __name__ == "__main__":
    main()