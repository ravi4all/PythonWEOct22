import random

# first of all CPU will think a random number
cpu = random.randint(1,100)
counter = 5
game = True
#while counter != 0:
while game:
    # here we are taking user's input
    user = int(input("Enter your guess : "))
    if cpu == user:
        print("Congrats, You have guessed the number...")
        game = False
        break
    elif cpu > user:
        print("You have guessed smaller number...")
    elif cpu < user:
        print("You have guessed greater number...")
    counter -= 1
    print("Chances Left :",counter)
    if counter == 0:
        print("You Lose, Number was",cpu)
        break
