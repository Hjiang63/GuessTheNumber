import random
from utilits import *
def play_game():
    print("Starting a new round...")
    # step1: generate a random target, and remember this target
    rand_target = random.randint(1, 100) # 1<= target <= 100
    print("A random integer between 1 and 100 (both inclusive) is generated.")
    # let the user keep guesing until right (while) - many times
    while True: #boolean type: yes (ture)/no (false)
        # ask for the guess
        user_guess = input("please take a guess: ").strip() #strip (): clean the white space at the beigining and the end of a string
        #  make sure the user input is a number
        if not user_guess.isdigit():
            print("Invalid guess: you should enter a number")
            continue
        user_guess = int(user_guess)
        # user_guess = 23 / "23"
        # verify the guess
        is_guessed_corrected = check_guess(guess=user_guess, target=rand_target) #either true or False
        # if guess is correct -> break out of the loop
        if is_guessed_corrected:
            break
    # inside: ask for input/the Guess,
        # verify the guess (if)
