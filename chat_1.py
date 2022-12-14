chat = True

while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg == "hello" or msg == "hi" or msg == "hey":
        print("Hello User")
    elif msg == "bye":
        print("Bye User")
        break
    else:
        print("I don't understand")

