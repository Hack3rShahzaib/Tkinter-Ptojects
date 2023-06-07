from tkinter import *
import pyttsx3
import customtkinter

def Speak():
    engine = pyttsx3.init()
    text = str(textbox.get(1.0, END))
    engine.say(text=text)
    engine.runAndWait()

root = Tk()
root.title("Text to Speech")
root.geometry("300x300+100+100")
root.resizable(False, False)
root.configure(bg="gray")

textbox = customtkinter.CTkTextbox(root, wrap=WORD, font=("Lucida", 26), width=500, height=230)
textbox.insert(INSERT, "Shahzaib Arain")
textbox.pack()

customtkinter.CTkButton(root, text="Speak", hover_color="green", fg_color="red", text_color="white", command=Speak).place(x=85, y=250)

root.mainloop()