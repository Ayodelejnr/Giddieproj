import random

while True:

    print("Rock Paper Scissor \n"
        "RULES OF THE GAME \n"
        "Paper vs Scissors = Scisors wins \n"
        "Rock vs Scissors = Rock wins \n"
        "Rock vs Paper = Paper wins \n"
        "START GAME!!!")

    player_choice = input("Enter your choice: R for Rock, \n P for Paper \n S for Scissors \n")
    print("You selected %s" %player_choice)
    choices=["R", "P", "S"]
    computer_choice = random.choice(choices)
    print("Computer's choice is %s" %computer_choice)
    print("*****checking*****")

    if player_choice == computer_choice:
        print("it's a tie")
        keep_playing = input("Would you like to play again? 'y' for Yes 'n' for No")
        if keep_playing.lower() != "y":
            break
        elif player_choice == "s":
            if computer_choice == "p":
                print("Scissors cuts paper, you win!")
            else:
                print("Rock smashes scissors, you loose!")

        elif player_choice =="R":
            if computer_choice == "s":
                print("Rock smashes scissors, you win!")
            else:
                print("Paper covers rock, you loose!")
        elif player_choice == "p":
            if computer_choice == "r":
                print("Paper cover's rock, you win!")
            else:
                print("Scissors cuts paper, you loose!")
        
        continue_game = input("Would you like to play again? 'y' for Yes 'n' for No \n")
        if continue_game.lower() != "y":
            break