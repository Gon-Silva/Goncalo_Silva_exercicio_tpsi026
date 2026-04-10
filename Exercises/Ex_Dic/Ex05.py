def cls():
    # Clears the terminal screen using ANSI escape codes
    print("\033[H\033[2J", end="")
    print("\033[H\033[3J", end="")
    print("\033c", end="")

def count_letters(dic :dict, word :str):
    for letter in word:

        if dic.get(letter):
            count = dic[letter]
        else:
            count = 0

        count += 1
        dic[letter] = count

def print_dic(dic :dict):
    print(dic)

def main():
    cls()
    
    dic = {}

    word = input("Enter a word: ")

    count_letters(dic, word)

    print_dic(dic)

if __name__ == "__main__":
    main()