import random


def game():
    number = random.randint(0,100)
    counter = 0
    while True:
        choice = int(input("WHAT IS YOUR GUESS ?"))
        if number > choice:
            print("Pick HIGHER number")
            counter+=1
        elif number < choice:
            print("Pick LOWER number")
            counter+=1
        else:
            counter+=1
            print(f"YOUR {counter}'TH CHOICES IS CORRECT")
            print("YOU WIN THE GAME")
            break


print("System is picking the number between 0 and 100")
print("PICKED")
print("LETS START")
game()


