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
            print("===================================================")
            print("        CALCULATE THE AVERAGE OF EVEN NUMBERS      ")
            print("===================================================")

# Perform arithmetic operations
def calculate_average_even(arr_number):
    print()
    total = 0
    size = len(arr_number)
    for i in range(size - 1):
        total += arr_number[i]

    return total / size

# Main Function
def main():
    clear_console()
    print_header(1)

    arr_number = []
    i = 0;

    while i < 10:
        print(f"{Fore.MAGENTA} > {Fore.WHITE}Enter your {Fore.BLUE}{i+1}º{Fore.WHITE} number [0-50]")

        try:
            number = int(input(f"{Fore.BLUE} >  {Fore.WHITE} "))

            if number % 2 == 0 and 0 < number <= 50:
                arr_number.append(number)
                i += 1
                print(f"{Fore.MAGENTA} > {Fore.GREEN}! SUCCESS ! {Fore.WHITE}")
            else:
                if 0 > number or number > 50: 
                    print(f"{Fore.MAGENTA} > {Fore.RED}! GREATER THAN 0 OR EQUAL TO 50 ! {Fore.WHITE}")
                if number % 2 != 0:
                    print(f"{Fore.MAGENTA} > {Fore.RED}! IT MUST NE EVEN ! {Fore.WHITE}")

        except ValueError:
            print(f"{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.WHITE}")

    print(f"{Fore.MAGENTA} > {Fore.WHITE}The average is {Fore.BLUE}{calculate_average_even(arr_number)}{Fore.WHITE}")
    print()

# Start the program
if __name__ == "__main__":
    main()