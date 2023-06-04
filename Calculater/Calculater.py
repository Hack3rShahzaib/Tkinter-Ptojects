from tkinter import Tk, Button, Entry, StringVar

class Caculater:
    def __init__(self, master) -> None:
        master.title("Calculater Created By Shahzaib")
        master.geometry("357x420+150+100")
        master.resizable(False, False)
        master.config(bg="gray")
        self.equation = StringVar()
        self.entry_value = ""
        self.equation.set("Shahzaib Arain")
        Entry(master, width=17, font="Arial 28 bold", bg="#2e5d33", fg="white", textvariable=self.equation).place(x=0, y=0)
        Button(master, text="(", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show("(")).place(x=0 , y=50)
        Button(master, text=")", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show(")")).place(x=90 , y=50)
        Button(master, text="%", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show("%")).place(x=180, y=50)
        Button(master, text="1", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show(1)).place(x=0, y=125)
        Button(master, text="2", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show(2)).place(x=90, y=125)
        Button(master, text="3", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show(3)).place(x=180, y=125)
        Button(master, text="4", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show(4)).place(x=0, y=200)
        Button(master, text="5", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show(5)).place(x=90, y=200)
        Button(master, text="6", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show(6)).place(x=180, y=200)
        Button(master, text="7", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show(7)).place(x=0, y=275)
        Button(master, text="8", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show(8)).place(x=180, y=275)
        Button(master, text="9", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show(9)).place(x=90, y=275)
        Button(master, text="0", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show(0)).place(x=90, y=350)
        Button(master, text=".", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show(".")).place(x=180, y=350)
        Button(master, text="+", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show("+")).place(x=270, y=275)
        Button(master, text="-", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show("-")).place(x=270, y=200)
        Button(master, text="/", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show("/")).place(x=270, y=50)
        Button(master, text="x", width=11, height=4, relief="flat", bg="red", fg="white", command=lambda:self.show("8")).place(x=270, y=125)
        Button(master, text="=", width=11, height=4, relief="flat", bg="red", fg="white", command=self.solve).place(x=270, y=350)
        Button(master, text="C", width=11, height=4, relief="flat", bg="red", fg="white", command=self.clear).place(x=0, y=350)
        
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)
        
    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)
        
    def solve(self):
        self.entry_value = eval(self.entry_value)
        self.equation.set(self.entry_value)

root = Tk()

calculater = Caculater(root)

root.mainloop()