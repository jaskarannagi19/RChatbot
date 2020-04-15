<<<<<<< HEAD
#!/usr/local/bin/python3
import time, conversation, tkinter as tk
import random, datetime, json, tkinter
from PIL import  ImageTk
import PIL.Image
from tkinter import *

=======
import tkinter as tk
import time
import tkinter
from tkinter import *
import random
import datetime
from PIL import Image, ImageTk
import conversation
import smtplib
import json
>>>>>>> 6ce34b134c04869ceee472af2be608bce7b6b12f
LARGE_FONT = ("Verdana", 18)
c1 = '#263238'
c2 = '#000000'
c3 = '#FFFFFF'
c6 = '#577e75'
c4 = '#faa21f'
c5 = '#577e75'
c7 = '#1e282d'
c8 = '#faa21f'

<<<<<<< HEAD

# ------------------------------------------------------------------------------------------------------------------

""" Moving from one page to another by help of button """
=======
# ------------------------------------------------------------------------------------------------------------------

""" Moving from one page to another by help of button """

>>>>>>> 6ce34b134c04869ceee472af2be608bce7b6b12f
# method that will display the main welcome screen upon being called

def welcome_to_info():
    global answer
    frame_welcome.pack_forget()
    frame_chat.pack()
    introText()

# method that will display the main chat screen upon being called
def welcome_to_chat():
    frame_chat.pack_forget()
    frame_welcome.pack()
<<<<<<< HEAD
# --------------------------------------------------------------------------------------------
root = Tk()
#---------------------------------------------------------------------------------------------------------------------
"""     WELCOME FRAME     First frame containing time date and welcome messages """
=======

# --------------------------------------------------------------------------------------------


root = Tk()

#---------------------------------------------------------------------------------------------------------------------


"""     WELCOME FRAME    
        First frame containing time date and welcome messages """

>>>>>>> 6ce34b134c04869ceee472af2be608bce7b6b12f
# Display the frame with a specified background colour and with set dimensions.  
frame_welcome = Frame(root, bg="#3A39FE", height='670', width='550')
# Propagate makes it so the dimensions cannot be set by the children of this object
frame_welcome.pack_propagate(0)
frame_welcome.pack()

# The main welcome label you see when opening the chatbot 
welcome = Label(frame_welcome, text='Welcome', font="Vardana 40 bold", bg="#3A39FE", fg="white")
welcome.place(relx=0.5, rely=0.25, anchor=CENTER)

# The secondary label that appears underneath the welcome label
welcome_chatbot = Label(frame_welcome, text='My name is Monty and I am a chatbot! ', font="Helvetica 15 bold italic", bg=c1, fg=c6)
welcome_chatbot.place(relx=0.5, rely=0.4, anchor=CENTER)

# Places the image of the chatbot at the bottom half of the screen
screen_1 = PIL.Image.open("icon/image_5.png")
screen1Img = ImageTk.PhotoImage(screen_1)
imgScreen1 = Label(frame_welcome, image=screen1Img)
imgScreen1.image = screen1Img
imgScreen1.place(x=-2, y=357)

# The button which will take the user to the chat screen
<<<<<<< HEAD
front = PIL.Image.open("icon/arrow_ahead.png")
frontImg = ImageTk.PhotoImage(front)
button_front = Button(frame_welcome, image=frontImg, relief="flat", bg="white", fg="#000000", bd="3px solid black",command=welcome_to_info).place(x=470, y=10)
back = PIL.Image.open("icon/arrow_behind.png")
backImg = ImageTk.PhotoImage(back)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
global chat_raw
global label_request


=======
front = Image.open("icon/arrow_ahead.png")
frontImg = ImageTk.PhotoImage(front)
button_front = Button(frame_welcome, image=frontImg, relief="flat", bg="white", fg="#000000", bd="3px solid black",command=welcome_to_info).place(x=470, y=10)
back = Image.open("icon/arrow_behind.png")
backImg = ImageTk.PhotoImage(back)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
emailArray = []
>>>>>>> 6ce34b134c04869ceee472af2be608bce7b6b12f
# Function to delete the user input after submit button is clicked
def emptyUserInput():
    entry.delete("1.0", END)

def submit(event):
<<<<<<< HEAD
    """ Function for producing response of Request of user """
    button_write.place_forget()
=======
    """ Function for producing response of
        Request of user """
    button_write.place_forget()
    # Creates a global variable named chat_raw
    global chat_raw
    # The input box is then read from the first line character 0 (the very beginning), while the end-1c tells the reader to stop at the end of the input box,
    # The -1c is because tkinter creates a new line at the end of each entry, which we dont want so we just delete 1 character from the end
    chat_raw = entry.get('1.0', 'end-1c')
    # The following line calls a function after 1/1000 of a second to delete the input. This was done to avoid a minor bug that kept happening
    entry.after(1, emptyUserInput)
    # This changes the user input to all lowercase
    chat = chat_raw.lower()
    emailArray.append(chat)
>>>>>>> 6ce34b134c04869ceee472af2be608bce7b6b12f

    # The input box is then read from the first line character 0 (the very beginning), while the end-1c tells the reader to stop at the end of the input box,
    # The -1c is because tkinter creates a new line at the end of each entry, which we dont want so we just delete 1 character from the end
    userInput = entry.get('1.0', 'end-1c')
    # The following line calls a function after 1/1000 of a second to delete the input. This was done to avoid a minor bug that kept happening
    entry.after(1, emptyUserInput)
    # This changes the user input to all lowercase
    userInput = userInput.lower()

    label_request = Label(scrollable_frame, text=userInput, bg="#00BFFF", fg=c7, justify=LEFT, wraplength=300, font='Verdana 10 bold')
    ts = time.time()
    _time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    time_stamp_bot = Label(scrollable_frame, text=_time, bg="white", fg="#000000", justify=LEFT, wraplength=300, font='Verdana 10 bold')
    time_stamp_user = Label(scrollable_frame, text=_time, bg="#00BFFF", fg="#000000", justify=LEFT, wraplength=300, font='Verdana 10 bold')
    label_request.pack(anchor='e')
    time_stamp_user.pack(anchor='e')

    

    # PASSING THE USER'S INPUT INTO THE CONVERSATION CONTROLLER FOR PROCESSING
    ongoingConversation, answer = conversation.converse(userInput,True)
    # render response to chatbot
    print("------------------------------------------------")
    print(answer)
    # This creates the label for where the user output is going to be stored, it is anchored on the west (left side) and is highlighted so you can clearly see it
<<<<<<< HEAD
    label_response = Label(scrollable_frame ,text= answer ,bg="white", fg="#000000", justify =LEFT , wraplength = 300, font = 'Verdana 10 bold')
    ts = time.time()
    _time=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    time_stamp = Label(scrollable_frame,text= _time ,bg="white", fg="#000000", justify = LEFT, wraplength = 300, font = 'Verdana 10 bold')
    label_response.pack(anchor = 'w')
    time_stamp.pack(anchor='w')
=======
    global label_request
    label_request = Label(scrollable_frame, text=chat_raw, bg="#00BFFF", fg=c7, justify=LEFT, wraplength=300,
                          font='Verdana 10 bold')
    ts = time.time()
    _time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    time_stamp_bot = Label(scrollable_frame, text=_time, bg="white", fg="#000000", justify=LEFT, wraplength=300,
                       font='Verdana 10 bold')
    time_stamp_user = Label(scrollable_frame, text=_time, bg="#00BFFF", fg="#000000", justify=LEFT, wraplength=300,
                       font='Verdana 10 bold')
    label_request.pack(anchor='e')
    time_stamp_user.pack(anchor='e')

    global answer
    if len(chat) != 0:
        answer = conversation.converse(chat)
        emailArray.append(answer)
    else:
        answer = "I can't respond if you don't say anything..."

    button_write.place(x=430, y=3)

    get_response()
    canvas.yview_moveto(1)
    pass

>>>>>>> 6ce34b134c04869ceee472af2be608bce7b6b12f

    

<<<<<<< HEAD


    button_write.place(x=430, y=3)
=======
def get_response() :

    # This code shows the bot reply and also, if the user input is "bye" then the program will end.
    global label_response

    label_response = Label(scrollable_frame ,text= answer ,bg="white", fg="#000000", justify =LEFT , wraplength = 300, font = 'Verdana 10 bold')
    ts = time.time()
    _time=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    time_stamp = Label(scrollable_frame,text= _time ,bg="white", fg="#000000", justify = LEFT, wraplength = 300, font = 'Verdana 10 bold')
    label_response.pack(anchor = 'w')
    time_stamp.pack(anchor='w')


    if answer ==  'Bye':
        root.destroy()

# This is where the bot will instantly type something to get the conversation started
def introText():
    global answer
    answer="Hello, I am Monty. Ask me anything"
    get_response()


# Doesnt do anything yet
def refresh_screen () :
    for widget in frame_chats.winfo_children():
        widget.destroy()

    button_write.place_forget()
    label_space = Label (scrollable_frame , bg = c1 ,  text = '')
    label_space.pack()
>>>>>>> 6ce34b134c04869ceee472af2be608bce7b6b12f

    canvas.yview_moveto(1)
    pass
# Email function
def send_mail():


    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    _emailArray = json.dumps(emailArray)
    s.login("chatbot.kentcomputing@gmail.com", "Groupproject2020")
    s.sendmail("chatbot.kentcomputing@gmail.com", "chatbot.kentcomputing@gmail.com", _emailArray)
    s.quit()
    pass

def provideResponse(ans):
    # This code shows the bot reply and also, if the user input is "bye" then the program will end.
    global label_response
    label_response = Label(scrollable_frame ,text= ans ,bg="white", fg="#000000", justify =LEFT , wraplength = 300, font = 'Verdana 10 bold')
    ts = time.time()
    _time=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    time_stamp = Label(scrollable_frame,text= _time ,bg="white", fg="#000000", justify = LEFT, wraplength = 300, font = 'Verdana 10 bold')
    label_response.pack(anchor = 'w')
    time_stamp.pack(anchor='w')

    userInput = entry.get('1.0', 'end-1c')
    # The following line calls a function after 1/1000 of a second to delete the input. This was done to avoid a minor bug that kept happening
    entry.after(1, emptyUserInput)
    # This changes the user input to all lowercase
    userInput = userInput.lower()
    ongoingConversation, answer = conversation.converse(ans,True)

    if ongoingConversation == False:
        root.destroy()

# This is where the bot will instantly type something to get the conversation started
def introText():
    _answer = conversation.intro()
    provideResponse(_answer)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

""" CHAT FRAME: Main chat screen   """
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

<<<<<<< HEAD
submitimage = PIL.Image.open("icon/image_8.png")
=======

submitimage = Image.open("icon/image_8.png")
>>>>>>> 6ce34b134c04869ceee472af2be608bce7b6b12f
submitImg = ImageTk.PhotoImage(submitimage)
button = Button(bottom_frame, image=submitImg, relief="flat", font='Vardana 10 bold', bg="#2221DE")
button.bind('<Button-1>', submit)
button.place(x=410, y=27)

entry = Text(bottom_frame, bg="white", fg="#000000", height='5', width='45', font='Verdana 10')
entry.bind('<Return>', submit)
entry.place(x=30, y=10)

<<<<<<< HEAD
frame_chats = Frame(frame_chat, bg="#FFFFFF", height='450', width='550')
# Create a canvas within the chat frame
canvas = Canvas(frame_chats, width='550')
# Create a scrollable frame within the canvas
scrollable_frame = Frame(canvas)
# Create a vertical scrollbar
scrollbar = Scrollbar(canvas,orient="vertical",command=canvas.yview)

# https://blog.tecladocode.com/tkinter-scrollable-frames/
# This method was taken from the above source and works perfectly with our code
# It basically makes it so the scrollbar only appears once the size of the canvas is changed
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
# Creates the canvas that the user will see with the scrollbar
canvas.create_window((0, 0), window=scrollable_frame, width='534', anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
=======

>>>>>>> 6ce34b134c04869ceee472af2be608bce7b6b12f

#For scrollbar add canvas widget and place frame w

<<<<<<< HEAD
frame_chats.pack_propagate(0)
frame_chats.pack()
canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side="right", fill="y")

button_write = Button(bottom_frame, text='Email Chat', bg=c3, fg=c2, font='Vardana 8', command=send_mail)
button_back = Button(frame_chat, image=backImg, relief="flat", bg=c3, command=welcome_to_chat).place(x=10, y=10)

exit = PIL.Image.open("icon/icon_exit.png")
exitImage = ImageTk.PhotoImage(exit)
button_front = Button(frame_chat, image=exitImage, relief="flat", bg=c3, command=root.destroy).place(x=500, y=10)

# -----------------------------------------------------------------------------------------------------------
root.title("Monty")
#runs the chatbot application
root.mainloop()

# Code sources: 	
# https://blog.tecladocode.com/tkinter-scrollable-frames/
=======
frame_chats = Frame(frame_chat, bg="#FFFFFF", height='450', width='550')
canvas = Canvas(frame_chats, width='550')
scrollbar = Scrollbar(canvas,orient="vertical",command=canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
canvas.create_window((0, 0), window=scrollable_frame, width='534', anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

frame_chats.pack_propagate(0)

frame_chats.pack()
canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side="right", fill="y")

button_write = Button(bottom_frame, text='Email Chat', bg=c3, fg=c2, font='Vardana 8', command=send_mail)
button_back = Button(frame_chat, image=backImg, relief="flat", bg=c3, command=welcome_to_chat).place(x=10, y=10)

exit = Image.open("icon/icon_exit.png")
exitImage = ImageTk.PhotoImage(exit)
button_front = Button(frame_chat, image=exitImage, relief="flat", bg=c3, command=root.destroy).place(x=500, y=10)





# -----------------------------------------------------------------------------------------------------------
root.title("Chatbot")
root.mainloop ()
>>>>>>> 6ce34b134c04869ceee472af2be608bce7b6b12f
