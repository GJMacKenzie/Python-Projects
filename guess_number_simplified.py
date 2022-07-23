# Simplified Number Guessing Game (without Functions or Main loop).


# List to guess from.
import random


# Settings
list_range = list(range(1, 11)) 
# print("Numbers to choose from:", *list_range, "Type:", type(list_range))
num_guesses = 3
# print("Number of guesses:", num_guesses, "Type:", type(num_guesses))


# Select an number from the list. 
num_to_guess = random.choice(range(list_range[0], list_range[-1]))
# print("Number to try and guess:",num_to_guess, "Type:", type(num_to_guess))


# Main game intro.
print(f"\nYou have {num_guesses} tries to guess a number I have chosen between {list_range[0]} and {list_range[-1]}.")


# Main game loop
guess_count = 1         # Set variable for counter.
while guess_count <= num_guesses:
    player_guess = input(f"Guess #{guess_count}: ")

    # Validate input:
    while not player_guess.isdecimal() or int(player_guess) not in list_range:
        print(f"Enter a number between {list_range[0]} and {list_range[-1]}.")
        player_guess = input(f"Guess #{guess_count}: ")

    # Check guess. If correct, break out of loop. Else, increase counter.
    if int(player_guess) == num_to_guess:
        print(f"\nCorrect! You got it in {guess_count} guess(es).")
        break
    else:
        guess_count += 1


# If player ran out of guesses, print message.        
if guess_count > num_guesses:
    print(f"\nSorry, you ran out of guesses. The correct answer was {num_to_guess}.")

# Play again Y/N would go here.

# Print exit message.
print("Thank you for playing.")
