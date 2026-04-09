def cls():
    # Clears the terminal screen using ANSI escape codes
    print("\033[H\033[2J", end="")
    print("\033[H\033[3J", end="")
    print("\033c", end="")

def swap_dic(dic :dict):
    a = {}
    for i in dic:
        a.update({dic[i]: i})

    return a

def main():
    cls()

    d = {'a': 1, 'b': 2, 'c': 3}

    print(d)
    print(swap_dic(d))
if __name__ == "__main__":
    main()