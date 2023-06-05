from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def show_image():
    try:
        path = filedialog.askopenfilename(initialdir="/", title="Select Image File", filetypes=[("JPG Files", "*.jpg"), ("PNG Files", "*.png")])
        img = Image.open(path)
        img = img.resize((380, 520))
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img)
        lbl.image = img
    except:
        messagebox.showerror("File Error", "Somthing went wrong")
root = Tk()
root.title("Image Viewer Created By Shahzaib")
root.geometry("400x450+150+80")
root.resizable(False, False)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM, padx=15, pady=15)
lbl = Label(root, width=380, height=520, bg="skyblue")
lbl.pack(pady=5)
btn = Button(bottomFrame, text="Select Image", bg="#4f3ed7", fg="white", command=show_image)
btn.pack(side=LEFT)
btn1 = Button(bottomFrame, text="Exit", bg="#ff8caf", fg="white", command=root.destroy)
btn1.pack(side=LEFT, padx=12)
root.mainloop()