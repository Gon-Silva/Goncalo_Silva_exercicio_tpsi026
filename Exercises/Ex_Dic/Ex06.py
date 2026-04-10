def cls():
    # Clears the terminal screen using ANSI escape codes
    print("\033[H\033[2J", end="")
    print("\033[H\033[3J", end="")
    print("\033c", end="")

def sum_sells(dic :dict):
    total_sell = 0
    for moth in dic:
        total_sell += dic[moth]

    return total_sell

def main():
    cls()

    sells = {'January': 1000, 'February': 1500, 'March': 1200}

    print(f"The total is {sum_sells(sells)}")

if __name__ == "__main__":
    main()