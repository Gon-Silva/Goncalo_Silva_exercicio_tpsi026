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
            print("============================================")
            print("                PERFECT NUMBERS             ")
            print("============================================")

# Check if the number is perfect
def check_perfect_number(number):
    total = 0
    for i in range(1, number-1):
        if number % i == 0:
            total += i
    
    if number == total:
        return True
    
    return False

# Main Function
def main():
    clear_console()
    print_header(1)

    i = 0

    print(f"{Fore.MAGENTA} > {Fore.WHITE}How many times do you want check")
    many_times = int(input(f"{Fore.BLUE} >  {Fore.WHITE} "))

    while i < many_times:
        print(f"{Fore.MAGENTA} > {Fore.WHITE}Enter your perfect number")

        try:
            perfect_number = int(input(f"{Fore.BLUE} >  {Fore.WHITE} "))

            if(perfect_number > 0):
                i += 1
                check_perfect_number(perfect_number)
                if (check_perfect_number(perfect_number)):
                    print(f"{Fore.MAGENTA} > {Fore.WHITE}Your number, {Fore.BLUE}{perfect_number}{Fore.WHITE}, is perfect number")
                else:
                    print(f"{Fore.MAGENTA} > {Fore.WHITE}Your number, {Fore.BLUE}{perfect_number}{Fore.WHITE}, isn't perfect number")
            else:
                print(f"{Fore.MAGENTA} > {Fore.RED}! GREATER THAN 0 ! {Fore.WHITE}")

        except ValueError:
            print(f"{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.WHITE}")


# Start the program
if __name__ == "__main__":
    main()