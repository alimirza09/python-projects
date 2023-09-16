import random
options = (1 , 2 , 3 , 4 , 5 , 6)
comp = random.choice(options)
user = int(input("enter your choice or type help to get a tutorial: "))
if user == "help":
    print("In this game you shall choose a number from 1-6 if your number and computer's number matches then your score won't count and it will start the computer turn to score. if the numbers are not the same you will get score the same as the number you typed in. if the computer scores more than you you lose if you score more than the computer the computer will lose")
user_score = 0
comp_score = 0


while user != comp:
    user_score = user_score + user
    print("your score is = " + str(user_score))
    int(user_score)
    comp = random.choice(options)
    user = int(input("enter your choice or type help to get a tutorial: "))
print(user_score)


if user == comp:
    print("your score has been stopped counting because the computer and your number are equal")
    comp = comp - comp
    while user != comp:
        
        int(comp_score)
        comp = random.choice(options)
        user = int(input("enter your choice or type help to get a tutorial: "))
        comp_score = comp_score + comp
        print("computer's score is = " + str(comp_score))
        comp = random.choice(options)
        user = int(input("enter your choice or type help to get a tutorial: "))
print(comp_score)
if comp_score > user_score:
    print("you lose computer has higher score than you")
elif comp_score < user_score:
    print("you win you have higher score than computer")

    