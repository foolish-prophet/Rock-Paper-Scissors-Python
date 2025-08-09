import random

player_options = ['rock', 'paper', 'scissors']
win_lose = ['win', 'lose', 'tie']
player_1_choice = input("Enter rock, paper, or scissors: ")
player_1_choice = player_1_choice.lower()
computer_choice = player_options[random.randint(0, 2)]
#3 unnecessary active = True

## unnecessary while active:
if player_1_choice not in player_options:
    print("Invalid choice")
    
else:
    if player_1_choice == "paper" and computer_choice == "rock":
        win_lose = win_lose[0]
        print(f"The computer got: {computer_choice}")
        print(win_lose)
        
    elif player_1_choice == "paper" and computer_choice == "scissors":
        win_lose = win_lose[1]
        print(f"The computer got: {computer_choice}")
        print(win_lose)

    elif player_1_choice == "scissors" and computer_choice == "paper":
        win_lose = win_lose[0]
        print(f"The computer got: {computer_choice}")
        print(win_lose)

    elif player_1_choice == "scissors" and computer_choice == "rock":
        win_lose = win_lose[1]
        print(f"The computer got: {computer_choice}")
        print(win_lose)

    elif player_1_choice == "rock" and computer_choice == "scissors":
        win_lose = win_lose[0]
        print(f"The computer got: {computer_choice}")
        print(win_lose)

    elif player_1_choice == "scissors" and computer_choice == "paper":
         win_lose = win_lose[1]
         print(f"The computer got: {computer_choice}")
         print(win_lose)

    elif player_1_choice == "scissors" and computer_choice == "scissors":
         win_lose = win_lose[2]
         print(f"The computer got: {computer_choice}")
         print(win_lose)

    elif player_1_choice == "paper" and computer_choice == "paper":
        win_lose = win_lose[2]
        print(f"The computer got: {computer_choice}")
        print(win_lose)  

    elif player_1_choice == "rock" and computer_choice == "rock":
        win_lose = win_lose[2]
        print(f"The computer got: {computer_choice}")
        print(win_lose)
            