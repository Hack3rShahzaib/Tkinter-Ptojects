from tkinter import *
from tkinter import messagebox, filedialog
import subprocess
import os

file = ""
def open_file():
    file_path = filedialog.askopenfilename(initialdir="/",filetypes=[("Python Files", "*.py")])
    with open(file_path, "r") as f:
        code = f.read()
        code_input.delete(1.0, END)
        code_input.insert(INSERT, code)
        set_file_path(file_path)
def save_file():
    if  file=="":
        path = filedialog.asksaveasfilename(initialdir="/",filetypes=[("Python Files", "*.py")])
    else:
        path = file
    with open(path, "w") as f:
        code = code_input.get(1.0, END)
        f.write(code)
        set_file_path(path)
def run_file():
    if file == "":
        messagebox.showerror("File Error", "Save Your Code in a File Buddy")
        return
    command = f"python test.py"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.delete(1.0, END)
    code_output.insert(INSERT, output)
    code_output.insert(INSERT, error)
def set_file_path(path):
    global file
    file = path

root = Tk()
root.title("Python IDLE Created By Shahzaib")
root.geometry("1280x720+150+80")
root.resizable(False, False)
root.config(bg="#323846")
#icon
icon_ = PhotoImage(file="logo.png")
root.iconphoto(False, icon_)
#code input
code_input = Text(root, font="consolas 18", wrap=WORD)
code_input.place(x=180, y=0, width=680, height=720)
#Scroll Bar
scroll_bar = Scrollbar(code_input)
scroll_bar.pack(side=RIGHT, fill=Y)
# Scroll Bar and code input merging
scroll_bar.config(command=code_input.yview)
code_input.config(yscrollcommand=scroll_bar.set)
# code Output
code_output = Text(root, font="consolas 15", bg="#323846", fg="lightgreen", wrap=WORD)
code_output.place(x=860, y=0, width=420, height=720)
#Scroll Bar
scroll_bar2 = Scrollbar(code_output)
scroll_bar2.pack(side=RIGHT, fill=Y)
# Scroll Bar and code input merging
scroll_bar2.config(command=code_output.yview)
code_output.config(yscrollcommand=scroll_bar.set)
#Button Images
run_img = PhotoImage(file="run.png")
open_img = PhotoImage(file="open.png")
save_img = PhotoImage(file="save.png")
#Buttons
Button(root, image=open_img, bg="#323846", bd=0, command=open_file).place(x=30, y=30)
Button(root, image=save_img, bg="#323846", bd=0, command=save_file).place(x=30, y=145)
Button(root, image=run_img, bg="#323846", bd=0, command=run_file).place(x=30, y=260)

root.mainloop()