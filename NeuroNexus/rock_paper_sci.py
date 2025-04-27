import random

options = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

print("----Welcome to Rock-Paper-Scissors!----")
print("First to 3 points wins the game!")
print("Choices: 1. Rock  2. Paper  3. Scissors")

round_no = 1

while user_score < 3 and computer_score < 3:
    print(f"\n--- Round {round_no} ---")
    user_choice = int(input("Enter your choice (1-3): "))

    if user_choice not in [1, 2, 3]:
        print("Invalid choice. You lose this round!")
        computer_score += 1
        round_no += 1
        continue

    user_pick = options[user_choice - 1]
    computer_pick = random.choice(options)

    print(f"You chose: {user_pick}")
    print(f"Computer chose: {computer_pick}")

    if user_pick == computer_pick:
        print("It's a tie! No points awarded.")
    elif (user_pick == "Rock" and computer_pick == "Scissors") or \
         (user_pick == "Paper" and computer_pick == "Rock") or \
         (user_pick == "Scissors" and computer_pick == "Paper"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Current Score ➔ You: {user_score} | Computer: {computer_score}")
    round_no += 1

# Final Winner
print("\n----Final Result----")
if user_score == 3:
    print("Congratulations! You are the WINNER!")
else:
    print("Computer wins! Better luck next time!")
