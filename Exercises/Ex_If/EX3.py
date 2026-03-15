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
    print("        ASCENDING & DESCENDING          ")
    print("========================================")

# Function that ascending an array
def ascending_array(arr , size):
    temp = arr[0]

    for i in range(size):
        for j in range(0, size - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1] 
                arr[j + 1] = temp

    return arr

# Function that descending an array
def descending_array(arr, size):
    temp = arr[0]

    for i in range(size):
        for j in range(0, size - i - 1):
            if arr[j] < arr[j + 1]:
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

    size = len(arr)

    print("")

    ascending_array(arr, size)

    print(" > Ascending: ", end="")

    for i in range(size):
        print(arr[i], end="")
        if(i != size):
            print(", ", end="")

    print("")

    descending_array(arr, size)

    print(" > Descending: ", end="")

    for i in range(size):
        print(arr[i], end="")
        if(i != size):
            print(", ", end="")

    print("\n")

# Start the program
if __name__ == "__main__":
    main()