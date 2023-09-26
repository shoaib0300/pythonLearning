import random

# List of words for the game
word_list = ["apple", "banana", "cherry", "dog", "elephant", "frog", "grape", "horse", "igloo", "jungle"]


# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)


# Function to display the current state of the word with blanks and correctly guessed letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


# Function to play the Hangman game
def play_hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        if set(guessed_letters) == set(word):
            print("Congratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("You ran out of attempts. The word was:", word)


# Start the game
if __name__ == "__main__":
    play_hangman()
