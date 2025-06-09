# fix the choices gettting duplicate bug
# add error handling

import random

# Creating function to choose item randomly
def PCSelectOption(array):
    selectedOption = random.choice(array)
    return selectedOption

# Function for user to select item
def UserSelectOption(array):
    count = 1
    for item in array:
        print(f'{count}. {item}')
        count += 1
    return array[(int(input("Select item: ")))-1]

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
    endGame = True if input("Do you want to continue?") == "no" else False