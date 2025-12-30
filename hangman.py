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
    print("Missed letters:", " ".join(missed_letters))
    guesses_left = len(hangman_pics) - 1 - len(missed_letters)
    print(f"Guesses left: {guesses_left}")
    blanks = [letter if letter in correct_letters else '_' for letter in secret_word]
    print("Word:", " ".join(blanks))
    print()

def get_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter a LETTER.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        else:
            return guess

def play_again():
    return input("Do you want to play again? (yes or no): ").lower().startswith('y')

def main():
    print("HANGMAN GAME")
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
                print(f"Yes! The secret word is '{secret_word}'! You have won!")
                game_is_done = True
        else:
            missed_letters.append(guess)
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
                print(f"You have run out of guesses! The word was '{secret_word}'.")
                game_is_done = True

        if game_is_done:
            if play_again():
                missed_letters = []
                correct_letters = []
                secret_word = get_random_word(WORDS)
                game_is_done = False
            else:
                break

if __name__ == "__main__":
    main()
