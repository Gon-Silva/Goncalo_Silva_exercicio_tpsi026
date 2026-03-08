# Function that check the input of the user
def check_week_day (week_days):

    print(f"\nInput > {week_days}")

    # Use match to check the input of the user
    match (week_days):
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print("Output > Day of the week\n")
        case "Saturday" | "Sunday":
            print("Output > Weekend\n")
        case _:
            print("Error, try again")

# Main fuction
def main():
    week_day = input("\nEnter the day of the week: ")
    check_week_day(week_day)

# Start the program
if __name__ == "__main__":
    main()