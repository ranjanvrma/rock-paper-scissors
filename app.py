import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def get_result(user_choice, computer_choice):
    if user_choice == computer_choice:
            return "draw"
    if (
        (user_choice == "rock" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "rock")
    ):
        return "lose"
    return "win"

def run_game():
    print("Rock Paper Scissors Game")
    print("Type Your Choice: Rock / Paper / Scissors")
    print("Type Exit to Terminate the Game")

    while True:
        user_choice = input("\nYour Move: ").strip().lower()

        if user_choice == "exit":
            print("Thanks for Playing!")
            break

        if user_choice not in choices:
            print("Invalid Choice! Try Again")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer Chose: {computer_choice}")

        result = get_result(user_choice, computer_choice)

        if result == "draw":
            print("It's a Draw!")
        elif result == "lose":
            print("Better Luck Next Time")
        else:
            print("You Won!")

        again = input("Want to Play Again? (yes/no): ").strip().lower()
        if again == "yes":
            continue
        else:
            print("Thanks for Playing")
            break

if __name__ == "__main__":
    run_game()