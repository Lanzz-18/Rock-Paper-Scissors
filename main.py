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
    return input("Select item: ")

# Displaying and updating scores
def ScoreManager(score, user, computer):
    user = user.lower()
    computer = computer.lower()
    print(f'Score: {score}')
    # Setting index for user
    if user == "rock":
        index_1 = 0
    elif user == "paper":
        index_1 = 1
    else:
        index_1 = 2
        
    # Setting index for computer
    if computer == "rock":
        index_2 = 0
    elif computer == "paper":
        index_2 = 1
    else:
        index_2 = 2

    score += scoreKeeper[index_1][index_2]

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
    computerChoice = PCSelectOption(options)
    userChoice = UserSelectOption(options)
    ScoreManager(score, userChoice, computerChoice)
    endGame = True if input("Do you want to continue?") == "Yes" else False