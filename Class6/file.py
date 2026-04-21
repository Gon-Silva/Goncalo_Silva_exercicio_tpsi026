import os

def cls():
    # Clears the terminal screen using ANSI escape codes
    print("\033[H\033[2J", end="")
    print("\033[H\033[3J", end="")
    print("\033c", end="")

def main():
    cls()

    '''
        qualquer ação com ficheiros
        
        read, write, append, binario

        Ações que devemos ter

        1 - open file

        2 - alguma ação

        3 - close file
    '''

    file_name = "./Dados/data.txt"

    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as m_file:
            text = m_file.read()
            print("No file ", text)
    
    else:
        os.makedirs(os.path.dirname(file_name), exist_ok=True)

        print("No file ", text)

    text = input("Introduz uma frase: ")

    with open(file_name, "w", encoding="utf-8") as m_file:
         m_file.write(text)


        
if __name__ == "__main__":
    main()