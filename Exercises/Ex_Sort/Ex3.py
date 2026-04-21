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

def string_to_word(string :str):
    string_list = []
    for i in range(len(string)):
        string_list.append(string[i])

    return string_list


def sorted(lst: list):
    size_of_lst = len(lst)

    for i in range(size_of_lst):
        swapped = False

        for j in range(0, size_of_lst - i - 1):
            word_1 = lst[j]
            word_2 = lst[j + 1]

            if len(word_1) < len(word_2):
                min_size = len(word_1)
            elif len(word_1) > len(word_2):
                min_size = len(word_2)
            else:
                min_size = len(word_1)

            # or
            # min_size = min(len(word_1), len(word_2))

            should_swapped = False
            already_decided = False

            for o in range(min_size):
                if ord(word_1[0]) > ord(word_2[0]):
                    should_swapped = True
                    already_decided = True
                    break
                elif ord(word_1[o]) < ord(word_2[o]):
                    already_decided = True
                    break

            if not already_decided and len(word_1) > len(word_2):
                should_swapped = True

            if should_swapped:
                swapped_list(lst, j)
                swapped = True

        if not swapped:
            break


def main():
    cls()

    palavra = "algoritmo"
    palavra_list = string_to_word(palavra)
    # Expect output -> ["abacaxi", "banana", "laranja", "uva"]

    sorted(palavra_list)

    cls()

    print()
    style_p("End")
    style_p(palavra_list)


if __name__ == "__main__":
    main()
