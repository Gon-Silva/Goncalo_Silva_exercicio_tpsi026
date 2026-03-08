# Function that check the input of the user
def check_grade (grade):

    print(f"\nInput > {grade}")

    # Use match to check the input of the user
    match (grade):
        case grade if grade >= 90:
            print("Excellent\n")
        case grade if grade >= 70:
            print("Good\n")
        case grade if grade >= 50:
            print("Sufficient\n")
        case grade if grade < 50:
            print("Insufficient\n")
        case _:
            print("Error, try again")

# Main fuction
def main():
    grade = int(input("\nEnter the grade: "))
    if grade > 100 or grade < 0:
        print("\nThe grade can't be higher than 100 or lower than 0\n");
    else:
        check_grade(grade)

# Start the program
if __name__ == "__main__":
    main()