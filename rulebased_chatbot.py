from tkinter import *
from tkinter.ttk import *
from openpyxl.chart import label
from nltk.chat.util import Chat, reflections

master = Tk()
master.title("Chatbot")
master.geometry("200x200")


def openNewWindow():
    newWindow = Toplevel(master)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    Label(newWindow,
          text="This is a new window").pack()
    label.pack(pady=10)
    mainloop()


reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"what is your name ?",
        ["I am BOT created to help you!", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good.How about You ?", ]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", ]
    ],
    [
        r"I am fine",
        ["Great to hear that,How can I help you?", ]
    ],
    [
        r"how old are (.*)?",
        ["I'm a computer program you Seriously you are asking me this?", ]
    ],
    [
        r"what do you (.*)?",
        ["Make me an offer I can't refuse", ]
    ],
    [
        r"(.*) created you ?",
        ["PC951 created me using Python's NLTK library ", "top secret ;)", ]
    ],
    [
        r"What is (.*) (location|city) ?",
        ['I am from Texas', ]
    ],
    [
        r"how is the weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot here in %1", "Too cold here in %1",
         "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. Their stock prices are going up.", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2", "Damn its raining too much here in %2"]
    ],
    [
        r"how is (.*) health?",
        ["I'm a computer program, so I'm always healthy", ]
    ],
    [
        r"what is your (.*) (sports|game) ?",
        ["I'm a very big fan of Football", ]
    ],
    [
        r"who is (.*) favourite sportsman ?",
        ["Messy", "Ronaldo", ]
    ],
    [
        r"who is (.*) favourite (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Google has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"bye, thank you!",
        ["BBye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
]


def chat():
    print("Hi! I am a chatbot")
    chats = Chat(pairs, reflections)
    chats.converse()


if __name__ == "__main__":
    chat()
