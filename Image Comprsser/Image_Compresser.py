from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os

def open_image():
    global img
    try:
        file_path = filedialog.askopenfilename(filetypes=(("PNG", "*.png"),
                                                            ("JPG", "*.jpg")))
        img = Image.open(file_path)
        lbl_img = ImageTk.PhotoImage(image=img)
        img_lbl.config(image=lbl_img, width=400, height=400)
        img_lbl.image = lbl_img
    except Exception as e:
        pass

def compress_image():
    global compressed_image
    try:
        img_width, img_height =img.size
        compressed_image = img.resize((img_width, img_height), Image.ANTIALIAS)
    except Exception as e:
        pass

def save_image():
    try:
        file_name = filedialog.asksaveasfilename()
        compressed_image.save(file_name+".png")
    except Exception as e:
        pass

root = Tk()
root.title("Image Compresser Created By Shahzaib")
root.geometry("400x460")
root.resizable(False, False)

topFrame = Frame(root, bd=3, bg="#000000", relief=GROOVE, width=400, height=400)
img_lbl = Label(topFrame, bg="black")
img_lbl.place(x=0, y=0)
topFrame.pack()

buttomFrame = Frame(root, bd=3, bg="#2d41f3", width=400, height=100, relief=GROOVE)

open_img_btn = Button(buttomFrame, text="Open Image", font="Lucida 16", bg="red", fg="white", command=open_image)
open_img_btn.place(x=5, y=5)

comp_img_btn = Button(buttomFrame, text="Compress", font="Lucida 16", bg="green", fg="white", command=compress_image)
comp_img_btn.place(x=140, y=5)

save_img_btn = Button(buttomFrame, text="Save Image", font="Lucida 16", bg="yellow", fg="white", command=save_image)
save_img_btn.place(x=260, y=5)

buttomFrame.pack()

root.mainloop()