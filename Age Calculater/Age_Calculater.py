from tkinter import *
from datetime import date

def calculateAge():
    today = date.today()
    year = int(yearEntry.get())
    month = int(monthEntry.get())
    day = int(dayEntry.get())
    age = today.year - year - ((today.month, today.day) < (month, day))
    name =nameValue.get()
    out = "{} your age is: {}".format(name, age)
    outValue = StringVar()
    Entry(bg="#2d000f", fg="white", font=30, textvariable=outValue, width=30, bd=0).place(x=300, y=530)
    outValue.set(out)

root = Tk()
root.title("Age Calculater Created By Shahzaib")
root.resizable(False, False)
root.geometry("800x600")
root.configure(bg="#2d000f")

icon_img = PhotoImage(file="Age calculator  .png")
Label(root, image=icon_img, bg="#2d000f").pack(padx=15, pady=15)

Label(root, text="Name", font=23, bg="#2d000f", fg="white").place(x=200, y=250)
Label(root, text="Year", font=23, bg="#2d000f", fg="white").place(x=200, y=300)
Label(root, text="Month", font=23, bg="#2d000f", fg="white").place(x=200, y=350)
Label(root, text="Day", font=23, bg="#2d000f", fg="white").place(x=200, y=400)

nameValue = StringVar()
nameValue.set("Shahzaib Arain")
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue, width=30, bd=3, font=20)
yearEntry = Entry(root, textvariable=yearValue, width=30, bd=3, font=20)
monthEntry = Entry(root, textvariable=monthValue, width=30, bd=3, font=20)
dayEntry = Entry(root, textvariable=dayValue, width=30, bd=3, font=20)

nameEntry.place(x=300, y=250)
yearEntry.place(x=300, y=300)
monthEntry.place(x=300, y=350)
dayEntry.place(x=300, y=400)

Button(root, text="CacuLate", bg="#2d000f", fg="white", font=23, command=calculateAge).place(x=370, y=470)

root.mainloop()