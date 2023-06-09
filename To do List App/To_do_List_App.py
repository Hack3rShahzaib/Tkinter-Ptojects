from tkinter import *

task_list = []

def open_task_file():
    try:
        global task_list
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(END, task)
    except:
        f = open("tasks.txt", "w")
        f.close()                  

def add_task():
    try:
        task = str(task_value.get())
        task_value.set("")
        task_list.append(task+"\n")
        with open("tasks.txt", "w") as file:
            for tasks in task_list:
                file.write(tasks)
        listbox.insert(END, task)
    except:
        pass

def delete_task():
    try:
        task = str(listbox.get(ANCHOR))
        if task in task_list:
            task_list.remove(task)
            with open("tasks.txt", "w") as file:
                for tasks in task_list:
                    file.write(tasks)
        listbox.delete(ANCHOR)
    except:
        pass

root = Tk()
root.title("To-Do-List Created By Shahzaib Arain")
root.geometry("400x650+400+100")
root.resizable(False, False)

#icon
icon_ = PhotoImage(file="task.png")
root.iconphoto(False, icon_)

# Top Bar
bar_img = PhotoImage(file="topbar.png")
Label(root, image=bar_img).pack()

dock_image = PhotoImage(file="dock.png")
Label(root, image=dock_image, bg="#32405b").place(x=30, y=25)

note_image = PhotoImage(file="task.png")
Label(root, image=note_image, bg="#32405b").place(x=340, y=25)

heading = Label(root, text="All Tasks", bg="#32405b", fg="white", font="arial 20 bold")
heading.place(x=130, y=20)

frame =Frame(root, width=400, height=50, bg="white")

task_value = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0, textvariable=task_value)
task_entry.place(x=10, y=7)
task_entry.focus()

btn = Button(frame, text="Add", font="arial 20 bold", bg="#5a95ff", fg="#fff", bd=0, command=add_task)
btn.place(x=300, y=0)

frame.place(x=0, y=180)

frame1 = Frame(root, width=700, height=280, bd=3, bg="#32405b")

listbox = Listbox(frame1, font="arail 12", bg="#32405b", width=40, height=16, selectbackground="#5a95ff", cursor="hand2", fg="#fff")

scroll = Scrollbar(frame1, command=listbox.yview)
listbox.config(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)

listbox.pack(side=LEFT, fill=BOTH)

frame1.pack(pady=(160, 0))

del_img = PhotoImage(file="delete.png")
del_btn = Button(root, image=del_img, bd=0, command=delete_task)
del_btn.pack(side=BOTTOM, pady=13)

open_task_file()

root.mainloop()