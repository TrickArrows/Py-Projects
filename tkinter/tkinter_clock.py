from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock");
root.geometry("300x100");

#initializing label 1  
L1 = Label(root)
L1.pack(anchor='center')

#initializing label 2
L2 = Label(root)
L2.pack(anchor='center')



def time():
    string = strftime('%H:%M:%S  %p');
    L1.config(text = "label 1 \n Clock:  - "+string)
    L1.after(1000,time)


def strn():
    L2.config(text = "label 2 - "+"hello world");

    
time()
strn()

mainloop()
