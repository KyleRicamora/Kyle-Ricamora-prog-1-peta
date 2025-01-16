# Wordle (with extra steps)

## Installation
Use these easy steps to create and launch a Wordle-like Python word-guessing game:

1. Python Version must be 3.12.6 (I tried running this in 3.11.9, it didn't work so I suggest downloading this version.)

2. Set Up Required Libraries:
- Launch your terminal or command prompt.
- To enable colorful terminal text, install the colorama library:
    #### Visual Studio Code Terminal:
  
    ![image](https://github.com/user-attachments/assets/5a8b322a-20a9-40d4-b810-49f39065bd6d)

    #### Command Prompt:

    ![image](https://github.com/user-attachments/assets/036dbbda-643a-4857-bd11-3a23de00627f)

  ```bash
  pip install colorama
  ```
  
- Colorama is a Python package that makes it easier to style and add colored text to terminal output. It's very helpful when we want to add visual appeal to our console programs or when we need to draw attention to specific areas of our output to improve readability.

  2.1 Make sure the colorama is installed correctly:
    - First, make sure your Python environment has the colorama module loaded. Launch the terminal or command prompt and type:

  ![image](https://github.com/user-attachments/assets/8ec3bbae-b771-434d-83ec-c5efe81529fc)

  ```bash
  pip show colorama
  ```

  (also works in vscode terminal)

  2.2 Check the Python environment:
    - Make sure the Python environment in which colorama is installed is the proper one. Before running the script, make sure the virtual environment is activated if you're using one:

    ```bash
    # Windows
    path\to\venv\Scripts\activate
    # MacOS/Linux (imagine using MacOS)
    source path/to/venv/bin/activate
    ```

3. Running the game in Command Prompt (Since you can already run this in VSCode.)
   - Open Command Prompt
   - Open the folder in which wordle-with-extra-steps.py was downloaded. Make use of the cd command:

    ```bash
    cd path\to\your\file
    ```

  - Enter the real folder location where wordle-with-extra-steps.py is stored instead of path\to\your\file (who am I kidding just find the folder where you stored the file).
  Example:
    ```bash
    cd C:\Users\YourUsername\Documents
    ```
  - Run the game by simply typing:
    ```bash
    python wordle-with-extra-steps.py
    ```

## Concept:
In this text-based game, players must guess a concealed word by recommending letters in a set amount of time.

## Features:

  1. Random Word Selection: A word is selected at random from a predetermined list to begin each game.
 
  2. Limited Attempts: Players can only guess the word a certain number of times, like twelve.
  
  3. Progress Display: The word with the guessed letters revealed and the unknown letters displayed as underscores is shown in the game.
  
  4. Score tracking: When a word is successfully guessed, points are given according to the amount of attempts left. Throughout rounds, the total and high scores are monitored.
  
  5. Win/Lose Conditions: When the player correctly guesses the word or uses up all of their efforts, the game is over.

  6. Players begin with 10 health points (HP), which they can increase to a maximum of 10 HP by winning 1 HP for each right guess and losing 1 HP for each round in which they are unable to guess the word.

  7. Colored Feedback: Following each guess, the state of the letters is indicated via a color display:
  - Green: The right letter in the right place.
  - Yellow: The right letter is positioned incorrectly.
  - Red: The letter is incorrect.

## Mechanics:

  1. Word Selection: At the beginning of each game, a random word is selected from a predetermined list.
  
  2. Input: Players enter a five-letter word guess on each try.
    
  4. Game Progression: Until the player guesses the complete word or uses up all of the permitted attempts, the game goes on.

  5. Main Menu: Players have the option to leave the main menu or launch a new game.

  6. Validation: To make sure the inputs are five-letter alphabetic words, they undergo validation.

  7. Attempts: You can guess the word up to six times per round.

  8. Health Management: 1 HP is lost if the word cannot be guessed within six attempts whereas one HP is restored if the guess is accurate.

  9. Game Over: When the player's HP decreases to 0, the game is over.

## Controls:
  1. Main Menu: Press '1' to start the game or '2' to end it.
  
  2. In-game: To make a guess, type a five-letter word and hit Enter.
  
  3. Post-Round: Type "yes" to continue playing after each round, or "no" to end it.

## Known Bugs and Limitations (will fix soon)
  1. Input Validation: Non-alphabetic characters or inputs of the wrong length might not be robustly handled by the existing validation technique.
  
  2. Case Sensitivity: When inputs are converted to lowercase, mixed-case or uppercase inputs may result in unexpected behavior.
  
  3. Restricted Word List: The game's limited word list may make it less replayable.
  
  4. Health Cap: Players can not gain more health for consecutive right guesses since health points are limited to 10.
  
  5. No Persistence: Game progression and scores are not saved between sessions.

### The structure and operation of the game are clearly understood from this summary, which also points out areas that might use further work or improvement.
