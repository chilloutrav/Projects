name = input("Type your name")

print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? "
).lower
if answer == "left":
    answer = input("You came to a river, you can walk around it or swin accross? Type walk to walk accross and type swim to swin accross: ").lower
    if answer == "swim":
        print("You swam accross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked accross for many miles, ran out of water and you lost the game.")
    else:
         print("Not a valid answer. You lose.")


elif answer == "right":
    print("You come to a bridge, it looks wobbly, do you want to cross it?U(yes/no)")
else:
    print("Not a valid answer. You lose.")
