def check_guess(guess, target):
    if guess < target:
        print(" Your guess is too small")
        return False
    elif guess > target:
        print("You guess is too large")
        return False
    else:
        print("Your guess is correct")
        return True

# variable = 5
# is_correct = check_guess(5,7)
# assigment = return something
# yunsuanfu == !=
