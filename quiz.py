

from tkinter import *




total = 0

q = [

"What is the name of the 45th president of the United States ?",
"What is the capital of the United States ?",
"What is the largest state of the United States ?",
"Who is the founder of the white house of the United States ?"

]


a0 = ["Barack Obama","Bill Clinton","Donald J. Trump","George W. Bush"]
a1 = ["Chicago","NewYork","Florida","Washington"]
a2 = ["NewYork","California","Ohio","Texas"]
a3 = ["Abraham Lincoln","Johnson","George Washington","Eisenhower"]


def bnext():

   global windows
   windows = Toplevel(root)
   windows.title("Question 1")
   windows.geometry()
   root.withdraw()

   lbl1 = Label(windows,text = q[0],font = ('arial',10,'bold')).pack(side = TOP)
   cb1 = Radiobutton(windows, text=a0[0], value=0,variable = v0,command = checked).pack(side=LEFT)
   cb2 = Radiobutton(windows, text=a0[1], value=1,variable = v0,command = checked).pack(side=LEFT)
   cb3 = Radiobutton(windows, text=a0[2], value=2,variable = v0,command = checked).pack(side=LEFT)
   cb4 = Radiobutton(windows, text=a0[3], value=3,variable = v0,command = checked).pack(side=LEFT)
   btn1 = Button(windows,text = "next",font = ('arial',12,'bold'),fg = 'blue',
                 command = bnext2).pack(side = RIGHT)
   btn2 = Button(windows,text = "back",font = ('arial',12,'bold'),fg = 'blue',
                 command = bback).pack(side = LEFT)
   windows.mainloop()


def bnext2():

   global windows3
   windows3 = Toplevel(windows)
   windows3.title("Question 2")
   windows3.geometry()
   windows.withdraw()

   lbl2 = Label(windows3, text=q[1], font=('arial', 10, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows3, text=a1[0], value=0,variable = v1,command = checked).pack(side=LEFT)
   cb6 = Radiobutton(windows3, text=a1[1], value=1,variable = v1,command = checked).pack(side=LEFT)
   cb7 = Radiobutton(windows3, text=a1[2], value=2,variable = v1,command = checked).pack(side=LEFT)
   cb8 = Radiobutton(windows3, text=a1[3], value=3,variable = v1,command = checked).pack(side=LEFT)

   btn3 = Button(windows3,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext3).pack(side=RIGHT)
   btn4 = Button(windows3,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback2).pack(side=LEFT)
   windows3.mainloop()


def bnext3():

   global windows4
   windows4 = Toplevel(windows3)
   windows4.title("Question 3")
   windows4.geometry()
   windows3.withdraw()

   lbl2 = Label(windows4, text=q[2], font=('arial', 10, 'bold')).pack(side=TOP)
   cb9 = Radiobutton(windows4, text=a2[0], value=0,variable = v2,command = checked).pack(side=LEFT)
   cb10 = Radiobutton(windows4, text=a2[1], value=1,variable = v2,command = checked).pack(side=LEFT)
   cb11 = Radiobutton(windows4, text=a2[2], value=2,variable = v2,command = checked).pack(side=LEFT)
   cb12 = Radiobutton(windows4, text=a2[3], value=3,variable = v2,command = checked).pack(side=LEFT)

   btn5 = Button(windows4,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext4).pack(side=RIGHT)
   btn6 = Button(windows4,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback3).pack(side=LEFT)
   windows4.mainloop()


def bnext4():

   global windows5
   windows5 = Toplevel(windows4)
   windows5.title("Question 4")
   windows5.geometry()
   windows4.withdraw()

   lbl2 = Label(windows5, text=q[3], font=('arial', 10, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows5, text=a3[0], value=0,variable = v3,command = checked).pack(side=LEFT)
   cb6 = Radiobutton(windows5, text=a3[1], value=1,variable = v3,command = checked).pack(side=LEFT)
   cb7 = Radiobutton(windows5, text=a3[2], value=2,variable = v3,command = checked).pack(side=LEFT)
   cb8 = Radiobutton(windows5, text=a3[3], value=3,variable = v3,command = checked).pack(side=LEFT)

   btn99 = Button(windows5,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext5).pack(side=RIGHT)
   btn7 = Button(windows5,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback4).pack(side=LEFT)

   windows5.mainloop()


def bnext5():

   global windows6
   windows6 = Toplevel(windows5)
   windows6.title("Final Result")
   windows6.geometry("400x500")
   windows5.withdraw()
   btn8 = Button(windows6, text="back", font=('arial', 12, 'bold'), fg='blue', command=bback5).pack(side=LEFT)
   bquit = Button(windows6, text="Quit", font=('arial', 12, 'bold'),
                  fg='blue', command=windows6.destroy).pack(side=RIGHT)
   bf = Label(windows6,text = "Your score is " + str(total) + "/4",font = ("arial",12,"bold"),fg = "red")
   bf.pack(side = BOTTOM)

   windows6.mainloop()


def bback():

    windows.withdraw()
    root.deiconify()
    root.mainloop()


def bback2():

    windows3.withdraw()
    windows.deiconify()
    windows.mainloop()


def bback3():

    windows4.withdraw()
    windows3.deiconify()
    windows3.mainloop()


def bback4():

    windows5.withdraw()
    windows4.deiconify()
    windows4.mainloop()


def bback5():

    windows6.withdraw()
    windows5.deiconify()
    windows5.mainloop()


def checked():

    #global c
    #global w

    c = 0
    if v0.get() == 2:

        c += 1

    if v1.get() == 3:

        c += 1

    if v2.get() == 1:

        c += 1

    if v3.get() == 2:

        c += 1

    global total
    total = c


root = Tk()

v0 = IntVar()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()


root.title("Quiz Program")
root.geometry("400x500")

lbl0 = Label(root,text = "Answer the following questions",font = ("arial",15,"bold"),fg = 'purple').pack(side = TOP)
lbl00 = Label(root,text = "about the history of the United states", fg = 'purple').pack(side = TOP)

btn1 = Button(root,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext).pack(side = RIGHT)


root.mainloop()