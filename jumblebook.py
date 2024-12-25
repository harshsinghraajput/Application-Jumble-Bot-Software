import tkinter
from tkinter import *
from tkinter import messagebox
import random
from random import shuffle

answers = ["America" , "India" , "Australia"]

questions = []


for i in answers:
    words = list(i)
    shuffle(words)
    questions.append(words)


num = random.randint(0 , len(questions)-1)
def initial():
    global questions , num
    lb1.configure(text=questions[num])

def answercheck():
    global questions , num , answers
    userinput = e1.get()#This takes the user input and gets the value 
    if userinput == answers[num]:
        messagebox.showinfo('Puchiee','Your answer was correct :) ')
    else:
            messagebox.showinfo('Better Luck Next Time','Wrong Answer :( ')
            e1.delete(0,END)

def resetswitch():
    global questions , answers ,num
    num = random.randint(0, len(questions)-1)
    lb1.configure(text=questions[num])
    e1.delete(0, END)

window = Tk()
window.geometry("300x300")
window.configure(background='#75DA8B')
window.title("Jumble Book")
window.iconbitmap("pupu.ico")

lb1 = Label(window , font='times 20' , bg='#75DA8B' , fg='#333945')
lb1.pack(pady=30, ipady=10 , ipadx=10)

answer = StringVar()
e1 = Entry(window, textvariable=answer)
e1.pack(ipadx=5 , ipady=5)  #Is like m answer area hoga jaha apne log answer dalenge

button1 = Button(window , text="Check" , bg='#26ae60',  width=20 , command=answercheck)
button1.pack(pady=40) #is line m Check aega

button2 = Button(window, text="Reset" , bg='#6ab04c' , width=20 , command=resetswitch )
button2.pack() #is line m reset aega


initial()
window.mainloop()