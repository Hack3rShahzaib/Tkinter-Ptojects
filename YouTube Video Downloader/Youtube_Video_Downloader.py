from tkinter import *
import customtkinter
from pytube import YouTube

def download_video():
    link = linkValue.get()
    yt = YouTube(url=link).streams.get_highest_resolution()
    yt.download()
    lbl.config(text="Download Complete")

root = Tk()
root.resizable(False, False)
root.title("YT Video Downloader By Shahzaib")
root.geometry("500x300+200+200")
root.config(bg="red")

customtkinter.CTkLabel(root, text="Video Downloader", text_color="white", font=("Arial", 30, "bold")).place(x=125, y=40)

linkValue = StringVar()
linkRntry = customtkinter.CTkEntry(root, font=("Lucida", 28), width=400, textvariable=linkValue).place(x=55, y=90)

customtkinter.CTkButton(root, text="Download", font=("Lucida", 28), fg_color="green", hover_color="black", command=download_video).place(x=180, y=150)

lbl = Label(root, fg="lightgreen", bg="red", font=("Arial", 30, "bold"))
lbl.place(x=65, y=210)

root.mainloop()