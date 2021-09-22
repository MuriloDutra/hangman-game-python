def play():
    print("***************************")
    print("Welcome to the hangman game")
    print("***************************")

    secret_word = "banana".strip().lower()
    hanged = False
    user_won = False
    hitted_letters = ["_", "_", "_", "_", "_", "_"]

    print()
    print(hitted_letters)
    while(not hanged and not user_won):
        user_attempt = input("Type a letter: ").strip().lower()
        index = 0

        for letter in secret_word:
            if(letter == user_attempt):
                hitted_letters[index] = letter
            index = index + 1
        print(hitted_letters)

if __name__ == '__main__':
    play()
