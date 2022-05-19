import random

def game():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'no winner'
    if win(user,computer):
        return 'You win'
    else:
        return 'You lost'

def win(player, computer):
    if (player == "r" and computer =="s") or (player == "s" and computer == "p") or (player == "p" and computer == "r"):
        return True


print(game())
