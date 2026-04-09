def cls():
    # Clears the terminal screen using ANSI escape codes
    print("\033[H\033[2J", end="")
    print("\033[H\033[3J", end="")
    print("\033c", end="")

def check_data(dic: dict):
    required_fields = ['name', 'age', 'email']

    for field in required_fields:
        if dic.get(field):
            print(f"{field.capitalize()} found: {dic[field]}")
        else:
            print(f"{field.capitalize()} not found")

def main():
    cls()

    # dictionary
    user = {'name': 'Carlos', 'age': 28}

    check_data(user)

if __name__ == "__main__":
    main()