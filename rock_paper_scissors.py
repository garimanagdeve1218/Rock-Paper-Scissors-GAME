import random

user_wins = 0                 #as we need two variables one for the user's score and one for the computer's score
computer_wins = 0

options = ["rock","paper","scissors"]

#we will use a while loop to ask the user to enter rock,paper or scissors and also let them enter Q and if they do that means imedietely quit the programme.

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower() #we will take whatever the user types in and just convert it to the lower.
    if user_input == "q":     #we wrote small q as the input will be converted to the lower.
        break                #this means if this condition is true break out of the while loop or end the loop right away.

    if user_input not in options:      #to check if the user's input is not in rock,paper or scissors
        continue                                           #if this condition is true the continue means it will again ask the user the input we could have also used something printing like invalid or something like that.

    random_number = random.randint(0,2)  #rock: 0, paper: 1, scissors:2
    computer_pick = options[random_number]     #random_number , we will use that as the index to actually access the string that the computer chose i.e. rock, papper or scissors.
    print("Computer picked: ", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The Computer won", computer_wins, "times.")
print("GoodBye!")


