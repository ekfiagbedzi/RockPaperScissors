import random

OPTIONS_WORDS = ["Nothing", "Rock", "Paper", "Scissors"]
OPTIONS_NUMBERS = list(range(4))
OPTIONS_DICT = dict(zip(OPTIONS_WORDS, OPTIONS_NUMBERS))

def get_computer_choice():
    computer_choice = random.choice(OPTIONS_NUMBERS)
    return(computer_choice)

def get_user_choice():
    user_choice = OPTIONS_DICT[input("Please enter you choice; one of Rock, Paper or Scisssors:\n")]
    return(user_choice)



def get_winner(user_choice, computer_choice):
    if user_choice > computer_choice:
        return("Congratulations!!! You Won!!!")

    elif user_choice < computer_choice:
        return("Sorry, You lost the game!")

    else:
        return("It is a draw game!")


def play():
    print(get_winner(get_user_choice(), get_computer_choice()))