# A Number Guessing game. With functions and a main game loop.
# Also, allows base game settings to be changed.

import random
from os import system, name

def intro():
    '''Explains the rules of the game.'''

    print("I will guess a random number within a given range.\nYou will have a set number of tries to guess it.\n")


def define_game_variables(change=False):
    """
    Sets the game variables to default values unless change requested.
    Allows those variables to be changed.
    """

    # Set Default game settings.
    default_range = list(range(1,11))
    default_guesses = 3

    # Change game settings.
    if change:
        print("\nThe new range will go from 1 to the number you choose below.\nChoose any positive number.")

        # Asks for new values for game variables and validates input.
        while True:
            try:
                new_range = int(input("\nWhat would you like the upper limit of the new range to be: "))
                if new_range <= 1:
                    raise ValueError
                break
            except ValueError:
                print("Enter a positive number other than 1.")

        # Define new value to the range variable.
        num_range = list(range(1, new_range + 1))

        while True:
            try: 
                new_guesses = int(input("\nHow many guesses would you like to allow? "))
                if new_guesses <= 0 or new_guesses > num_range[-1]:
                    raise ValueError
                break
            except ValueError:
                print(f"Enter a positive number no greater than {num_range[-1]}.")

        # Define new value to the guesses variable.
        num_guesses = new_guesses

    else:
        num_range = default_range 
        num_guesses = default_guesses

    return num_range, num_guesses


def display_game_settings(num_range, num_guesses):
    """Displays the games settings."""

    print(f"You have {num_guesses} attempt(s) to guess a number between {num_range[0]} and {num_range[-1]}.")
    if num_guesses == 3 and num_range[-1] == 10:
        print("(These are the default settings.)")
    else:
        print("(These are modified settings.)")


def change_game_settings():
    '''Asks user if they want to change game settings.'''

    change_settings = input("\nWould you like to change these settings? (Y/N) ")
    if change_settings.lower().startswith('y'):
        return True
    else:
        return False


def clear_screen():
    """Clears the screen at the start of the game."""

    # For Windows
    if name == 'nt':
        _ = system('cls')
    # For Linux
    else:
        _ = system('clear')


def play_the_game(num_range, num_guesses):
    """The number guessing game."""

    # Main game setup.
    clear_screen()
    intro()
    display_game_settings(num_range, num_guesses)
    num_to_guess = random.choice(range(1, num_range[-1]))
    
    # For Cheating/Testing - Black text on black background.
    print(f"\033[0;30m{num_to_guess}\033[0m")
    
    # Main loop.
    guess_count = 1
    while guess_count <= num_guesses:
        guess = input(f"Guess #{guess_count}: ")
        # Validate input.
        while not guess.isdecimal() or int(guess) not in num_range:
            print(f"Please enter a digit between {num_range[0]} and {num_range[-1]}.")
            guess = input(f"Guess #{guess_count}: ")
        # Check guess. If correct, break out of loop. Else, increase counter.
        if int(guess) == num_to_guess:
            print(f"\nCongratulations! You got it in {guess_count} guess(es).")
            break
        else:
            guess_count += 1
        
        # If player ran out of guesses, print message. 
        if guess_count > num_guesses:    
            print(f"\nSorry. You ran out of guesses.\nThe correct answer was {num_to_guess}.")

    play_again(num_range, num_guesses)
    

def play_again(num_range, num_guesses):
    """Asks the player if they would like to play the game again."""
    again = input("\nWould you like to play again? (Y/N): ")
    if again.lower().startswith('y'):
        reset = input("Would you like to use the current settings? (Y/N): ")
        if reset.lower().startswith('y'):
            play_the_game(num_range, num_guesses)
        else:
            main()
    else:
        print("\nThank you for playing.")
        exit


def main():
    """The main game loop."""
    clear_screen()
    num_range, num_guesses = define_game_variables()
    intro()
    display_game_settings(num_range, num_guesses)
    change = change_game_settings()
    if change == True:
        num_range, num_guesses = define_game_variables(change)
    play_the_game(num_range, num_guesses)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
