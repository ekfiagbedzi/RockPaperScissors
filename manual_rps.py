import random

OPTIONS_WORDS = ["Nothing", "Rock", "Paper", "Scissors"]
OPTIONS_NUMBERS = list(range(4))
OPTIONS_DICT = dict(zip(OPTIONS_WORDS, OPTIONS_NUMBERS))

def get_computer_choice():
    computer_choice = random.choice(OPTIONS_NUMBERS)
    return(computer_choice)

def get_user_choice():
    user_choice = input("Please enter you choice; one of Rock, Paper or Scisssors:\n")
    return(user_choice)



def get_winner(user_choice, computer_choice):
    if OPTIONS_DICT[user_choice] > computer_choice:
        print("Congratulations!!! You Won!!!")

    elif OPTIONS_DICT[user_choice] < computer_choice:
        print("Sorry, You lost the game!")

    else:
        print("It is a draw game!")


def play():
    get_winner(get_user_choice(), get_computer_choice())

play()