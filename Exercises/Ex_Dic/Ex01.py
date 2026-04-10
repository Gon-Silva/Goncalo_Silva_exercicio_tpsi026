import subprocess
import os
import readchar
from colorama import Fore, Back, Style

# To use the readchar and colorama, it will be necessary use this command in command line

    # Before for you install this library I recommend upgrade python and install pip

    # Windows -> python -m pip install –upgrade python
    # Linux & MacOS -> pip install –upgrade python

    # readchar -> pip3 install readchar
    # colorama -> pip3 install reacolorama

# Function to clean the console
def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

def break_point():
    print(f"{Fore.MAGENTA} > {Fore.CYAN}{Style.BRIGHT}Press any key to continue...{Style.RESET_ALL}{Fore.RESET}")
    readchar.readkey()

def print_message(message:str):
    print(f"{Fore.MAGENTA} > {Fore.GREEN}{Style.BRIGHT}{message}{Style.RESET_ALL}{Fore.RESET}")

def print_current_student(current :int):
    print(f"{Fore.MAGENTA} > {Fore.GREEN}{Style.BRIGHT}{f"Student"}{Fore.BLUE}[{Fore.YELLOW}{current}{Fore.BLUE}]{Style.RESET_ALL}{Fore.RESET}")

def print_information(message :str, information :str):
    print(f"{Fore.BLUE}  | {Fore.GREEN}{Style.BRIGHT}{message}{Fore.YELLOW}{information}{Style.RESET_ALL}{Fore.RESET}")

def print_student(dict_students :dict, current :int):

    first_name = f"{dict_students[current]['first name']}"
    last_name = f"{dict_students[current]['last name']}"
    age = f"{dict_students[current]['age']}"
    course = f"{dict_students[current]['course']}"

    print_current_student(current)
    print_information("First Name: ", first_name)
    print_information("Last Name: ", last_name)
    print_information("Age: ", age)
    print_information("Course: ", course)

    print("")

def print_option(number:int, message:str):
    print(f"{Fore.BLUE}  | {Fore.BLUE}[{Fore.YELLOW}{number}{Fore.BLUE}] {Fore.CYAN}{Style.BRIGHT}{message}{Style.RESET_ALL}{Fore.RESET}")

def input_message(message:str):
    return input(f"{Fore.MAGENTA} > {Fore.GREEN}{Style.BRIGHT}{message}{Style.RESET_ALL}{Fore.MAGENTA} > {Fore.RESET}")

def notify_invalid_selection(message:str):
    print(f"\n{Fore.MAGENTA} > {Fore.RED}{Style.BRIGHT}{message}{Style.RESET_ALL}{Fore.RESET}")
    break_point()

def check_input(message:str):
        try:
            user_input = int(input_message(message))
            return user_input, True

        except ValueError:
            notify_invalid_selection("! MUST BE A NUMBER !")
            return 0, False

def insert_dict(dict_students :dict):
    clear_console()
    value = len(dict_students)
    while True:
        first_name = input_message("Insert the first name")

        last_name = input_message("Insert the last name")

        age, is_valid = check_input("Insert the age")

        if not is_valid:
            continue

        course = input_message("Insert the course")

        break

    
    dict_students.update({
        value + 1: {
                "first name": first_name,
                "last name": last_name,
                "age": age,
                "course": course
            }
        })

    print("")
    print_message("Add successfully")
    print("")
    break_point()

def list_dictionary(dict_students :dict):
    clear_console()
    for student in dict_students.keys():

        print_student(dict_students, student)

    break_point()

def main():

    # test dictionary
    Students = {
        1: {"first name": "João", "last name": "Silva", "age": 18, "course": "CET"},
        2: {"first name": "Ana",  "last name": "Costa", "age": 20, "course": "CET"},
    }

    while True:

        clear_console()

        print_message("MENU =================")
        print_option(1, "Insert")
        print_option(2, "List")
        print_option(3, "Leave")

        print("")

        choice, is_valid = check_input("Select a option")

        if not is_valid:
            continue

        match choice:
            case 1:
                insert_dict(Students)
                pass
            case 2:
                list_dictionary(Students)
                pass
            case 3:
                print("")
                print_message("Thank you for using the program")
                print("")
                break
            case _:
                print("")
                notify_invalid_selection("Select a valid option")

if __name__ == "__main__":
    main()