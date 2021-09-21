def play():
    print("***************************")
    print("Welcome to the hangman game")
    print("***************************")

    secret_word = "banana"
    hanged = False
    user_won = False

    while(not hanged and not user_won):
        user_attempt = input("Type a letter: ")
        index = 0

        for letter in secret_word:
            if(letter == user_attempt):
                print(f"Found the letter {user_attempt} in the position {index} ")
            index = index + 1

if __name__ == '__main__':
    play()
