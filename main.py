import random

user_score = 0
computer_score = 0

while True:
    user_action = input("\nEnter choice (rock, paper, scissors): ").lower()
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nThe computer chose {computer_action}!")

    if user_action == computer_action:
        user_score = user_score + 0
        computer_score = computer_score + 0
        print("You both chose the same!")
    elif user_action == "rock":
        if computer_action == "scissors":
            user_score = user_score + 1
            print("Rock smashes scissors, you win!")
        else:
            computer_score = computer_score + 1
            print("Paper covers rock, you lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            user_score = user_score + 1
            print("Paper covers rock, you win!")
        else:
            print("Scissors cuts paper, you lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            user_score = user_score + 1
            print("Scissors cuts paper, you win!")
        else:
            computer_score = computer_score + 1
            print("Rock smashes scissors, you lose.")

    print('\nScore: ', user_score, ':', computer_score)

    if user_score == 3:
        print("\nUser wins!")
        break
    if computer_score == 3:
        print("\nComputer wins!")
        break