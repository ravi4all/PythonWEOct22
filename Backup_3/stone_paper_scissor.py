import random

choices = ["stone", "paper", "scissor"]

while True:
    user_choice = input("Enter your choice : ")
    cpu = random.choice(choices)
    print(f"Your Move : {user_choice}, CPU Move : {cpu}")
    if cpu == user_choice:
        print("Match Tie...")
    elif cpu == "stone" and user_choice == "paper":
        print("User Win...")
    elif cpu == "paper" and user_choice == "scissor":
        print("User Win...")
    elif cpu == "scissor" and user_choice == "stone":
        print("User Win...")
    elif cpu == "stone" and user_choice == "scissor":
        print("CPU Win...")
    elif cpu == "scissor" and user_choice == "paper":
        print("CPU Win...")
    elif cpu == "paper" and user_choice == "stone":
        print("CPU Win...")
    else:
        print("Invalid Choice...")

