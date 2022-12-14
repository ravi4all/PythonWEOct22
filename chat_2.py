from datetime import datetime as dt

chat = True

greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
dateIntent = ["tell me date", "date", "date please", "what's the date"]
timeIntent = ["tell me time", "time", "time please", "what's the time"]

#Logical Operator - and, or, not
#Membership Operator - in, not in
#Identity Operator - is, is not
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg in greetIntent:
        print("Hello User")
    elif msg in dateIntent:
        d = dt.now().date()
        print(d.strftime("%d %B, %Y, %A"))
    elif msg in timeIntent:
        t = dt.now().time()
        print(t.strftime("%H:%M:%S,%p"))
    elif msg == "bye":
        print("Bye User")
        break
    else:
        print("I don't understand")

