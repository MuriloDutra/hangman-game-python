import random

def play():
    print("***************************")
    print("Welcome to the hangman game")
    print("***************************")

    words_list = []
    with open("words.txt", "r") as file:#If some error happens or not, the file.close() will be called automatically
        for line in file:
            line = line.strip()#It removes "\n"
            words_list.append(line)
        file.close()

    word_position = random.randrange(0, len(words_list))
    secret_word = words_list[word_position].strip().upper()
    hanged = False
    user_won = False
    errors = 0
    hitted_letters = ["_" for letter in secret_word]#Filling the list with "_"

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
