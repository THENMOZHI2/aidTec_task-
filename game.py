import random 
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
def check_answer(guess,number,attempts):
    if guess<number:
        print("Your guess is too low")
        return attempts-1
    elif guess>number:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"Your guess is right...The answer was {number}")
def game():
    print("let me think of a number between 1 to 100.")
    number=random.randint(1,100)
    level=input("choose level of difficulty...Type 'easy' or 'hard':")
    attempts=set_difficulty(level)
    guess=0
    while guess!=number:
        print(f"You have {attempts} remaining to guess the number.")
        guess=int(input("Guess a number:"))
        attempts=check_answer(guess,number,attempts)
        if attempts==0:
            print("You are out of guesses... You lose!")
            return 
        elif guess!=number:
            print("Guess again")
game()