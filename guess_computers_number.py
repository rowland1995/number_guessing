import random

score = 0
while score < 5: #program ends when user score reaches 5
    
    computer_number = random.randint(1,5) #variable for random number
    user_number = input("Guess the computers number between 1-5: ") #takes users guess
    print("The computer picked : " + str(computer_number))
    
    
    if int(user_number) > 5:
        print("Your guess is too high")
        
    if int(user_number) < 0:
        print("Your guess is too low")

    if int(user_number) == computer_number:
        print("You picked correct!")
        score = score + 1
        if score == 5:
            print("YOU WIN")
        print("Your score = " + (str(score)))
    else:
        print("You chose wrong. Try again.")


