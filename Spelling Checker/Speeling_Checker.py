from tkinter import *
import customtkinter
from textblob import TextBlob

def correct_text():
    text = textValue.get()
    if len(text) > 6:
        lbl.place(x=10, y=210)
    elif len(text) <= 6:
        lbl.place(x=50, y=210)
    ctext = TextBlob(text)
    right = str(ctext.correct())
    lbl_text = f"Correct Text is : {right}"
    lbl.config(text=lbl_text)
root = Tk()
root.resizable(False, False)
root.title("Spelling Checker By Shahzaib")
root.geometry("500x300+200+200")
root.config(bg="lightgreen")

customtkinter.CTkLabel(root, text="Spelling Checker", text_color="black", font=("Arial", 30, "bold")).place(x=125, y=40)

textValue = StringVar()
textValue.set("Shahzaib Arain")
textRntry = customtkinter.CTkEntry(root, font=("Lucida", 28), width=400, textvariable=textValue).place(x=55, y=90)

customtkinter.CTkButton(root, text="Check", font=("Lucida", 28), fg_color="red", hover_color="black", command=correct_text).place(x=180, y=150)

lbl = Label(root, fg="black", bg="lightgreen", font=("Arial", 30, "bold"))

root.mainloop()