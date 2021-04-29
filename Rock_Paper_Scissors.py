import random

user_action = input("Enter a choice (rock, paper, scissors): ")
print("Press q to quit.")

#prompts the user to input a choice

#make the computer choose

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)


#This allows a random element to be selected from the list. You can also print choices that
#the user and the computer made

print(f"\n You chose {user_action}, computer chose {computer_action}.\n")

#print the user and the computer actions can be helpful, and it can also help you debug later in case
#something isn't quite right with the outcome.

while True:
	if user_action == computer_action:
		print(f"Both players selected {user_action}. It's a tie!")
	elif user_action == "rock":
		if computer_action == "scissors":
			print("Rock smashes scissors! You win!")
		else:
			print("Paper covers rock! You lose!")
	elif user_action == "paper":
		if computer_action == "rock":
			print("Paper covers rock! You Win!")
		else:
			print("Scissors cuts paper! You lose!")
	elif user_action == "scissors":
		if computer_action == "paper":
			print("scissors cuts paper! You win!")
		else:
			print("rock crushes scissors! You lose!")
	elif user_action != possible_actions:
		print("That doesn't work...")

	play_again = input("Play again? (y/n): ")
	if play_again.lower() != "y":
		print("Sore loser...")
		break
