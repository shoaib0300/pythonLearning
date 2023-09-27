import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 20.")

# Set the number of attempts
attempts = 3

while attempts > 0:
    print(f"You have {attempts} attempts left.")

    # Ask the player for their guess
    guess = int(input("Guess the number: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You've guessed the number correctly.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

    # Decrement the attempts
    attempts -= 1

# If all attempts are used up, reveal the correct number
if attempts == 0:
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
