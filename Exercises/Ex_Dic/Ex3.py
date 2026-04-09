def cls():
    # Clears the terminal screen using ANSI escape codes
    print("\033[H\033[2J", end="")
    print("\033[H\033[3J", end="")
    print("\033c", end="")

def check_input(input_message :str):
    while True:
        try:
            input_user = int(input(input_message))
            return input_user
        except ValueError:
            print("[ERROR] Must be a number")

def print_dict(dic :dict):
    print(f"\nName: {dic['name']}")
    print(f"Price: {dic['price']}")

def add_information(dic :dict):
    name = input("Name: ")
    price = check_input("Price: ")
    stock = check_input("Stock: ")

    current_key = len(dic)

    dic.update({
            'name': name,
            'price': price,
            'stock': stock
    })

def remove_information(dic :dict):
    dic = dic.pop("stock")

def main():

    cls()

    # Empty dictionary
    products = {}

    add_information(products)

    remove_information(products)

    print_dict(products)

if __name__ == "__main__":
    main()