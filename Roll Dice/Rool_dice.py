from tkinter import *
import random

def roll():
    dice = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
    first_dice = random.choice(dice)
    second_dice = random.choice(dice)
    roll_lbl.config(text=f"{first_dice}{second_dice}")
    roll_lbl.pack()

root = Tk()
root.geometry("700x450+150+100")
root.title("Roll Dice Created By Shahzaib")
root.config(bg="#2d5f7e")

roll_lbl = Label(root, font="times 300", bg="#2d5f7e", fg="white")
roll_btn =Button(root, text="Let's Roll...", width=30, height=3, font=10, bg="red", fg="white", command=roll)
roll_btn.pack(padx=10, pady=10)

root.mainloop()