def cls():
    # Clears the terminal screen using ANSI escape codes
    print("\033[H\033[2J", end="")
    print("\033[H\033[3J", end="")
    print("\033c", end="")

def count_word(phrase :str):
    phrase = phrase.split()

    dic_count = {}

    for word in phrase:
        if dic_count.get(word):
            count = dic_count[word]
        else:
            count = 0

        count += 1
        dic_count[word] = count

    return dic_count

def main():
    cls()

    phrase = input("Write a phrase: ")

    dic = count_word(phrase)

    print(dic)

if __name__ == "__main__":
    main()  