import readchar
from colorama import Fore, Back, Style

'''
Não foi possível concluir o ponto 3 dado que o ponto 5 impede a descriptografia dos acentos ou outros simbolos fora do intervalo 32 a 126
'''

def cls():
    # Clears the terminal screen using ANSI escape codes
    print("\033[H\033[2J", end="")
    print("\033[H\033[3J", end="")
    print("\033c", end="")

def break_point():
    print(f"\n{Fore.MAGENTA} > {Fore.CYAN}{Style.BRIGHT}Press any key to continue...{Style.RESET_ALL}{Fore.RESET}")
    readchar.readkey()

def print_message(message):
    print(f"{Fore.MAGENTA} > {Fore.GREEN}{Style.BRIGHT}{message}{Style.RESET_ALL}{Fore.RESET}")

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

def check_key(message :str):
    key = input_message(message)

    if key == "":
        notify_invalid_selection("Enter a vaild key")
        return "", False
    
    return key, True

def key_to_decimal(key :str):
    total_sum = 0
    for i in key:
        total_sum += ord(i)

    return total_sum

def encryption_menu(list_message :list):

    while True:
        cls()

        message = input_message("Enter your message to be encryption")
        key, is_valid = check_key("Enter your key")

        if not is_valid:
            continue

        encryption(message, key, list_message)

        print()
        print_message(f"Encryption message -> {list_message}")
        print()

        print_message("ENCRYPTION SUCCESS")
        break_point()
        return

def encryption(message :str, key :str, list_message :list):
    total_sum = 0

    total_sum = key_to_decimal(key)

    for i in message:
        list_message.append((ord(i) + total_sum - 32) % 95 +32)

def decryption_menu(list_message :list):

    while True:
        cls()

        key, is_valid = check_key("Enter your key")

        if not is_valid:
            continue

        print()

        print_message(f"decryption message -> {decryption(list_message, key)}")

        break_point()
        return

def decryption(list_message :list, key :str):

    total_sum = key_to_decimal(key)
    message = ""
    
    for i in range(len(list_message)):
        message += (chr((list_message[i] - total_sum - 32) % 95 +32))

    return message

def main():

    list_message = []

    while True:

        cls()

        print_message("MENU ==================")
        print_option(1, "Encryption")
        print_option(2, "Decryption")
        print_option(3, "Leave")

        print()

        choice, is_valid = check_input("Select an option")

        if not is_valid:
            continue

        match choice:
            case 1:
                encryption_menu(list_message)
                pass
            case 2:
                decryption_menu(list_message)
                pass
            case 3:
                print_message("Thank you for using the app")               
                break
            case _:
                notify_invalid_selection("Need to be between 1 to 3")
                pass

if __name__ == "__main__":
    main()