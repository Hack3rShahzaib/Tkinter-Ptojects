from tkinter import *

mode = True

def Toggle():
    global mode
    if mode:
        btn.config(image=off, bg="#26242f")
        root.config(bg="#26242f")
        mode = False
    else:
        btn.config(image=on, bg="white")
        root.config(bg="white")
        mode = True    

root = Tk()
root.title("Toggle Switch Created By Shahzaib")
root.geometry("400x600")
root.config(bg="white")

on = PhotoImage(file="light.png")
off = PhotoImage(file="dark.png")

btn = Button(root, image=on, bd=0, bg="white", activebackground="white", command=Toggle)
btn.pack(padx=50, pady=50)

root.mainloop()