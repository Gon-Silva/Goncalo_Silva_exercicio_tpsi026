import readchar
from colorama import Fore, Style

def cls():
    # Clears the terminal screen using ANSI escape codes
    print("\033[H\033[2J", end="")
    print("\033[H\033[3J", end="")
    print("\033c", end="")


def break_point():
    print(
        f"\n{Fore.MAGENTA} > {Fore.CYAN}{Style.BRIGHT}Press any key to continue...{Style.RESET_ALL}{Fore.RESET}"
    )
    readchar.readkey()


def style_1(message):
    print(
        f"{Fore.MAGENTA} > {Fore.CYAN}{Style.BRIGHT}{message}{Style.RESET_ALL}{Fore.RESET}"
    )


def style_p(message):
    print(
        f"{Fore.MAGENTA} > {Fore.GREEN}{Style.BRIGHT}{message}{Style.RESET_ALL}{Fore.RESET}"
    )


def show_state(lst: list, title: str, location: int):
    print()
    style_1(title)
    style_p(lst)
    style_p(f"list {Fore.YELLOW}[{location}]{Fore.RESET} -> {lst[location]}")
    style_p(f"list {Fore.YELLOW}[{location + 1}]{Fore.RESET} -> {lst[location + 1]}")
    print()

def swapped_list(lst: list, position: int):
    cls()
    show_state(lst, "Before: ", position)
    lst[position], lst[position + 1] = lst[position + 1], lst[position]
    show_state(lst, "After: ", position)
    break_point()


def count_lowercase(string: str):
    count = 0
    for char in string:
        if char.islower():
            count += 1
    return count


def bubble_sort(lst: list):
    size_lst = len(lst)

    for i in range(size_lst):
        for j in range(size_lst - i - 1):
            if count_lowercase(lst[j]) > count_lowercase(lst[j + 1]):
                swapped_list(lst, j)

def main():
    cls()

    random_list = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]


    bubble_sort(random_list)

    cls()

    print()
    style_p("End")
    style_p(random_list)


if __name__ == "__main__":
    main()