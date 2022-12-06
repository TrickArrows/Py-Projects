from tkinter import *


root = Tk()
root.title("Register Here");
root.geometry("500x400");

def getvals():
    print("submited");

    
Label(root, text="Python Registration Form \n", font="arial 15 bold").grid();

#Name Field
name = Label(root, text="Name", font="arial 10 bold").grid(row=1, column=0);
dob = Label(root, text="Date of Birth", font="arial 10 bold").grid(row=2, column=0);
mail = Label(root, text="Mail ID", font="arial 10 bold").grid(row=3, column=0);
mobile = Label(root, text="Mobile Number", font="arial 10 bold").grid(row=4, column=0);

#Entry Field
name_Value = Entry(root, textvariable = StringVar).grid(row=1, column=1);
dob_Value = Entry(root, textvariable = StringVar).grid(row=2, column=1);
mail_Value = Entry(root, textvariable = StringVar).grid(row=3, column=1);
mobile_Value = Entry(root, textvariable = IntVar).grid(row=4, column=1);

#checkbox
checkbtn = Checkbutton(text="Privacy and Policy").grid(row=5, column=1);

#submit button
Button(text="Submit", command=getvals).grid(row=6, column=1);

mainloop()
