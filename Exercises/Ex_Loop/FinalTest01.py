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
            print("============================================")
            print("                FINAL TEST 01               ")
            print("============================================")
        case 2:
            print("============================================")
            print("              NUMBER ANALYZER               ")
            print("============================================")
        case 3:
            print("============================================")
            print("                CALCULATOR                  ")
            print("============================================")

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

    print(f"{Fore.MAGENTA} > {Fore.RESET}The number, {Fore.BLUE}{number}{Fore.RESET}, is {Fore.YELLOW}{result}{Fore.RESET}")

# Check the divisors in a number
def check_divisors_number(number):
    arr_list = []

    for i in range(1, number + 1):
        if number % i == 0:
            arr_list.append(i)

    print(f"{Fore.MAGENTA} > {Fore.WHITE}Your number have {Fore.BLUE}{len(arr_list)}{Fore.WHITE} divisors")
    print(f"{Fore.MAGENTA} > {Fore.WHITE}The list of divisors: {Fore.BLUE}{arr_list}{Fore.WHITE}")

# Check if the number is perfect
def check_perfect_number(number):
    total = 0
    for i in range(1, number - 1):
        if number % i == 0:
            total += i
    
    if number == total:
        return print(f"{Fore.MAGENTA} > {Fore.RESET}Your number, {Fore.BLUE}{number}{Fore.RESET}, {Fore.YELLOW}is perfect number{Fore.RESET}")
    
    return print(f"{Fore.MAGENTA} > {Fore.RESET}Your number, {Fore.BLUE}{number}{Fore.RESET}, {Fore.YELLOW}isn't perfect number{Fore.RESET}")

# Perform arithmetic operations
def calculate_multiplication_tables(number):
    count = 0
    print()
    print(f"{Fore.MAGENTA} > {Fore.WHITE}MULTIPLICATION TABLE {number}")
    for i in range(1, number + 1):
        count += 1
        print(f"{Fore.MAGENTA} > {Fore.WHITE}{number} x {i} = {number * i}")

        if count == 20:
            print(f"\n{Fore.MAGENTA} > {Fore.WHITE}Do you want continue [YES or NO]")

            respond = input(f"{Fore.BLUE} >  {Fore.WHITE} ").lower()
            if respond == "yes" or respond == "y":
                count = 0
            elif respond == "no" or respond == "n":
                print(f"{Fore.MAGENTA} > {Fore.WHITE} LEAVING THE PROGRAM ")
                break
            else:
                print(f"{Fore.MAGENTA} > {Fore.RED} ! YES OR NO ! {Fore.WHITE}")

# Perform arithmetic operations
def perform_operations(number, symbol):
    for i in range(1, number):
        match symbol:
            case '+':
                print(f"{Fore.MAGENTA} > {Fore.BLUE}{number} + {i} = {number + i} {Fore.WHITE}")
            case '-':
                print(f"{Fore.MAGENTA} > {Fore.BLUE}{number} - {i} = {number - i} {Fore.WHITE}")
            case '*':
                print(f"{Fore.MAGENTA} > {Fore.BLUE}{number} * {i} = {number * i} {Fore.WHITE}")
            case '/':
                print(f"{Fore.MAGENTA} > {Fore.BLUE}{number} / {i} = {number / i} {Fore.WHITE}")

def number_analyzer(number):
    count = 0
    clear_console()
    while number >= 1 and count < 10:
        print(f"{Fore.MAGENTA} > {Fore.BLUE}{number}{Fore.RESET}")
        check_prime_number(number)
        check_divisors_number(number)
        check_perfect_number(number)
        print()
        count += 1
        number -= 1

        if count == 10 and number > 1:
            print(f"\n{Fore.MAGENTA} > {Fore.WHITE}Do you want continue [YES or NO]")

            respond = input(f"{Fore.BLUE} >  {Fore.WHITE} ").lower()
            if respond == "yes" or respond == "y":
                clear_console()
                count = 0
            elif respond == "no" or respond == "n":
                print(f"{Fore.MAGENTA} > {Fore.WHITE} LEAVING THE PROGRAM ")
                break
            else:
                print(f"{Fore.MAGENTA} > {Fore.RED} ! YES OR NO ! {Fore.WHITE}")  

def menu_number_analyzer():
    number = 0
    can_continue = True

    while(can_continue):

        clear_console()
        print_header(2)

        print(f"\n{Fore.MAGENTA} > {Fore.RESET}Enter a number between 1 to 30.000\n")

        try:
            number = int(input(f"{Fore.BLUE}  > {Fore.WHITE} "))

            if 0 < number <= 30000:
                number_analyzer(number)
                print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.WHITE}")
                readchar.readkey()
                can_continue = False
            else:
                print(f"\n{Fore.MAGENTA} > {Fore.RED}! BETWEEN 1 TO 30.000 ! {Fore.WHITE}")
                print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.WHITE}")
                readchar.readkey()

        except ValueError:
            print(f"\n{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.WHITE}")
            print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.WHITE}")
            readchar.readkey()

def calculator_simple(number):
    print(f"{Fore.MAGENTA} > {Fore.RESET} Select Select the operation")
    print(f"{Fore.BLUE}  | {Fore.RESET}+ Sum")
    print(f"{Fore.BLUE}  | {Fore.RESET}- Subtract")
    print(f"{Fore.BLUE}  | {Fore.RESET}x Multiplication")
    print(f"{Fore.BLUE}  | {Fore.RESET}/ Division")

    print(f"\n{Fore.MAGENTA} > {Fore.RESET}Select an option:\n")
    choice = input(f"{Fore.BLUE}  > {Fore.WHITE} ")

    try:
        number2 = float(input(f"{Fore.MAGENTA} > {Fore.RESET}Enter the second number [1 TO 1000]: {Fore.WHITE}"))
    except ValueError:
        return print(f"{Fore.RED}Invalid input! Please enter a number.")
    
    match choice:
        case '+':
            result = number + number2
            op_symbol = "+"
        case '-':
            result = number - number2
            op_symbol = "-"
        case 'x' | '*':
            result = number * number2
            op_symbol = "x"
        case '/':
            if number2 == 0:
                return print(f"{Fore.RED}Error: Division by zero is not allowed.")
            result = number / number2
            op_symbol = "/"
        case _:
            return print(f"{Fore.RED}Invalid option!")

    print(f"\n{Fore.MAGENTA} > {Fore.WHITE}Result: {Fore.BLUE}{number} {op_symbol} {number2} = {Fore.YELLOW}{result}")
    print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.WHITE}")
    readchar.readkey()

def calculator(number , choice):
    match choice:
        case 1:
            clear_console()
            calculator_simple(number)
        case 2:
            clear_console()
            calculate_multiplication_tables(number)
        case _:
            print(f"\n{Fore.MAGENTA} > {Fore.RED} ! INVALID NUMBER ! {Fore.WHITE}")
            print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.WHITE}")
            readchar.readkey()
    
def menu_calculator():
    number = 0
    choice = 0
    count = 0
    can_continue = True

    while(can_continue):

        clear_console()
        print_header(3)

        if count > 0:
            print(f"\n{Fore.MAGENTA} > {Fore.WHITE}Do you want continue [YES or NO]")

            respond = input(f"{Fore.BLUE} >  {Fore.WHITE} ").lower()
            if respond == "yes" or respond == "y":
                clear_console()
                count = 0
            elif respond == "no" or respond == "n":
                print(f"{Fore.MAGENTA} > {Fore.WHITE} LEAVING THE PROGRAM ")
                break
            else:
                print(f"{Fore.MAGENTA} > {Fore.RED} ! YES OR NO ! {Fore.WHITE}")

        print(f"\n{Fore.MAGENTA} > {Fore.RESET}Enter a number between 1 to 1.000\n")

        try:
            number = int(input(f"{Fore.BLUE}  > {Fore.WHITE} "))

            if 0 < number <= 1000:
                print(f"\n{Fore.MAGENTA} > {Fore.RESET}=========== OPTIONS ===========\n")
                print(f"{Fore.BLUE}  | {Fore.RESET} 1 - Normal Calculator")
                print(f"{Fore.BLUE}  | {Fore.RESET} 2 - Multiplication tables")

                try:
                    choice = int(input(f"\n{Fore.BLUE}  > {Fore.WHITE} "))
                    calculator(number, choice)
                    count += 1

                except ValueError:
                    print(f"\n{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.WHITE}")
                    print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.WHITE}")
                    readchar.readkey()

            else:
                print(f"\n{Fore.MAGENTA} > {Fore.RED}! BETWEEN 1 TO 1.000 ! {Fore.WHITE}")
                print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.WHITE}")
                readchar.readkey()

        except ValueError:
            print(f"\n{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.WHITE}")
            print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.WHITE}")
            readchar.readkey()

# Main Function
def main():
    choice = 0
    can_continue = True

    while(can_continue):

        clear_console()
        print_header(1)

        print(f"\n{Fore.MAGENTA} > {Fore.RESET}=========== OPTIONS ===========\n")
        print(f"{Fore.BLUE}  | {Fore.RESET} 1 - Number Analyzer")
        print(f"{Fore.BLUE}  | {Fore.RESET} 2 - Calculator")
        print(f"{Fore.BLUE}  | {Fore.RESET} 3 - Leave the program")

        print(f"\n{Fore.MAGENTA} > {Fore.RESET}Select an option:\n")

        try:
            choice = int(input(f"{Fore.BLUE}  > {Fore.WHITE} "))

            match choice:
                case 1:
                    menu_number_analyzer()
                case 2:
                    menu_calculator()
                case 3:
                    print("Leave the program")
                    can_continue = False
                case _: 
                    print(f"\n{Fore.MAGENTA} > {Fore.RED} ! INVALID NUMBER ! {Fore.WHITE}")
                    print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.WHITE}")
                    readchar.readkey()

        except ValueError:
            print(f"\n{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.WHITE}")
            print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.WHITE}")
            readchar.readkey()

# Start the program
if __name__ == "__main__":
    main()