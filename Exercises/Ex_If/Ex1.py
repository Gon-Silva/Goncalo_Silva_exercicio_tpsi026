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
    print("             CONVERT TIME               ")
    print("========================================")

def main():
    clear_console()

    print_header()

    print("\n > Insert the seconds")
    second = int(input("  > "))

    hour = int(second / 3600)
    minutes = int(second / 60 - hour * 60)
    second = second - (hour * 3600 + minutes * 60)

    print(f"{hour} hour, {minutes} minutes, {second} second\n")

# Start the program
if __name__ == "__main__":
    main()