# Task1
from tkinter import *
from tkinter import messagebox

def addTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
     
root = Tk()
root.geometry('500x450+500+200')
root.title('PythonGuides')
root.config(bg='#A7Afff')

frame = Frame(root)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=35,
    height=12,
    bd=0,
    fg='#464646',
    font=('Arial',10),
    selectbackground='#a6a6a6',
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    # 'Dell',
    # 'HP',
    # 'IBM',
    # 'JP MORGAN',
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    root,
    width=35,
    fg='#4B4A49',
    font=('Arial', 14)
    )

my_entry.pack(pady=10)

button_frame = Frame(root)
button_frame.pack(pady=20)

addTask_btn = Button(
    #frame,
    button_frame,
    text='Add Task',
    fg='#4B4A49',
    font=('Arial', 12),
    bg='#c5f776',
    padx=20,
    pady=5,
    command=addTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    #frame,
    button_frame,
    text='Delete Task',
    font=('Arial', 12),
    bg='#ff8b61',
    fg='#4B4A49',
    padx=20,
    pady=5,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


root.mainloop()