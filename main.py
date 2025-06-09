# add error handling

import random

# Creating function to choose item randomly
def PCSelectOption(array):
    selectedOption = random.choice(array)
    return selectedOption

# Function for user to select item
def UserSelectOption(array):
    count = 1
    while True:
        try:
            for item in array:
                print(f'{count}. {item}')
                count += 1
            choice = int(input("Select item: "))
            if(1 <= choice <= 3):
                return array[choice-1]
            else:
                raise ValueError("Enter between 1-3")
        except ValueError as e:
            print(e)

# Displaying and updating scores
def ScoreManager(user, computer):
    global userScore, computerScore
    # Updating score and returning
    userScore += scoreKeeper[user][options.index(computer)]
    computerScore += scoreKeeper[computer][options.index(user)]
    print(f'Your Score: {userScore}\nComputer Score: {computerScore}')

# Making the array and score
options = ["Rock", "Paper", "Scissors"]
userScore = 0
computerScore = 0

# Order of items = Rock, Paper, Scissors
scoreKeeper = {"Rock" : [0, 0, 1],
            "Paper": [1, 0, 0],
            "Scissors": [0, 1, 0]}

endGame = False
while(not endGame):
    # Choices
    userChoice = UserSelectOption(options)
    computerChoice = PCSelectOption(options)
    print(f'Your choice: {userChoice}\nComputer Choice: {computerChoice}')
    ScoreManager(userChoice, computerChoice)
    while True:
        endGame = input("Do you want to continue(y/n)? ")
        if(endGame == "y"):
            endGame = False
            break
        elif(endGame == "n"):
            print("Thank you for playing\nHave a nice day :)")
            endGame = True
            break
        else:
            print("Invalid input")