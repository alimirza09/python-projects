from PIL import Image
import random
options = ("rock" , "scisscors" , "paper")
bot = random.choice(options)
user0 = input("do you want to stop y/n: ")
while user0 == "n":#loop
    user = input("enter your choice: ")
    if bot == "rock" and user == "paper":
        print("you won bot used rock")
        
    elif bot == "scissors" and user == "rock":
        print("you won bot used " + bot)
        
    elif bot == "paper" and user == "scissors":
        print("you won bot used " + bot)
        
    elif bot == "rock" and user == "scissors":
        print("you lost bot used " + bot)
        
    elif bot == "scissors" and user == "paper":
        print("you lost bot used " + bot)
        
    elif bot == "paper" and user == "rock":
        print("you lost bot used " + bot)
    elif bot == user:
        print("it is a tie")    
    if user not in options:
        print("invalid input")
    user0 = input("do you want to stop y/n: ")
