import random

player_options = ['rock', 'paper', 'scissors']
win_lose = ['win', 'lose', 'tie']
max_rounds = 5
round_number = 1

while round_number <= 5:
    
    player_1_choice = input("Enter rock, paper, or scissors: ")
    player_1_choice = player_1_choice.lower()
    computer_choice = player_options[random.randint(0, 2)]

    if player_1_choice == 'quit':
        print("game exited...")
        break

    if player_1_choice not in player_options:
        print("Invalid choice")
        continue

    if player_1_choice == "paper" and computer_choice == "rock":
        result = win_lose[0]
        print(f"The computer got: {computer_choice}")
        print(result)
        
    elif player_1_choice == "paper" and computer_choice == "scissors":
        result = win_lose[1]
        print(f"The computer got: {computer_choice}")
        print(result)

    elif player_1_choice == "scissors" and computer_choice == "paper":
        result = win_lose[0]
        print(f"The computer got: {computer_choice}")
        print(result)

    elif player_1_choice == "scissors" and computer_choice == "rock":
        result = win_lose[1]
        print(f"The computer got: {computer_choice}")
        print(result)

    elif player_1_choice == "rock" and computer_choice == "scissors":
        result = win_lose[0]
        print(f"The computer got: {computer_choice}")
        print(result)

    elif player_1_choice == "scissors" and computer_choice == "paper":
        result = win_lose[1]
        print(f"The computer got: {computer_choice}")
        print(result)

    elif player_1_choice == "scissors" and computer_choice == "scissors":
        result = win_lose[2]
        print(f"The computer got: {computer_choice}")
        print(result)

    elif player_1_choice == "paper" and computer_choice == "paper":
        result = win_lose[2]
        print(f"The computer got: {computer_choice}")
        print(result)  

    elif player_1_choice == "rock" and computer_choice == "rock":
        result = win_lose[2]
        print(f"The computer got: {computer_choice}")
        print(result)
            
    round_number += 1