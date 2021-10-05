import random

def play():
    print_header()

    secret_word = choose_secret_word()
    hitted_letters = initialize_list(secret_word)
    print(f"\n{hitted_letters}")

    hanged = False
    user_won = False
    errors = 0

    while(not hanged and not user_won):
        user_attempt = requests_user_attempt()

        if(user_attempt in secret_word):
            adds_correct_attempt(user_attempt, hitted_letters, secret_word)
        else:
            errors += 1
            attempts_left = 7 - errors
            attempts_text = "attempts" if attempts_left > 1 else "attempt"
            print(f"You missed. You have {attempts_left} {attempts_text} left")
            print_hangman(errors)

        hanged = (errors == 7)
        user_won = ("_" not in hitted_letters)
        print(hitted_letters)

    if(user_won):
        print_win_message()
    else:
        print_loser_message(secret_word)

def print_header():
    print("***************************")
    print("Welcome to the hangman game")
    print("***************************")

def choose_secret_word(file_name="words.txt", first_line=0):
    words_list = []
    with open(file_name, "r") as file:  # If some error happens or not, the file.close() will be called automatically
        for line in file:
            line = line.strip()  # It removes "\n"
            words_list.append(line)
        file.close()

    word_position = random.randrange(first_line, len(words_list))
    secret_word = words_list[word_position].strip().upper()
    return secret_word

def initialize_list(secret_word):
    return ["_" for letter in secret_word]# Filling the list with "_"

def requests_user_attempt():
    return input("Type a letter: ").strip().upper()

def adds_correct_attempt(user_attempt, hitted_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (letter == user_attempt):
            hitted_letters[index] = letter
        index += 1

def print_win_message():
    print("Congratulations, you WON!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_loser_message(secret_word):
    print("You LOST. Try it again!")
    print("The word was: {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def print_hangman(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == '__main__':
    play()
