# A deductive logic game, where you must guess a secret number based on clues.
# By Joe MacKenzie. Finished on 3 Jul 2022.
# Inspired from 'The Big Book of Small Python Projects' - Project 'Bagels'
# View Original code here: https://nostarch.com/big-book-small-python-projects

import random, os

# Game variables
secret_number_length = 5    # Sets length of the word from 1 to 10.
max_guesses = 10            # Sets the maximun number of guesses.

class Color:
    """A class for easily adding color to text. Used for giving hints."""
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def intro():
    """Welcomes the player and explains the rules with a whole lot ot text."""
    print(f'{Color.BOLD}Welcome to my number guessing game!{Color.END}\n')
    print(f"I will think of a {Color.DARKCYAN}{secret_number_length}{Color.END}-digit number (with no repeating digits).")
    print(f"You have {Color.DARKCYAN}{max_guesses}{Color.END} guesses to try and figure it out.")
    print("\nAfter each guess, I will repeat your guess back with color-coded hints.")
    print(f"{Color.GREEN}Green{Color.END}: means it is the right number and in the right position.")
    print(f"{Color.YELLOW}Yellow{Color.END}: means the number is correct, but in the wrong position.")
    print(f"{Color.RED}Red{Color.END}: means the number is not in the solution at all.")
    print(f"Example: {Color.GREEN}5{Color.YELLOW}4{Color.RED}6{Color.END}")
    print(f"Means: 5 is correct, 4 is in the wrong pisition and 6 isn't part of the answer.")

def get_secret_number():
    """Generates a secret number the player will try to guess."""
    # List of available characters to choose from.
    data_choices = list('0123456789')
    # Randomize list of data choices
    random.shuffle(data_choices)    
    # Randomizes whether secret number is chosen from beginning or end of list.
     # And turns selection into a string.
    second_random = (random.randint(0, 1))
    if second_random == 0:
        secret_number = ''.join(str(i) for i in data_choices[:secret_number_length])
        # ▲▲▲ A clearer version of what happens above. Down here.▼▼▼
        # secret_number = data_choices[:secret_number_length]
        # secret_number = ''.join(str(i) for i in secret_number)
    else:
        secret_number = ''.join(str(i) for i in data_choices[-secret_number_length:])
    return secret_number

def hints(guess, secret_number):
    """Analyzes the players guess and provides hints."""
    if guess == secret_number:
        return '1' 
    # Make dictionary to save hints.
    guess_hints = {}
    for x in range(len(guess)):
        if guess[x] == secret_number[x]:
            guess_hints[guess[x]] = '\033[92m'
            # print(f"{Color.GREEN}{guess[x]}{Color.END}") - Didn't work. DEL
        else:
            if guess[x] in secret_number:
                guess_hints[guess[x]] = '\033[93m'
                # print(f"{Color.YELLOW}{guess[x]}{Color.END}") - DEL
            else:
                guess_hints[guess[x]] = '\033[91m'
                # print(f"{Color.RED}{guess[x]}{Color.END}") -DEL
    else:
        print("HINT: ", end='')
        for num, col in guess_hints.items():
            # new_hints = (f"{col}{num}{Color.END}, end=''") - NOT Needed?- DEL
            # return new_hints
            print(f"{col}{num}{Color.END}", end='')
        print("\n")
        
def guess_loop(secret_number):
    """
    The loops through the players guesses and provide feed back by using the hints function. It ends the loop if the player gets the answer or runs out of attempts.
    """
    # Intro text at start of guess loop.
    print(f"\n{Color.BOLD}Let's play!{Color.END}")
    print(f"{Color.BOLD}I have chosen a {Color.END}{Color.DARKCYAN}{secret_number_length}{Color.END}{Color.BOLD}-digit number. You have{Color.END} {Color.DARKCYAN}{max_guesses}{Color.END}{Color.BOLD} tries to guess it.{Color.END}")
    # Guess loop
    loop_count = 1
    guess = ''
    while loop_count <= max_guesses:
        guess = input(f"Guess #{loop_count}: ")
        # The code on the line below was taken from the original source. Input 
         # validation is hard. MODIFIED to not allow repeated digits.
        while len(set(guess.replace(" ", ""))) != secret_number_length or not guess.isdecimal() or not len(guess) == secret_number_length:
            print(f"Please enter a {Color.DARKCYAN}{secret_number_length}{Color.END}-digit number with no repeated digits.")
            guess = input(f"Guess #{loop_count}: ")
        exit_loop = hints(guess, secret_number)
        if exit_loop == '1':
            if loop_count == 1:
                print(f"You are correct!!!\nYou got it on the {Color.GREEN}{loop_count}st{Color.END} try. Amazing.")
                break
            else:
                print(f"You are correct!!!\nYou got it in {Color.GREEN}{loop_count}{Color.END} tries.")
                break
        loop_count += 1
        if loop_count > max_guesses:
            print(f"Sorry. You ran out of guesses. \nThe answers was {Color.GREEN}{secret_number}.{Color.END}")

def main():
    """The main loop of the game."""  
    while True:
        # Clears the screen at the start of the game.
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print Intro text
        intro()
        # Generates a Secret Number
        secret_number = get_secret_number()
        # print(secret_number) # Used for testing - DELETE or Comment Out
        # Loop through the players guesses with hints. Ends if correct answer 
         # given or out of guesses.
        guess_loop(secret_number)
        # Play again? Breaks out of main game loop if anything other than 'Y/y'.
        again = input("\nWould you like to play again? Y/N: ")
        if not again.lower().startswith('y'):
            print('\nThanks for playing.')
            break

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
