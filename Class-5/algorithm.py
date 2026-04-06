import os
import platform
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
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def break_point():
    print(f"\n{Fore.MAGENTA} > {Fore.CYAN}{Style.BRIGHT} Press any key to continue...{Style.RESET_ALL}{Fore.RESET}")
    readchar.readkey()

# Check the array if is empty
def is_empty(array):
    if len(array) == 0:
        print(f"{Fore.MAGENTA} > {Fore.RESET}Add data ")
        break_point()
        return True
    
    return False

def insert_names_menu(arr_names):
    clear_console()

    print(f"{Fore.MAGENTA} > {Fore.RESET}Enter a name")

    name = input(f"\n{Fore.MAGENTA} > {Fore.RESET}")

    arr_names.append(name)

def list_array_menu(arr_names):
    clear_console()

    for i in range(len(arr_names)):
        print(f"{Fore.MAGENTA} > {Fore.RESET}Name {i + 1} - {arr_names[i]}")

    break_point()

def delete_element_array_menu(arr_names, arr_index):
    while True:
        clear_console()

        if is_empty(arr_names):
            break

        print(f"{Fore.MAGENTA} > {Fore.CYAN} MENU ==================")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 1 - Find the name and delete")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 2 - Delete by position")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 3 - Back to menu")

        try:
            choice = int(input(f"\n{Fore.MAGENTA} > {Fore.RESET}"))

            match choice:
                case 1:
                    delete_find(arr_names, arr_index)
                    break
                case 2:
                    delete(arr_names)
                    pass
                case 3:
                    print(f"{Fore.MAGENTA} > {Fore.RESET}Back to menu")
                    break
                case _:
                    print(f"{Fore.MAGENTA} > {Fore.RESET}Select a validate option")
                    break_point()

        except ValueError:
                print(f"{Fore.MAGENTA} > {Fore.RESET}It must be a number")
                break_point()

    break_point()

def delete_find(arr_names, arr_index):
    while True:
        find_name_menu(arr_names, arr_index)

        print(f"\n{Fore.MAGENTA} > {Fore.RESET}Which one do you want to delete?")

        try:
            position = int(input(f"{Fore.MAGENTA} > {Fore.RESET}"))
            position -= 1

            size = len(arr_index)

            if position >= 0 and position < size:
                print(f"{Fore.MAGENTA} > {Fore.RESET}Delete name {arr_index[position] + 1}: \"{arr_names[arr_index[position]]}\" [Position: {arr_index[position]}]")
                arr_names.pop(arr_index[position])
                break

            else:
                print(f"{Fore.MAGENTA} > {Fore.RESET}Need to between 1 and {size}")
                break_point()

        except ValueError:
            print(f"{Fore.MAGENTA} > {Fore.RESET}It must be a number")
            break_point()

def delete(arr_names):
    while True:
        print(f"{Fore.MAGENTA} > {Fore.RESET}Enter a number to delete")

        size = len(arr_names)

        try:
            position = int(input(f"{Fore.MAGENTA} > {Fore.RESET}"))

            if position >= 0 and position < size:
                print(f"{Fore.MAGENTA} > {Fore.RESET}Delete name {arr_names[position]}")
                arr_names.pop(position)
                break

            else:
                print(f"{Fore.MAGENTA} > {Fore.RESET}Need to between 0 and {size - 1}")
                break_point()

        except ValueError:
            print(f"{Fore.MAGENTA} > {Fore.RESET}It must be a number")
            break_point()

def find_name_menu(arr_names, arr_index):
    while True:
        clear_console()
        print("Enter a name")

        size = len(arr_names)

        if size == 0:
            print(f"{Fore.MAGENTA} > {Fore.RESET}Add data ")
            readchar.readkey()
            break

        name = input(f"{Fore.MAGENTA} > {Fore.RESET}")

        if find_name(arr_names, arr_index, name):
            for i in range(len(arr_index)):
                print(f"{Fore.MAGENTA} > {Fore.RESET}Name {i + 1}: \"{arr_names[arr_index[i]]}\" [Position: {arr_index[i]}]")
        else:
            print(f"{Fore.MAGENTA} > {Fore.RESET}Sorry but name you're looking for doesn't exit")

        break_point()
        break

def find_name(array, index, name):
    index.clear()
    for i in range(len(array)):
        if array[i] == name:
            index.append(i)

    if len(index) == 0:
        return False
    else:
        return True

def main():

    arr_names = ["da", "fa", "oi", "da"]
    arr_index = []

    while True:

        clear_console()

        print(f"{Fore.MAGENTA} > {Fore.CYAN} MENU ==================")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 1 - Insert names")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 2 - Lists the names")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 3 - Delete names")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 4 - Find the name")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 5 - Leave the program {Fore.RESET}")

        try:
            choice = int(input(f"\n{Fore.MAGENTA} > {Fore.RESET}"))

            match choice:
                case 1:
                    insert_names_menu(arr_names)
                    pass
                case 2:
                    list_array_menu(arr_names)
                    pass
                case 3:
                    delete_element_array_menu(arr_names, arr_index)
                    pass
                case 4:
                    find_name_menu(arr_names, arr_index)
                    pass
                case 5:
                    print(f"{Fore.MAGENTA} > {Fore.RESET}Thank you for using the program")
                    break
                case _:
                    print(f"{Fore.MAGENTA} > {Fore.RESET}Select a validate option")
                    break_point()

        except ValueError:
            print("It must be a number")
            break_point()

if __name__ == "__main__":
    main()