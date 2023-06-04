from tkinter import *
import time

def change_time():
    crount_time = time.strftime("%H:%M:%S:%p")
    lbl.configure(text=crount_time)
    root.after(1000, change_time)

root = Tk()
root.title("Digital Clock Creared By Shahzaib")

lbl = Label(root, font="digital-7 70 bold", bg="black", fg="red")
lbl.pack(anchor="center")
change_time()
root.mainloop()