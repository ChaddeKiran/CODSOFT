#Task 3 Password Generator
from tkinter import * 
import random
 
root = Tk()
root.geometry("700x300")
passwrd = StringVar()
passwordlen = IntVar()
passwordlen.set(0)
 
 
def generate():  # Function to generate the password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    password = ""
    for x in range(passwordlen.get()):
        password = password + random.choice(pass1)
    passwrd.set(password)
 
# function to copy the passcode
 
# Labels
 
 
l1=Label(root, text="Password Generator", font="Arial 24 bold").pack()
l2=Label(root, text="Enter the password length ", font="Arial 14 bold").pack(pady=3)
e1=Entry(root, textvariable=passwordlen, font="Arial 12 bold", width=20).pack(pady=3)
b1=Button(root, text="Generate Password ",font="Arial 14 bold", bg="#FDBA14", command=generate).pack(pady=7)
e2=Entry(root, textvariable=passwrd, font="Arial 14 bold", width=35).pack(pady=3)
root.mainloop()