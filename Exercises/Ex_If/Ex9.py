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
            print("              CHECK MONTHS              ")
            print("========================================")

# Main Function
def main():
    clear_console()
    print_header(1)

    can_continue = True

    while can_continue:
        print(f"\n{Fore.MAGENTA} > {Fore.WHITE}Insert a number")
            
        try: # If a user accidentally types a letter instead of a number, your program won't crash
            month = float(input(f"{Fore.BLUE} > {Fore.WHITE} "))
                
            print(f"{Fore.MAGENTA} > {Fore.WHITE}Month {Fore.WHITE}", end="")

            if(1 <= month <= 12): can_continue = False

            match month:
                case 1:
                    print("January")
                case 2:
                    print("February")
                case 3:
                    print("March")
                case 4:
                    print("April")
                case 5:
                    print("May")
                case 6:
                    print("June")
                case 7:
                    print("July")
                case 8:
                    print("August")
                case 9:
                    print("September")
                case 10:
                    print("October")
                case 11:
                    print("November")
                case 12:
                    print("December")
                case _:
                    print(f"{Fore.MAGENTA} > {Fore.RED}! INVALID INPUT (1-12 only) ! {Fore.WHITE}")
                    
        except ValueError:
                print(f"{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.WHITE}")

    print(" ")

# Start the program
if __name__ == "__main__":
    main()