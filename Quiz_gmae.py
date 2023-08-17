# This is a quiz game
computer = input("Do you want to play the game")
if computer.lower() == "yes":
    print("Let's play the game")

else:
    print("Let me know if you change your mind")


score = 0
answer = input("What does CPU stands for ?")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1

else:
    print("Incorrect")
    score -= 1


answer = input("What does RAM stand for ? ")
if answer.lower() == "random access memory":
        print("Correct")
        score += 1


else:
        print("Incorrect")
        score -= 1



answer = input("What does ROM stand for ? ")
if answer.lower() == "read only memory":
        print("Correct")
        score += 1


else:
        print("Incorrect")
        score -= 1

print("Your total score is : " , score)
