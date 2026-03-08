# Function that check the input of the user
def Type_order (type_order, value_order):

    match type_order:
        case 1:
            type_order_string = "purchase"
        case 2:
            type_order_string = "sale"
    
    print(f"\nInput > {{\"Type\": {type_order_string}, \"Value\": {value_order}}}")
    
    print("Output > ", end=" ")
    # Use match to check the input of the user
    match type_order:
        case 1:
            print(f"Purchase of {value_order}€\n")
        case 2:
            print(f"Sale of {value_order}€\n")

# Main fuction
def main():
    print("\n| 1 - Purchase")
    print("| 2 - Sale\n")

    print("Enter the type of order:\n")

    type_order = int(input(" > "))

    print("\nEnter the of value of order:\n")
    value_order = int(input(" > "))

    if (type_order < 0 or type_order > 2) and (value_order < 0):
        print("The type is incorrect and value order can't be lower than 0")
    else :
        Type_order(type_order, value_order)

# Start the program
if __name__ == "__main__":
    main()