def cls():
    # Clears the terminal screen using ANSI escape codes
    print("\033[H\033[2J", end="")
    print("\033[H\033[3J", end="")
    print("\033c", end="")

def join_dic(dic_1 :dict, dic_2 :dict):
    return dic_1 | dic_2
        

        
def main():
    cls()

    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 3, 'd': 4}

    d3 = join_dic(d1, d2)

    print(d1)
    print(d2)
    print(d3)

if __name__ == "__main__":
    main()                            