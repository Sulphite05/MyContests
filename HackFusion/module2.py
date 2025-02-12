# Sulphitesimal
# Member: Aqiba Abdul Qadir

import random
from time import time
import sqlite3

words = ['choose', 'world', 'log', 'terrible', 'cater', 'terminate', 'from', 'whatever', 'allocate', 'here', 'the',
         'are', 'what', 'backward', 'is', 'move', 'deallocate', 'system', 'forward', 'henceforth', 'you', 'allow',
         'wonder', 'Hello', 'sip', 'creation']


def dbs(user, score=0):
    conn = sqlite3.connect()
    conn.execute('Create Table scores'
                 'User TEXT'
                 'Score INTEGER)')
    conn.execute('INSERT INTO scores')


def hangman(lives):
    if lives == 6:
        print("""
                    |_|
                    /|\
                     |
                    / \ """)
    elif lives == 5:
        print("""
                   |_|
                    |\
                    |
                   / \ """)
    elif lives == 4:
        print("""
                   |_|
                    |
                    |
                   / \ """)
    elif lives == 3:
        print("""
                   |_|
                    |
                    |
                     \ """)

    elif lives == 2:
        print("""
                   |_|
                    |
                    |
                      """)
    elif lives == 1:
        print("""
                   |_|


                      """)


def play(word):
    lives = 6
    total_letters = set(word)

    correct = set()

    guessed_letters = set()
    display_word = '_' * len(word)

    score = 0  # fetch later
    while lives > 0 and len(correct) != len(total_letters):
        hangman(lives)  # TO DO: Display hangman stick
        print(display_word)
        print("You have 30 seconds!")
        now = time()
        while True:
            alpha = input("Enter an alphabet")
            if time() - now > 30:
                lives -= 1
                print("Time was over! You lost a life")
                break
            if alpha in guessed_letters:
                print('Try again!')
            elif len(alpha) > 1:
                print("Enter a single alphabet only!")
            else:
                guessed_letters.add(word)
                if alpha in total_letters:
                    correct.add(alpha)
                    print("Correct!")
                else:
                    lives -= 1
                    print("Incorrect! You lost a life")
                new = []
                for a in word:
                    if a in correct:
                        new.append(a)
                    else:
                        new.append('_')
                display_word = ''.join(new)
                break
    if not lives:
        print("You lose!")
        return 0
    else:
        score += 1
        # TODO: store to dbs
        print("Congratulations! You won!")
        # display leaderboard
        return 1


def single_play(pl):
    word = random.choice(words)
    play(word)


def multiplay(pl1, pl2):
    print(f"{pl2}, please look away :))")
    word = ''
    while not word:
        word = input(f"{pl1}, please enter a word quickly!")
        if not word:
            print("Enter a word, not an empty string, genius :)")

    print("\n" * 20)  # This is to hide the word
    print(f"{pl2},  you can now begin playing :))")
    play(word)


def challenge(pl):
    curr = 2
    word = ''
    while curr < 8:
        while len(word) != curr:
            word = random.choice(words)
        print(f"Difficulty level {curr - 1}")
        if play(word):  # means the user won so we increase difficulty
            curr += 1
    print("Congrats! You won all the levels")


while True:
    opt = input("Select Game Mode:\n1. Single Player\n2. Multiplayer\n3. CHALLENGE Mode")
    if opt == '1':
        pl1 = input('Enter your handle:')
        single_play(pl1)

    elif opt == '2':
        pl1 = input('Enter your handle, player 1:')
        pl2 = input('Enter your handle, player 2:')
        multiplay(pl1, pl2)

    elif opt == '3':
        pl1 = input('Enter your handle:')
        challenge(pl1)

    else:
        print("Invalid choice. Restarting...")
        continue
    ch = input("Would you like to play again?(Y/N)")
    if ch == 'N':
        print("Good bye!")
        break


