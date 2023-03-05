# pip install googletrans==3.1.0a0

from googletrans import Translator
from gtts import gTTS
from tkinter import *

window = Tk()
window.geometry('620x280')

set_bg = PhotoImage(file="img.png")
label_1 = Label(window,image=set_bg)
label_1.place(x=0, y=-50)

e1 = Entry(window, bg="white", fg="red", font=("Arial", 25, "bold") )
e1.place(x=20,y=20)

def convert_language():
    a1 = e1.get()
    t1 = Translator()
    t2 = clicked_option.get()

    if t2 == "English":
        convert = "en"
    elif t2 == "Hindi":
        convert = "hi"
    elif t2 == "German":
        convert = "de"
    elif t2 == "French":
        convert = "fr"
    elif t2 == "Spanish":
        convert = "es"
    elif t2 == "Russian":
        convert = "ru"

    trans_text = t1.translate(a1, dest = convert)
    trans_text = trans_text.text
    ob1 = gTTS(text=trans_text, slow=False, lang=convert)
    label_2.config(text=trans_text)

choices = [
    "English",
    "Hindi",
    "German",
    "French",
    "Spanish",
    "Russian"
]

clicked_option = StringVar()
clicked_option.set("Select Language")

list_drop = OptionMenu(window, clicked_option, *choices)
list_drop.configure(background="green", foreground="white", font=('Arial',15,"bold"))
list_drop.place(x=400, y=20)

label_2 = Label(window, text="\t\t\t\t\t\t", bg ="black",fg="white",font=("Arial",40,"bold"))
label_2.place(x=0 ,y=170)
label_2 = Label(window, text="Translated text",bg="black",fg="white",font=("Arial",40,"bold"))
label_2.place(x=20,y=170)

Button_1 = Button(window, text="Translate",bg="red",fg="white",font=("Arial",25, "bold"),command=convert_language)
Button_1.place(x=120,y=80)

window.mainloop()