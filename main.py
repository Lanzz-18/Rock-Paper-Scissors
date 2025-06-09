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
    return array[int(input("Select item: "))-1]

# Displaying and updating scores
def ScoreManager(score, user, computer):
    # Updating score and returning
    score += scoreKeeper[user][options.index(computer)]
    print(f'Score: {score}')
    return score

# Making the array and score
options = ["Rock", "Paper", "Scissors"]
score = 0

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
    score = ScoreManager(score, userChoice, computerChoice)
    endGame = True if input("Do you want to continue?") == "no" else False