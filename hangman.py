import random

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
       ===
    """,
    """
     +---+
     O   |
         |
         |
       ===
    """,
    """
     +---+
     O   |
     |   |
         |
       ===
    """,
    """
     +---+
     O   |
    /|   |
         |
       ===
    """,
    """
     +---+
     O   |
    /|\  |
         |
       ===
    """,
    """
     +---+
     O   |
    /|\  |
    /    |
       ===
    """,
    """
     +---+
     O   |
    /|\  |
    / \  |
       ===
    """
]

WORDS = ["python", "hangman", "challenge", "programming", "openai", "computer", "science"]

def get_random_word(word_list):
    return random.choice(word_list)

def display_board(hangman_pics, missed_letters, correct_letters, secret_word):
    print(hangman_pics[len(missed_letters)])
    print()
    print("Letters ye missed:", " ".join(missed_letters) if missed_letters else "None, matey!")
    guesses_left = len(hangman_pics) - 1 - len(missed_letters)
    print(f"Ye have {guesses_left} guesses left, arrr!")
    blanks = [letter if letter in correct_letters else '_' for letter in secret_word]
    print("The word be:", " ".join(blanks))
    print()

def get_guess(already_guessed):
    while True:
        guess = input("Take a guess at a letter, ye scallywag: ").lower()
        if len(guess) != 1:
            print("Avast! Only one letter at a time, matey!")
        elif not guess.isalpha():
            print("Arrr! That be no letter! Try again, landlubber.")
        elif guess in already_guessed:
            print("Ye already guessed that letter! Try a new one, arrr!")
        else:
            return guess

def play_again():
    return input("Do ye want to play again, or be ye scared? (aye or nay): ").lower().startswith('y')

    print("ARRR! Welcome to Hangman, ye salty dog!")
    missed_letters = []
    correct_letters = []
    secret_word = get_random_word(WORDS)
    game_is_done = False

    while True:
        display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters.append(guess)
            if all(letter in correct_letters for letter in secret_word):
                print(f"Yo-ho-ho! Ye found the word: '{secret_word}'! Ye be a true pirate!")
                game_is_done = True
        else:
            missed_letters.append(guess)
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
                print(f"Arrr! Ye be out of guesses! The word was '{secret_word}'. Walk the plank!")
                game_is_done = True

        if game_is_done:
            if play_again():
                missed_letters = []
                correct_letters = []
                secret_word = get_random_word(WORDS)
                game_is_done = False
            else:
                print("Fair winds and following seas, matey!")
                break

if __name__ == "__main__":
    main()
