import os
import platform

# This function clean the console
# For this, I need to import modulos like « os » and « platform »

    # os permit to interact with operating system
    # plataform permit the program to undertand what type of operating system the user is using

import readchar
from colorama import Fore, Back, Style # Import the colorama Module

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
            print("               ACCOUNT                  ")
            print("========================================")
        case 2:
            print("========================================")
            print("              ADD BALANCE               ")
            print("========================================")
        case 3:
            print("========================================")
            print("             VIEW BALANCE               ")
            print("========================================")

# Fuction to add balance
def add_balance(balance):
    clear_console()
    print_header(2)

    print(f" {Fore.MAGENTA} > {Fore.WHITE} How much do you want add?")
    balance = + float(input(f"\n {Fore.BLUE}  > {Fore.WHITE} "))

    print(f"\n {Fore.MAGENTA} > {Fore.WHITE} Your balance is {Fore.GREEN}{balance}€{Fore.WHITE}")

    print(f" {Fore.MAGENTA} > {Fore.WHITE}Press any key to continue... ")
    readchar.readkey()  # This waits for a single keypress

    return balance

# Function to add check
def add_check(balance):
    clear_console()
    print_header(2)

    print(f" {Fore.MAGENTA} > {Fore.WHITE} What is the value of the check?")
    check = float(input(f"\n {Fore.BLUE}  > {Fore.WHITE} "))

    if(balance >= check):
        balance = balance - check
        print(f"\n {Fore.MAGENTA} > {Fore.WHITE} Check cahsed")
        print(f" {Fore.MAGENTA} > {Fore.WHITE} Your balance is {Fore.GREEN}{balance}€{Fore.WHITE}")
    else:
        print(f" {Fore.MAGENTA} > {Fore.WHITE} Uncashed check")
        print(f" {Fore.MAGENTA} > {Fore.WHITE} Your balance is {Fore.GREEN}{balance}€{Fore.WHITE}")

    print(f" {Fore.MAGENTA} > {Fore.WHITE}Press any key to continue... ")
    readchar.readkey()  # This waits for a single keypress

    return balance

# Function to view balance
def view_balance(balance):
    clear_console()
    print_header(3)

    print(f" {Fore.MAGENTA} > {Fore.WHITE} Your balance is {Fore.GREEN}{balance}€{Fore.WHITE}")

    print(f" {Fore.MAGENTA} > {Fore.WHITE}Press any key to continue... ")
    readchar.readkey()  # This waits for a single keypress

# Main Function
def main():

    start_program = True

    balance = 0.00

    while(start_program):
        clear_console()
        print_header(1)

        print(f" {Fore.MAGENTA} > {Fore.WHITE} 1 - Add balance")
        print(f" {Fore.MAGENTA} > {Fore.WHITE} 2 - Add check")
        print(f" {Fore.MAGENTA} > {Fore.WHITE} 3 - View Balance")
        print(f" {Fore.MAGENTA} > {Fore.WHITE} 4 - Leave")
        choice = int(input(f"\n  {Fore.BLUE} > {Fore.WHITE} "))

        match choice:
            case 1:
                balance = add_balance(balance)
            case 2:
                balance = add_check(balance)
            case 3:
                view_balance(balance)
            case 4:
                print(f"\n{Fore.MAGENTA} > {Fore.WHITE} LEAVING THE PROGRAM")
                start_program = False

            case _:
                print(f" {Fore.MAGENTA} > {Fore.RED} ! INVALID INPUT ! {Fore.WHITE}")
                print(f" {Fore.MAGENTA} > {Fore.RED}Press any key to continue...{Fore.WHITE} ")
                readchar.readkey()  # This waits for a single keypress

# Start the program
if __name__ == "__main__":
    main()