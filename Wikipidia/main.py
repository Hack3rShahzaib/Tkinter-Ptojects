from tkinter import *
from wikipedia import summary as Search

def search_on_wikipidia():
    search_prompt = prompt.get()
    text.delete(1.0, END)
    try:
        aswer = Search(search_prompt)
        text.insert(INSERT, aswer)
    except:
        text.insert(INSERT, "Please Check Your Input and Internet")
root = Tk()
root.title("Wikipidia")
topFrame = Frame(root)
prompt = Entry(topFrame, font="Lucida 16")
prompt.pack()
Search_btn = Button(topFrame, text="Search", font="Arial 14", bg="red", fg="white", command=search_on_wikipidia)
Search_btn.pack()
topFrame.pack(side=TOP)

buttomFrame = Frame(root)
scroll = Scrollbar(buttomFrame)
text = Text(buttomFrame, width=30, height=15, wrap=WORD, font="Lucida 14", yscrollcommand=scroll.set)
scroll.config(command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
text.pack()
buttomFrame.pack()

root.mainloop()