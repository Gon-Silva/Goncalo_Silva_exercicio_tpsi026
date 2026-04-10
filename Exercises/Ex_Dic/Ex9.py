def cls():
    # Clears the terminal screen using ANSI escape codes
    print("\033[H\033[2J", end="")
    print("\033[H\033[3J", end="")
    print("\033c", end="")

def average(total :int, count :int):
    return total / count

def create_dict_average(dic :dict):
    dic_average = {}
    for item in dic:
        total_sum = sum(dic[item])
        total_count = len(dic[item])

        dic_average.update({item: average(total_sum, total_count)})

    return dic_average

def print_result(dic :dict):
    for item in dic:
        print(f"{item}: {dic[item]}")

def main():
    cls()

    grades = {
        'João':  [7, 8, 9],
        'Maria': [10, 9, 8],
        'Ana':   [6, 7, 8]
    }

    average = create_dict_average(grades)

    print_result(average)

if __name__ == "__main__":
    main()  