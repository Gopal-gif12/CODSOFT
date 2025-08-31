import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

# Main game loop
print(" Welcome to Rock-Paper-Scissors Game ")

user_score = 0
computer_score = 0

while True:
    print("\nPlease choose: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print(" Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer_choice = get_computer_choice()
    print(f" You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "tie":
        print(" It's a tie!")
    elif result == "user":
        print(" You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"\n Score -> You: {user_score} | Computer: {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\n Thanks for playing! Final Score -> You:", user_score, "| Computer:", computer_score)
        break
