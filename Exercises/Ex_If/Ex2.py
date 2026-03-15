import os
import platform

# This function clean the console
# For this, I need to import modules like « os » and « platform »

    # os permit to interact with operating system
    # platform permit the program to understand what type of operating system the user is using

# Function to clean the console
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Function to print a header
def print_header():
    print("========================================")
    print("        FIND THE BIGGEST NUMBER         ")
    print("========================================")

# Function that sort the array
def sort_array(arr):
    size = len(arr)
    temp = arr[0]

    for i in range(size):
        for j in range(0, size - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1] 
                arr[j + 1] = temp

    return arr


def main():
    clear_console()

    print_header()

    # Create a array
    arr = []

    print("\n > Insert the first number")
    arr.append(int(input("  > ")))

    print("\n > Insert the second number")
    arr.append(int(input("  > ")))

    print("\n > Insert the third number")
    arr.append(int(input("  > ")))

    sort_array(arr)

    print(f"\n > The biggest is {arr[len(arr) - 1]}")
    print(f" > The lowest is {arr[0]}")

    print("")

# Start the program
if __name__ == "__main__":
    main()