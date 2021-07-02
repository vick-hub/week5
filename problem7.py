import os
import sys
import random

"""
Notes:
- Very good.
- Ask the user to only enter one letter 'r', 'p' or 's' and 'x' for exit
"""

def main():
    print(""""Rock, paper, scissors. This is a two-person game where both plays count down from 3
    then choose to say either 'rock', 'paper' or 'scissors'. Each time there is a winner based upon the following 
    rules:
    - rock vs. paper: paper wins because a rock can be wrapped in a paper;
    - rock vs. scissors: rock wins because a rock can crush a pair of scissors;
    - paper vs. scissors: scissors wins because it can cut the paper.
    - when you type 'done' game is over.""")
    print('=' * 120)
    game = random.choice(['rock', 'paper', 'scissors'])
    # print(game)
    selection = input('Enter your selection: ')
    while selection != 'done':
        if game == selection:
            print("draw")
            selection = input('Enter your selection: ')
        if game == 'rock' and selection == 'paper':
            print("You won!!!")
        elif game == 'scissors' and selection == 'rock':
            print("You won!!!")
        elif game == 'paper' and selection == 'scissors':
            print("You won!!!")
        else:
            print("You lost!!!")
        selection = input('Enter your selection: ')
    print("Game is over.")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
