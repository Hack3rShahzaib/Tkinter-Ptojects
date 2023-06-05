from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Calendar")
root.resizable(False, False)
root.configure(bg="lightblue")

cal = Calendar(root, setmode="day", date_pattetn="d/m/yy")
cal.pack()

root.mainloop()