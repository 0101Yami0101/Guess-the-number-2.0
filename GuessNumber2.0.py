#guess the number game with a Difficulty system
from random import randint
from art import logo

EASY_ATTEMPTS = 5
HARD_ATTEMPTS = 10


def set_diff():   
    userPick = input("Choose difficulty: easy or high \n").lower()
    if userPick == "easy":
        return EASY_ATTEMPTS   
    else:
        return HARD_ATTEMPTS


def check(a_guess,a_answer,turns):
    if a_guess > a_answer:
        print("Too High")
        return turns - 1  #Everytime this function runs turns is lowered by 1
    elif a_guess < a_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it. The answer is {a_answer} ")

#Game function
def game():
    print(logo)
    print("Welcome to the number guessing game")
    print("The number is between 1 and 100")
    answer = randint(1,100)

    #User Chooses difficulty
    turns = set_diff()
    

    #User guesses
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts left")
        guess = int(input("Guess a number"))

        turns = check(guess,answer,turns)
        if turns == 0:
            print(f"Opps you lost! The answer was {answer}")
            return
        elif guess != answer:
            print("Guess again")

game()

