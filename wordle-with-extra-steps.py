import random
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init()

# This is a list of 5-letter words that will be used in the game
words = ["apple", "grape", "peach", "mango", "lemon", "berry", "melon", "olive"]

def wordpicker():
    """Pick a random word from the list."""
    return random.choice(words)

def checker(mystery_word, guesser):
    """
    Check if the guesser's letter is in the mystery word.
    Returns the response with the correct letters in the right place ('green'),
    and the correct letters in the wrong place ('yellow').
    """
    response = []
    for i in range(5):
        if guesser[i] == mystery_word[i]:
            response.append("green")  # The letter is in the right place
        elif guesser[i] in mystery_word:
            response.append("yellow")  # The letter is in the wrong place
        else:
            response.append("red")  # The letter is not in the word
    return response

def display_response(guesser, response):
    """Displays the feedback to the guesser."""
    outcome = []
    for i in range(5):
        character = guesser[i]
        rp = response[i]
        if rp == "green":
            outcome.append(f"\033[92m{character}\033[0m")  # Correct position
        elif rp == "yellow":
            outcome.append(f"\033[93m{character}\033[0m") # Wrong position
        else:
            outcome.append(f"\033[91m{character}\033[0m")  # Not in the word
    print(" ".join(outcome))


def wordle():
    """This is the main function that runs the game."""
    print("Welcome to Wordle but you lose health as you guess wrong and you regain health if you get an answer right! (Score Tracker Included)")
    print("Guess the 5 letter word. You have 6 attempts each round. (good luck and enjoy dawg)")
    print("Response: Green = Correct letter in the right place, Yellow = Correct letter in the wrong place, Red = Incorrect letter")

    max_hp = 10  # You start with 10 health points
    hp = max_hp
    tscore = 0  # Total score for the game
    hscore = 0  # High score for the game
    sessions = 0  # Number of rounds played

    while hp > 0:
        mystery_word = wordpicker()
        attempts = 6  # You have 6 attempts to guess the word
        score = 0  # Score for the round
        correct_guess = False

        print(f"\nRound {sessions + 1}")
        print(f"Health: {hp}/{max_hp}")

        for tries in range(attempts):
            while True:
                guesser = input(f"Attempt {tries + 1}/{attempts}: ").lower()
                
                # Manually check if the word is exactly 5 letters long and alphabetic
                valid = True
                count = 0
                for char in guesser:  # Manually count characters
                    if not char.isalpha():  # Invalid if non-alphabetic
                        valid = False
                        break
                    count += 1
                if count != 5:  # If it's not exactly 5 characters
                    valid = False
                
                if valid:
                    break  # If valid, exit the loop
                print("Invalid input. Please enter a valid 5-letter word.")
            
            response = checker(mystery_word, guesser)
            display_response(guesser, response)

            if guesser == mystery_word:
                correct_guess = True  # The word is guessed correctly
                score = attempts - tries  # Points are based on the number of attempts left
                tscore += score  # Total score is updated
                hp = min(max_hp, hp + 1)  # Regain health by 1 point
                print(f"Correct! The word is {mystery_word}. You scored {score} points.")
                print(f"You scored {score} points this round. Total score: {tscore}")
                print(f"Health restored to {hp}/{max_hp}.")
                break

        if not correct_guess:
            hp -= 1  # Damage taken for incorrect guess
            print(f"\nYou have used all your attempts. The word was {mystery_word.upper()}.")
            print(f"You took 1 damage. Health: {hp}/{max_hp}")

        sessions += 1

        # High score is updated
        if tscore > hscore:
            hscore = tscore
            print(f"\nNew Personal Best! Score: {hscore}")

        # Checks the health points
        if hp <= 0:
            print("\nGame Over! You have run out of health. (skill issue)")
            break

        # Asks if the player wants to play again
        while True:
            one_more = input("Do you want to play another round? (yes/no): ").lower()
            if one_more == "yes":
                break # Continues the game if the answer is "yes"
            elif one_more == "no":
                print("\nThank you for playing Wordle! Here are your final stats: ")
                print(f"Rounds played: {sessions}")
                print(f"Total score: {tscore}")
                print(f"High score: {hscore}")
                sys.exit()  # Exits the game if the answer is "no"
            else:
                print("Just yes or no is it that hard to ask? :) ")
def main_menu():
    """Displays the main menu and start the game or exit based on user input."""
    while True:
        print("\nMain Menu")
        print("\nWordle with extra steps")
        print("1. Start Game")
        print("2. Exit")
        choice = input("Pick 1 or 2: ")
        if choice == "1": #This starts the game
            wordle() 
            break
        elif choice == "2":
            print("Exiting the game...") #Exits the game
            break
        else:
            print("Invalid choice. Just 1 or 2 no funny business.")
# Runs the game
if __name__ == "__main__":
    main_menu()