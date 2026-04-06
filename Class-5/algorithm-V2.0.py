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
    print(f"\n{Fore.MAGENTA} > {Fore.CYAN}{Style.BRIGHT}Press any key to continue...{Style.RESET_ALL}{Fore.RESET}")
    readchar.readkey()

def print_message(message):
    print(f"\n{Fore.MAGENTA} > {Fore.GREEN}{Style.BRIGHT}{message}{Style.RESET_ALL}{Fore.RESET}")

def input_message(message:str):
    return input(f"\n{Fore.MAGENTA} > {Fore.GREEN}{Style.BRIGHT}{message}{Style.RESET_ALL}{Fore.MAGENTA} > {Fore.RESET}")

def check_input(message:str):
        try:
            user_input = int(input_message(message))
            return user_input, True

        except ValueError:
            print(f"\n{Fore.MAGENTA} > {Fore.RED}{Style.BRIGHT}! MUST BE A NUMBER !{Style.RESET_ALL}{Fore.RESET}")
            break_point()
            return 0, False

def check_range(max:int, min:int, input_user:int):
    if min <= input_user <= max:
        return False
    else:
        print(f"\n{Fore.MAGENTA} > {Fore.RED}{Style.BRIGHT}! BETWEEN {Fore.YELLOW}{min}{Fore.RED} AND {Fore.YELLOW}{max}{Fore.RED} !{Style.RESET_ALL}{Fore.RESET}")
        break_point()
        return True

def notify_invalid_selection(message:str):
    print(f"\n{Fore.MAGENTA} > {Fore.RED}{Style.BRIGHT}{message}{Style.RESET_ALL}{Fore.RESET}")
    break_point()

# Check the array if is empty
def is_empty(array:list):
    if len(array) == 0:
        print(f"{Fore.MAGENTA} > {Fore.RESET}Add data ")
        break_point()
        return True
    
    return False

def insert_menu(list_names:list):
    can_continue = True

    while can_continue:
        clear_console()

        numbers, can_continue = check_input("How many name do you want to add? [1-1000]")

        if can_continue:
            can_continue = check_range(1000, 1, numbers)
        else:
            can_continue = True

    for i in range(numbers):
        insert("Enter a name", list_names)

def insert(message:str, list_names:list):
    name = input_message(message)
    list_names.append(name)

def list_name(list_names:list):
    clear_console()

    for i in range(len(list_names)):
        print_message(f"Name {i + 1} - {list_names[i]}")

    break_point()

def delete_menu(list_names:list, list_index:list):
    can_continue = True
    while can_continue:
        clear_console()

        if is_empty(list_names):
            break

        print(f"{Fore.MAGENTA} > {Fore.CYAN} MENU ==================")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 1 - Find the name and delete")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 2 - Delete by position")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 3 - Back to menu")

        choice, can_continue = check_input("Select a option")

        if can_continue:
            match choice:
                case 1:
                    find_and_delete(list_names, list_index)
                    pass
                case 2:
                    position_delete(list_names)
                    pass
                case 3: break
                case _:
                    notify_invalid_selection("! SELECT A VALIDATE OPTION !")
        else:
            can_continue = True

def position_delete(list_names:list):
    can_continue = True
    size = len(list_names)

    while can_continue:
        clear_console()
        position, can_continue = check_input(f"Enter a position [1-{size}]")

        if can_continue:
            can_delete = not check_range(size, 1, position)
            position -= 1

            if can_delete:
                print_message(f"Delete - {Fore.YELLOW}{delete(list_names, position)}{Fore.GREEN} [Position: {position}]")
                can_continue = False

            break_point()

def find_and_delete(list_names:list, list_index:list):
    find_name_menu(list_names, list_index, False)

    if not list_index:
        return

    position, can_continue = check_input("Which one do you want to delete?")

    if can_continue:
        can_delete = not check_range(len(list_index), 1, position)
        position -= 1

        if can_delete:
            print_message(f"Delete - {Fore.YELLOW}{delete(list_names, position)}{Fore.GREEN} [Position: {list_index[position]}]")
        
        break_point()

def delete(list_names:list, position:int):
    return list_names.pop(position)

def find_name_menu(list_names:list, list_index:list, show_break_point):
    while True:
        clear_console()

        if is_empty(list_names):
            break

        name = input_message("Enter name")

        if find(list_names, list_index, name):
            for i in range(len(list_index)):
                original_pos = list_index[i]
                found_name = list_names[original_pos]

                print_message(f"Name - {Fore.YELLOW}{found_name}{Fore.GREEN} [Position: {original_pos}]")

            if show_break_point: break_point()
            return list_index
        else:
            notify_invalid_selection("Sorry, name not found")
            return []

def find(array:list, index:list, name:str):
    index.clear()
    for i in range(len(array)):
        if array[i] == name:
            index.append(i)

    if len(index) == 0:
        return False
    else:
        return True

def main():

    list_names = ["da", "fa", "oi", "da"]
    list_index = []
    can_continue = True

    while can_continue:

        clear_console()

        print(f"{Fore.MAGENTA} > {Fore.CYAN} MENU ==================")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 1 - Insert names")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 2 - Lists the names")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 3 - Delete names")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 4 - Find the name")
        print(f"{Fore.MAGENTA}  |{Fore.CYAN} 5 - Leave the program {Fore.RESET}")

        choice, can_continue = check_input("Select a option")

        if can_continue:
            match choice:
                case 1:
                    insert_menu(list_names)
                    pass
                case 2:
                    list_name(list_names)
                    pass
                case 3:
                    delete_menu(list_names, list_index)
                    pass
                case 4:
                    find_name_menu(list_names, list_index, True)
                    pass
                case 5:
                    print(f"\n{Fore.MAGENTA} > {Fore.GREEN}{Style.BRIGHT}Thank you for using the program{Style.RESET_ALL}{Fore.RESET}\n")
                    break
                case _:
                    notify_invalid_selection("! SELECT A VALIDATE OPTION !")
        else:
            can_continue = True

if __name__ == "__main__":
    main()