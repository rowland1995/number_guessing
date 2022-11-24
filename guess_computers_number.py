import random

score = 0
while True:
    
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
        print(score)
    else:
        print("You chose wrong. Try again.")


