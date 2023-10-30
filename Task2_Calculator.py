#Task 2
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("600x350")

def cal_sum():
   val1=int(a.get())
   val2=int(b.get())
   op= c.get()
   sum = 0
   if(op=="+"):
    sum=val1+val2
   elif(op=="-"):
    sum=val1-val2
   elif(op=="*"):
    sum=val1*val2
   elif(op=="/"):
    sum=val1/val2
   elif(op=="//"):
    sum=val1//val2
   else:
    msg=messagebox.showinfo( "Warning", "Invalid opration!!!")  
   label.config(text=sum)

Label(root, text="Enter First Number").pack()
a=Entry(root, width=35)
a.pack()
Label(root, text="Enter Second Number").pack()
b=Entry(root, width=35)
b.pack()
Label(root, text="Enter Operation").pack()
c=Entry(root, width=35)
c.pack()

label=Label(root, text="Total Sum : ")
label.pack(pady=20)

Button(root, text="Calculate Sum", command=cal_sum).pack()

root.mainloop()

