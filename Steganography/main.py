from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
from stegano import lsb

def show_image():
    try:
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title="Select an image File",
                                            filetypes=(("PNG File", "*.png"),
                                                        ("JPG File", "*.jpg"),
                                                        ("Text File", "*.txt"),
                                                        ("All Files", "*.*")))
        img = Image.open(filename)
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img, width=250, height=250)
        lbl.image = img
    except:
        pass

def Hide():
    try:
        global hide_data
        msg = text_box.get(1.0, END)
        hide_data = lsb.hide(str(filename), msg)
    except:
        pass

def Show():
    try:
        hide_msg =lsb.reveal(filename)
        text_box.delete(1.0, END)
        text_box.insert(INSERT, hide_msg)
    except:
        pass

def Save():
    try:
        hide_data.save("Shahzaib.png")
    except:
        pass

root = Tk()
root.title("Steganography - Hide a Message in an Image")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#2f4155")
# Icon
icon_ = PhotoImage(file="logo.jpg")
root.iconphoto(False, icon_)
# Logo
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)
Label(root, text="CYBER SCIENCE", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)
# Photo Frame
photo_frame = Frame(root, bd=3, bg="black", relief=GROOVE, width=340, height=280)
lbl = Label(photo_frame, bg="black")
lbl.place(x=40, y=10)
photo_frame.place(x=10, y=80)
# Text Frame
text_frame = Frame(root, bd=3, bg="white", relief=GROOVE, width=340, height=280)
text_box = Text(text_frame, bg="white", fg="black", font="Robote 20", relief=GROOVE)
text_box.place(x=0, y=0, width=320, height=295)
scroll_bar = Scrollbar(text_frame)
scroll_bar.place(x=320, y=0, height=300)
scroll_bar.configure(command=text_box.yview)
text_box.configure(yscrollcommand=scroll_bar.set)
text_frame.place(x=350, y=80)
# Button Frame for open image and save image
button_frame = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
Button(button_frame, text="Open Image", width=10, height=2, font="arial 14 bold",command=show_image).place(x=20, y=30)
Button(button_frame, text="Save Image", width=10, height=2, font="arial 14 bold", command=Save).place(x=180, y=30)
Label(button_frame, text="Picture, image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)
button_frame.place(x=10, y=370)
# Button Frame for open image and save image
button_frame1 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
Button(button_frame1, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(button_frame1, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)
Label(button_frame1, text="Picture, image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)
button_frame1.place(x=360, y=370)

root.mainloop()