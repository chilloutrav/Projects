print("Welcome to 'This Special Quiz' game")

permission = input("Do you wanna play or that was a mistake opening the game?(if yes type 'yes') ")
print("To be clear about the rules, if you got a question correct you get +1 point and if you got the question wrong you will get a -1 point")
print('Your score will be displayed in the end of the quiz')

score = 0

if permission.lower() != "yes":
    quit()
answer = input("What does the main part of a computer? : ")

if answer.lower() == "cpu":
    print("correct")
    score += 1
else:
    print("Sorry that was incorrect maybe next time")
    score -= 1
print("your score was", score)
#for more questions just copy past the answer part to end of else statement

    

