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
            print("           CHECK PRIME NUMBER           ")
            print("========================================")

# Check if the number is prime or compound
def check_prime_number(number):
    if number <= 1:
        result = "compound"
    elif number == 2 or number == 3:
        result = "prime"
    elif number % 2 == 0:
        result = "compound"
    else:
        result = "prime"
        for i in range(3, math.isqrt(number) + 1, 2):
            if number % i == 0:
                result = "compound"
                break

    return print(f"{Fore.MAGENTA} > {Fore.WHITE}The number, {Fore.BLUE}{number}{Fore.WHITE}, is {result}")

# Main Function
def main():
    clear_console()
    print_header(1)

    i = 0
    grade_total = 0

    arr_numbers = []

    can_continue = True

    while can_continue:
        print(f"{Fore.MAGENTA} > {Fore.WHITE}Enter as many numbers as you want to check")

        try:
            number_of_check = int(input(f"{Fore.BLUE} >  {Fore.WHITE} "))

            if 1 <= number_of_check:
                can_continue = False
            else:
                print(f"{Fore.MAGENTA} > {Fore.RED}! HIGHER THAN 0 ! {Fore.WHITE}")

        except ValueError:
            print(f"{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.WHITE}")

    print()

    while i < number_of_check:
        print(f"{Fore.MAGENTA} > {Fore.WHITE}Enter the {i + 1}º number")

        try:
            number = int(input(f"{Fore.BLUE} >  {Fore.WHITE} "))
            arr_numbers.append(number)
            i = i + 1
        except ValueError:
            print(f"{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.WHITE}")

    print()

    for number in range(len(arr_numbers)):
       check_prime_number(arr_numbers[number])

# Start the program
if __name__ == "__main__":
    main()