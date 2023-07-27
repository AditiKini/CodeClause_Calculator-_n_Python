from tkinter import *


window = Tk()
window.title("Calculator")
window.config(padx=10, pady=10, background="black")
window.minsize(width=50, height=100)


def click(num):
    current = Data.get()
    Data.delete(0, END)
    Data.insert(END, current + str(num))


def calculate():
    expression = Data.get()
    try:
        result = eval(expression)
        Data.delete(0, END)
        Data.insert(END, str(result))
    except Exception:
        Data.delete(0, END)
        Data.insert(END, "Error")


def clear_all():
    Data.delete(0, END)


Data = Entry(width=28,font=("Arial", 12))
Data.grid(row=1, column=1, columnspan=4, sticky="w", padx=5, pady=5)


one = Button(text="1", width=7,  bg="grey",  command = lambda :  click("1"))
two = Button(text="2", width=7,bg="grey",  command = lambda : click("2"))
three = Button(text="3", width=7, bg="grey", command = lambda : click("3"))
four = Button(text="4", width=7, bg="grey", command = lambda : click("4"))
five = Button(text="5", width=7, bg="grey", command = lambda : click("5"))
six = Button(text="6", width=7,bg="grey",  command = lambda : click("6"))
seven = Button(text="7", width=7,bg="grey",  command = lambda : click("7"))
eight = Button(text="8", width=7,bg="grey",  command = lambda : click("8"))
nine = Button(text="9", width=7, bg="grey", command = lambda : click("9"))
zero = Button(text="0", width=7,bg="grey",  command = lambda : click("0"))
dot = Button(text=".", width=7, bg="grey", command = lambda : click("."))
divide = Button(text="/", width=7, bg="grey", command = lambda : click("/"))
multiply = Button(text="x", width=7,bg="grey",  command = lambda : click("*"))
subtract = Button(text="-", width=7,bg="grey",  command = lambda : click("-"))
add = Button(text="+", width=7,bg="grey",  command = lambda : click("+"))
equal = Button(text="=", width=7,bg="orange",  command = calculate)
clear = Button(text="C", width=7,bg="cyan",  command = clear_all)

one.grid(row=4, column=1, sticky="w",padx=3, pady=3)
two.grid(row=4, column=2, sticky="w",padx=3, pady=3)
three.grid(row=4, column=3,  sticky="w",padx=3, pady=3)
four.grid(row=5, column=1, sticky="w",padx=3, pady=3)
five.grid(row=5, column=2, sticky="w",padx=3, pady=3)
six.grid(row=5, column=3,  sticky="w",padx=3, pady=3)
seven.grid(row=6, column=1, sticky="w",padx=3, pady=3)
eight.grid(row=6, column=2, sticky="w",padx=3, pady=3)
nine.grid(row=6, column=3,  sticky="w",padx=3, pady=3)
zero.grid(row=7, column=2, sticky="w",padx=3, pady=3)
dot.grid(row=7, column=3, sticky="w",padx=3, pady=3)
divide.grid(row=3, column=4, sticky="w",padx=3, pady=3)
multiply.grid(row=4, column=4, sticky="w",padx=3, pady=3)
subtract.grid(row=5, column=4,  sticky="w",padx=3, pady=3)
add.grid(row=6, column=4,  sticky="w",padx=3, pady=3)
equal.grid(row=7, column=4,  sticky="w",padx=3, pady=3)
clear.grid(row=3, column=3,  sticky="w",padx=3, pady=3)
window.mainloop()

