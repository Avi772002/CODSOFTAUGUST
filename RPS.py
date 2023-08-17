import random

choices = ('rock' , 'paper' , 'scissor')
userInput = input("Enter your choice (rock , paper , scissor) : ")
computerInput = random.choice(choices)

print(f"userInput:{userInput}")
print(f"computerInput:{computerInput}")

while userInput not in choices:
    userInput = input("Enter your choice (rock , paper , scissor) : ")

if userInput == computerInput:
    print("The match draws! ")


elif userInput == 'rock' and computerInput == 'paper':
    print("Computer won the match :)")

elif userInput == 'paper' and computerInput == 'rock':
    print("You won the match :)")

elif userInput == 'rock' and computerInput == 'scissor':
    print("You won the match :)")

elif userInput == 'scissor' and computerInput == 'rock':
    print("Computer won the match :)")

elif userInput == 'paper' and computerInput == 'scissor':
    print("Computer won the match :)")

elif userInput == 'scissor' and computerInput == 'paper':
    print("You won the match :)")