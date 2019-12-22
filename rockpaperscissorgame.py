import random

# CREATED 12.21.19
hands = ["rock", "paper", "scissors"]
choices = int(0)
tries = int(3)
player_points = int(0)
computer_points = int(0)
# goes up to five rounds for player
while player_points != 5:
    computer_choice = random.choice(hands)
    player_choice = input("Please choose rock, paper, or scissors").lower().strip()
    if player_choice == computer_choice:  # computer and player choice are same
        print("Try again, you guys got the same thing!\n")
    elif player_choice == "rock":  # player chooses rock.
        if computer_choice == "scissors":
            player_points += 1
            print(player_choice, "beats: ", computer_choice, ". You won this round.\n")
        else:  # computer chose paper
            computer_points += 1
            print("Computer chose: ", computer_choice, "Better luck next time.\n")
    elif player_choice == "paper":  # player chooses paper
        if computer_choice == "rock":
            computer_points += 1
            print("Computer chose: ", computer_choice, "Better luck next time!\n")
        else:  # computer chose scissors
            player_points += 1
            print(player_choice, "beats: ", computer_choice, "You won this round.\n")
    elif player_choice == "scissors":  # player chooses scissors
        if computer_choice == "rock":
            print("Computer chose:", computer_choice, ". Better luck next time!\n")
        else:  # computer chose paper, you chose scissors:
            player_points += 1
            print(player_choice, "beats", computer_choice, "You won this round.\n")
    else:  # player chooses something that is not paper, scissors, or rock
        print("Please choose rock, paper, scissors.\n")

print("Congratulations, you've won a total of: ", player_points, "rounds")
print("The computer has won: ", computer_points, "rounds")
