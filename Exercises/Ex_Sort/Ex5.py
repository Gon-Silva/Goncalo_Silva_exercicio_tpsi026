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


def show_state(dic: dict, title: str, location: int):
    print()
    style_1(title)
    style_p(dic)
    style_p(f"list {Fore.YELLOW}[{location}]{Fore.RESET} -> {dic[location]}")
    style_p(f"list {Fore.YELLOW}[{location + 1}]{Fore.RESET} -> {dic[location + 1]}")
    print()


def swapped_list(lst: list, position: int):
    cls()
    show_state(lst, "Before: ", position)
    lst[position], lst[position + 1] = lst[position + 1], lst[position]
    show_state(lst, "After: ", position)
    break_point()


def add_to_dict(lst :list):
    dic = {}
    size_lst = len(lst)

    for key in range(size_lst):
        if lst[key][0] in dic:
            dic[lst[key][0]].append(lst[key])
        else:
            dic[lst[key][0]] = []
            dic[lst[key][0]].append(lst[key])

    return dic



def sorted_dict(lst :list, dic :dict):
    size_lst = len(lst)
    dic_sec = {}

    for i in range(size_lst):
        for j in range(size_lst - i - 1):
            if ord(lst[j]) > ord(lst[j + 1]):
                swapped_list(lst, j)

    for i in range(size_lst):
        dic_sec[lst[i]] = dic[lst[i]]

    return dic_sec
            

def main():
    cls()

    random_list = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
    # Expect output -> ["Rede", "Python", "inteligência", "dados", "Aprender"]

    random_dict = add_to_dict(random_list)

    random_dict = sorted_dict(list(random_dict.keys()), random_dict)
    
    print()
    style_p("End")
    style_p(random_dict)


if __name__ == "__main__":
    main()