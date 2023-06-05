from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def BMI():
    h = float(Height.get())
    w = float(Weight.get())
    m = h/100
    bmi = round(float(w/m**2),1)
    label1.config(text=bmi)
    if bmi <= 18.5:
        label2.config(text="Underweight!")
        label3.config(text="You Have lower weights \n than Normal weights")
    elif bmi>18.5 and bmi<=25:
        label2.config(text="Normal!")
        label3.config(text="it indicates that you are healthy")
    elif bmi>25 and bmi<=30:
        label2.config(text="Overweight!")
        label3.config(text="it indicates that that a person \n slightly overweight \n A doctor may Adwise to lose some \n weight for health reasons")
    else:
        label2.config(text="Obes!")
        label3.config(text="health may risk, if thay do not \n lose weight")

root = Tk()
root.title("BMI Calculater Created By Shahzaib")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")
#icon
icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)
# top Icon
top_img = PhotoImage(file="top.png")
top_lbl = Label(root, image=top_img, bg="#f0f1f5")
top_lbl.place(x=-10, y=10)
# Button B0x
Label(root, bg="lightblue", width=72, height=18).pack(side=BOTTOM)
# two boxes
box_img = PhotoImage(file="box.png")
Label(root, image=box_img).place(x=20, y=100)
Label(root, image=box_img).place(x=240, y=100)
#scale
scale = PhotoImage(file="scale.png")
Label(root, image=scale, bg="lightblue").place(x=20, y=310)
#slider1
def get_crount_value():
    return "{: .2f}".format(crount_value.get())
def slider_changed(event):
    Height.set(get_crount_value())
    size = int(float(get_crount_value()))
    img = Image.open("man.png")
    resized_img = img.resize((50, 10+size))
    photo2 =ImageTk.PhotoImage(resized_img)
    man_image.config(image=photo2)
    man_image.image = photo2
    man_image.place(x=70, y=550-size)
crount_value = DoubleVar()
style = ttk.Style()
style.configure("TScale", background="white")
slider1 = ttk.Scale(root, from_=0, to=220, orient=HORIZONTAL, style="TScale", variable=crount_value, command=slider_changed)
slider1.place(x=80, y=250)
#slider12
def get_crount_value2():
    return "{: .2f}".format(crount_value2.get())
def slider_changed2(event):
    Weight.set(get_crount_value2())
crount_value2 = DoubleVar()
style2 = ttk.Style()
style2.configure("TScale", background="white")
slider2 = ttk.Scale(root, from_=0, to=200, orient=HORIZONTAL, style="TScale", variable=crount_value2, command=slider_changed2)
slider2.place(x=300, y=250)
#entries
Height = StringVar()
Height.set(get_crount_value())
Weight = StringVar()
Height.set(get_crount_value2())
height = Entry(root, textvariable=Height, font="Arial 50", bg="#fff", fg="#000", width=5, bd=0, justify=CENTER)
height.place(x=35, y=160)
weight = Entry(root, textvariable=Weight, font="Arial 50", bg="#fff", fg="#000", width=5, bd=0, justify=CENTER)
weight.place(x=255, y=160)
#main image
man_image = Label(root, bg="lightblue")
man_image.place(x=70, y=530)

Button(root, text="View Report", width=15, height=2, font="Araial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(x=280, y=340)

label1 =Label(root, font="arial 60 bold", bg="lightblue", fg="#fff")
label1.place(x=120, y=305)
label2 =Label(root, font="arial 20 bold", bg="lightblue", fg="#b3ba3a")
label2.place(x=200, y=430)
label3 =Label(root, font="arial 10 bold", bg="lightblue")
label3.place(x=200, y=500)

root.mainloop()