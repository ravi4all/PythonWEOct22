import streamlit as st
from datetime import datetime as dt
import os, glob, random

chat = True

greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
dateIntent = ["tell me date", "date", "date please", "what's the date"]
timeIntent = ["tell me time", "time", "time please", "what's the time"]
musicIntent = ["play song", "play music", "start song"]

st.title("Chat Application")
st.write("Simple chat application")

form = st.form("chat_form")
msg = form.text_input("Enter your msg")
btn = form.form_submit_button("Submit")

if btn:
    print("Clicked...")

    if msg in greetIntent:
        st.write("Hello User")
    elif msg in dateIntent:
        d = dt.now().date()
        st.write(d.strftime("%d %B, %Y, %A"))
    elif msg in timeIntent:
        t = dt.now().time()
        st.write(t.strftime("%H:%M:%S,%p"))
    elif msg in musicIntent:
        path = r"D:\Batches\Songs\new_songs"
        os.chdir(path)
        songs = glob.glob("*.mp3")
        song = random.choice(songs)
        os.startfile(song)
    elif msg == "bye":
        print("Bye User")
    else:
        print("I don't understand")
