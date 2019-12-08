import tkinter
from tkinter import *
import random
import time
from time import sleep

colours = ['Red','Blue','Green','Black', 
           'Orange','Purple','Brown'] 
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'hey']
question = ['How are you?', 'How are you doing?']
responses = ['Okay', "I'm fine"]
huh = "I did not understand what you said"

#class Window(Frame):
#    def __init__(self, master=None):
#        Frame.__init__(self, master)                 
#        self.master = master
#        self.init_window()
#
#    def init_window(self):
#        self.master.title("Chatbot")
#        self.pack(fill=BOTH, expand=1)
#        menu = Menu(self.master)
#        self.master.config(menu=menu)
#        file = Menu(menu)
#        file.add_command(label="Quit", command=self.client_exit)
#        menu.add_cascade(label="Home", menu=file)
#
#        self.introText()
#
#    def introText(self):
#        num = random.randrange(0,3)
#       randcolor = random.randrange(0, 7)
#        sentences = ("Why not try saying hello?", "Ask me a question!", "Don't be nervous, say something!")
#        text = Label(self, text=(sentences[num]))
#        text.config(fg = str(colours[randcolor]))
#        text.pack()
#
#    def client_exit(self):
#        exit()

root = tkinter.Tk()
root.geometry("600x600")

#app = Window(root)

def B_and_U(event):
  userOutputFunc()
  botOutput()


def userOutputFunc():
  userText = userInput.get()
  userOutput = Label(root, text=userText)
  userOutput.pack(side=TOP, fill=X, anchor='e')
  root.update()

def botOutput():
    userText = userInput.get()
    if userText in greetings:
      botText = random.choice(greetings)
    elif userText in question:
      botText = random.choice(responses)
    else:
      botText = huh
    output = tkinter.Label(root, text='')
    output.pack(side=TOP, fill=X, anchor='w')
    output.after(1000, output.config(text=botText))

userInput = tkinter.Entry(root)

userInput.place(x=300, y=550, anchor='center')
userInput.focus_set()

userInput.bind("<Return>", B_and_U)

root.mainloop()  