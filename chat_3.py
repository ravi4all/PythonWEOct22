from datetime import datetime as dt
import os, glob, random
import json
import urllib.request as url

chat = True

greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
dateIntent = ["tell me date", "date", "date please", "what's the date"]
timeIntent = ["tell me time", "time", "time please", "what's the time"]
musicIntent = ["play song", "play music", "start song"]
newsIntent = ["news", "tell me news", "please tell me news"]

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
    elif msg in musicIntent:
        path = r"D:\Batches\Songs\new_songs"
        # chdir - change directory
        os.chdir(path)
        # fetch all mp3 files
        songs = glob.glob("*.mp3")
        # select random song
        song = random.choice(songs)
        # play song
        os.startfile(song)
    elif msg in newsIntent:
        print("Here are top headlines...")
        path = "https://newsapi.org/v2/top-headlines?country=in&apiKey=695e07af402f4b119f0703e9b19f4683"
        response = url.urlopen(path)

        data = json.load(response)
        articles = data["articles"]

        for i in range(len(articles)):
            print(articles[i]['title'])
            print("*" * 50)

        print("""
        1. Sports
        2. Entertainment
        3. Business
        4. Health
        5. Tech
        6. Science
        """)
        choice = input("Which News Category you want : ")

    elif msg == "bye":
        print("Bye User")
        break
    else:
        print("I don't understand")

