import random

print("Rock Paper Scissors Game")
print("Type Your Choice: Rock / Paper / Scissors")
print("Type Exit to Terminate the Game")

choices = ["rock", "paper", "scissors"]
while True:
    user_choice = input("\nYour Move: ").lower()

    if user_choice == "exit":
        print("Thanks for Playing!")
        break

    if user_choice not in choices:
        print("Invalid Choice! Try Again")
        continue

    computer_choice = random.choice(choices)

    print(f"Computer Chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Draw!")
    elif (
        (user_choice == "rock" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "rock")
    ):
        print("Better Luck Next Time!")
    else:
        print("You Won!")

    again = input("Want to Play Again? (yes / no): ").lower()
    if again == "yes":
        continue
    else:
        print("Thanks for Playing!")
        break
