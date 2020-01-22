import tkinter as tk
#from tkinter import *
#import random
#from datetime import datetime

import time
import tkinter
from tkinter import *
import random

LARGE_FONT = ("Verdana", 18)


#------------------------------------------------------------------------------------------

"""  colors  for   later   use"""

c1 = '#263238'
c2 = '#000000'
c3 = '#FFFFFF'
c6 = '#577e75'

c4 = '#faa21f'
c5 = '#577e75'

c7 = '#1e282d'
c8 = '#faa21f'

# Alternative Chat Colours
'''
c4 = '#4790f9'
c5 = '#00a3cf'

c7 = '#85c0f6'
c8 = '#83e7f2'
'''

#-------------------------------------------------------------------------------------------


colours = ['Red','Blue','Green','Black',
           'Orange','Purple','Brown']
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'hey']
question = ['how are you?', 'how are you doing?']
responses = ['Okay', "I'm fine"]
huh = "I did not understand what you said"

# ------------------------------------------------------------------------------------------------------------------

"""

moving from one page to another
    by help of button

"""


def welcome_to_info():
    frame_welcome.pack_forget()
    frame_chat.pack()
    introText()


def welcome_to_chat():
    frame_chat.pack_forget()
    frame_welcome.pack()

# -----------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------


root = Tk ()


#----------------------------------------------------------------------------------------------------

"""  images used in window  """

back = PhotoImage(file = 'icon/arrow_behind.PNG')

front = PhotoImage(file = 'icon/arrow_ahead.PNG')

exitt = PhotoImage(file = 'icon/exit.PNG')

screen_1 = PhotoImage(file = 'icon/image_5.PNG')

submit_img = PhotoImage(file = 'icon/image_8.PNG')

#---------------------------------------------------------------------------------------------------------------------


"""     WELCOME FRAME    """
"""    first frame containing time date and welcome messages """

frame_welcome = Frame(root, bg="#3A39FE", height='670', width='550')
frame_welcome.pack_propagate(0)
frame_welcome.pack()

welcome = Label(frame_welcome, text='Welcome', font="Vardana 40 bold", bg="#3A39FE", fg="white")
welcome.place(x=160, y=200)

welcome_chatbot = Label(frame_welcome, text='I am Chatbot ! ', font="Helvetica 15 bold italic", bg=c1, fg=c6)
welcome_chatbot.place(x=200, y=270)

pic_1 = Label(frame_welcome, image=screen_1)
pic_1.place(x=-2, y=357)

button_front = Button(frame_welcome, image=front, relief="flat", bg="white", fg="#000000", bd="3px solid black",command=welcome_to_info).place(x=470, y=10)

# __________________________________________________________________

"""  time option  """


def clock():
    current = time.strftime("%H:%M:%S")
    label_time = Label(frame_welcome, bd=5, text=current, height=1, width=8, font='Ariel 11 bold', fg="#000000",
                       relief='groove', bg=c3)
    label_time.place(x=120, y=63)

    label_time.after(1000, clock)


button_time = Button(frame_welcome, text='Time', height=1, font='Vardana 10 bold', width=8, bg="white", fg="#000000", command=clock)
button_time.place(x=30, y=63)

# _____________________________________________________________________________

"""    date option   """


def date():
    try:
        date = time.strftime("%d %B , 20%y")
        label_date = Label(frame_welcome, bd=5, relief='groove', text=date, bg=c3, fg="#000000", height=1,
                           font='Ariel 11 bold')
        label_date.place(x=400, y=63)

        label_date.after(86400000, date)

    except AttributeError:
        print('')


button_date = Button(frame_welcome, text='Date', height=1, font='Vardana 10 bold', width=8, bg="white", fg="#000000", command=date)
button_date.place(x=310, y=63)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def submit():
    """
function for producing response of
        request of user

    """
    button_write.place_forget()
    global chat_raw
    chat_raw = entry.get('1.0', 'end-1c')
    entry.delete('1.0', END)
    chat = chat_raw.lower()

    global label_request
    label_request = Label(frame_chats, text=chat_raw, bg=c4, fg=c7, justify=LEFT, wraplength=300,
                          font='Verdana 10 bold')

    label_request.pack(anchor='w')

    global answer


    if chat in greetings:
        answer = random.choice(greetings)


    elif chat in question:
        answer = random.choice(responses)

    else:
        answer = huh
        button_write.place(x=430, y=3)

    get_response()
    pass



def get_response() :

    global label_response
    label_response = Label(frame_chats ,text= answer ,bg="white", fg="#000000", justify = LEFT , wraplength = 300, font = 'Verdana 10 bold')

    label_response.pack(anchor = 'e')

    if answer ==  'Bye':
        root.destroy()

def introText():
    num = random.randrange(0, 3)
    randcolor = random.randrange(0, 7)
    sentences = ("Why not try saying hello?", "Ask me a question!", "Don't be nervous, say something!")
    global answer
    answer=sentences[num]
    get_response()


def refresh_screen () :

    for widget in frame_chats.winfo_children():
        widget.destroy()

    button_write.place_forget()
    label_space = Label (frame_chats , bg = c1 ,  text = '')
    label_space.pack()

def send_mail():
    pass

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""         CHAT FRAME   """
""""       main chat screen   """

frame_chat = Frame(root, bg="white", height='670', width='550')
frame_chat.pack_propagate(0)

frame_top = Frame(frame_chat, bg="#3A39FE", height='100', width='550')
frame_top.pack()

label_topic = Label(frame_top, bg="#3A39FE", fg='white', font='Verdana 20 bold ')
label_topic.pack(pady='40')

frame_spacer = Frame(frame_top, bg=c2, height="10", width="550")
frame_spacer.pack()

bottom_frame = Frame(frame_chat, bg="#3A39FE", height='100', width='550')
bottom_frame.pack_propagate(0)
bottom_frame.pack(side=BOTTOM)

button = Button(bottom_frame, image=submit_img, relief="flat", font='Vardana 10 bold', bg="#2221DE", command=submit)
button.place(x=410, y=27)

entry = Text(bottom_frame, bg="white", fg="#000000", height='5', width='45', font='Verdana 10')
entry.bind('<Return>', submit)
entry.place(x=30, y=10)

frame_chats = Frame(frame_chat, bg="#FFFFFF", height='450', width='500')
frame_chats.pack_propagate(0)
frame_chats.pack()

label_space = Label(frame_chats, bg="#000000").pack()


button_write = Button(bottom_frame, text='write', bg=c3, fg=c2, font='Vardana 8', command=send_mail)

button_back = Button(frame_chat, image=back, relief="flat", bg=c3, command=welcome_to_chat).place(x=10, y=10)
button_front = Button(frame_chat, image=exitt, relief="flat", bg=c3, command=root.destroy).place(x=440, y=10)

# -----------------------------------------------------------------------------------------------------------


root.title("Chatbot")
root.mainloop ()