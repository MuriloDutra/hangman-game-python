def play():
    print("***************************")
    print("Welcome to the hangman game")
    print("***************************")

    secret_word = "banana".strip().upper()
    hanged = False
    user_won = False
    errors = 0
    hitted_letters = ["_", "_", "_", "_", "_", "_"]

    print()
    print(hitted_letters)
    while(not hanged and not user_won):
        user_attempt = input("Type a letter: ").strip().upper()

        if(user_attempt in secret_word):
            index = 0
            for letter in secret_word:
                if(letter == user_attempt):
                    hitted_letters[index] = letter
                index += 1
        else:
            errors += 1
            attempts_left = 6 - errors
            attempts_text = "attempts" if attempts_left > 1 else "attempt"
            print(f"You missed. You have {attempts_left} {attempts_text} left")
        hanged = (errors == 6)
        user_won = ("_" not in hitted_letters)
        print(hitted_letters)

    if(user_won):
        print("You WON, congratulations!!!")
    else:
        print("You LOST, try it again.")
    print("Game over.")

if __name__ == '__main__':
    play()
