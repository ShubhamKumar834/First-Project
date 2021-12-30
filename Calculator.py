#===========================================Import libraries=======================================================.
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#===========================Work Window============================================================================.

def btn_1():
    global vals
    global show
    vals = vals + "1"
    show.set(vals)

def btn_2():
    global vals
    global show
    vals = vals + "2"
    show.set(vals)

def btn_3():
    global vals
    global show
    vals = vals + "3"
    show.set(vals)

def btn_4():
    global vals
    global show
    vals = vals + "4"
    show.set(vals)

def btn_5():
    global vals
    global show
    vals = vals + "5"
    show.set(vals)
   
def btn_6():
    global vals
    global show
    vals = vals + "6"
    show.set(vals)

def btn_7():
    global vals
    global show
    vals = vals + "7"
    show.set(vals)

def btn_8():
    global vals
    global show
    vals = vals + "8"
    show.set(vals)

def btn_9():
    global vals
    global show
    vals = vals + "9"
    show.set(vals)

def btn_0():
    global vals
    global show
    vals = vals + "0"
    show.set(vals)

def plus():
    global val2
    global vals
    val2 = int(vals)
    global operator 
    operator = "+"
    vals = vals + "+"
    show.set(vals)
    
def minus():
    global val2
    global vals
    val2 = int(vals)
    global operator 
    operator = "-"
    vals = vals + "-"
    show.set(vals)

def multiply():
    global val2
    global vals
    val2 = int(vals)
    global operator 
    operator = "*"
    vals = vals + "*"
    show.set(vals)

def divid():
    global val2
    global vals
    val2 = int(vals)
    global operator 
    operator = "/"
    vals = vals + "/"
    show.set(vals)

def clear():
    global vals
    global val2
    global operator
    vals = ""
    val2 = 0
    operator = ""
    show.set(vals)
 
def equal():
    global vals
    global val2
    global operator
    val3 = vals
    if operator == "+":
        x = int((val3.split("+")[1]))
        e = val2 + x
        show.set(e)
        vals = str(e)

    elif operator == "-":
        x = int((val3.split("-")[1]))
        e = val2 - x
        show.set(e)
        vals = str(e)

    elif operator == "*":
        x = int((val3.split("*")[1]))
        e = val2 * x
        show.set(e)
        vals = str(e)    

    elif operator == "/":
        x = int((val3.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Please Enter valid value for division.")
            val2 = ""
            vals = ""
            show.set(vals)
        else:
            e = int(val2 / x)
            show.set(e)
            vals = str(e)

if __name__ == '__main__':
    cal= Tk()
    cal.iconbitmap('E:\python programs\cal_icon (2).ico')
    cal.title(" Simple Calculator. ")
    cal.geometry("350x350")
    cal.resizable(0,0)
    cal.configure(bg = 'Grey')
    vals = ""
    val2 = 0
    operator = ""
    show = StringVar(value = "0")

#========Display result======================================================================================.
    result = Entry(cal, width = 40, justify = RIGHT, font = ('Roman new times',11,'bold'), textvariable = show, relief = GROOVE, bd = 5)
    result.grid(column = 0,columnspan=4, row=0, rowspan=2, padx=7, pady=10, ipadx=2, ipady=20)

#=================================================Buttons====================================================. 
    b7 = Button(cal, text='7', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='#808080', command=btn_7)
    b7.grid(row=2, column=0, padx=2, pady=2)
    b8 = Button(cal, text='8', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='#808080', command=btn_8)
    b8.grid(row=2, column=1, padx=2, pady=2)
    b9 = Button(cal, text='9', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='#808080', command=btn_9)
    b9.grid(row=2, column=2, padx=2, pady=2)
    plus = Button(cal, text='+', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='#808080', command = plus)
    plus.grid(row=2, column=3, padx=2, pady=2)

#==============================================================================================================.
    b4 = Button(cal, text='4', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='#808080', command=btn_4)
    b4.grid(row=3, column=0, padx=2, pady=2)
    b5 = Button(cal, text='5', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='#808080', command=btn_5)
    b5.grid(row=3, column=1, padx=2, pady=2)
    b6 = Button(cal, text='6', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='#808080', command=btn_6)
    b6.grid(row=3, column=2, padx=2, pady=2)
    minus = Button(cal, text='-', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='#808080', command=minus)
    minus.grid(row=3, column=3, padx=2, pady=2)

#==============================================================================================================.
    b1 = Button(cal, text='1', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='#808080', command=btn_1)
    b1.grid(row=4, column=0, padx=2, pady=2)
    b2 = Button(cal, text='2', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='#808080', command=btn_2)
    b2.grid(row=4, column=1, padx=2, pady=2) 
    b3 = Button(cal, text='3', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='#808080', command=btn_3)
    b3.grid(row=4, column=2, padx=2, pady=2)
    multiply = Button(cal, text='*', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='#808080', command=multiply)
    multiply.grid(row=4, column=3, padx=2, pady=2)

#==============================================================================================================.
    b0 = Button(cal, text='0', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='#808080', command=btn_0)
    b0.grid(row=5, column=0, padx=2, pady=2)
    clear = Button(cal, text='Clear', bd=3, relief=RAISED, width=5, height=2, font=('oswald',11,'bold'), bg='red', command = clear)
    clear.grid(row=5, column=1, padx=2, pady=2)
    equal = Button(cal, text='=', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='green', command = equal)
    equal.grid(row=5, column=2, padx=2, pady=2)
    divid = Button(cal, text='/', bd=3, relief=RAISED, width=5, height=2, font=('Spectral',11,'bold'), bg='#808080', command = divid)
    divid.grid(row=5, column=3, padx=2, pady=2)

#================Start Gui Appication=============================================================================.
    cal.mainloop()


