from tkinter import *

root = Tk()
root.title("Calculator")
# root.geometry("360x240")

# Input Field
i = 0
display = Entry(root)
display.grid(row=0, columnspan=4, sticky=W + E)

# Numeric Buttons
Button(root, text="1", command=lambda: numInsertion("1")).grid(row=4, column=0, sticky=W + E, padx=2, pady=2)
Button(root, text="2", command=lambda: numInsertion("2")).grid(row=4, column=1, sticky=W + E, padx=2, pady=2)
Button(root, text="3", command=lambda: numInsertion("3")).grid(row=4, column=2, sticky=W + E, padx=2, pady=2)
Button(root, text="4", command=lambda: numInsertion("4")).grid(row=3, column=0, sticky=W + E, padx=2, pady=2)
Button(root, text="5", command=lambda: numInsertion("5")).grid(row=3, column=1, sticky=W + E, padx=2, pady=2)
Button(root, text="6", command=lambda: numInsertion("6")).grid(row=3, column=2, sticky=W + E, padx=2, pady=2)
Button(root, text="7", command=lambda: numInsertion("7")).grid(row=2, column=0, sticky=W + E, padx=2, pady=2)
Button(root, text="8", command=lambda: numInsertion("8")).grid(row=2, column=1, sticky=W + E, padx=2, pady=2)
Button(root, text="9", command=lambda: numInsertion("9")).grid(row=2, column=2, sticky=W + E, padx=2, pady=2)
Button(root, text="0", command=lambda: numInsertion("0")).grid(row=5, column=1, sticky=W + E, padx=2, pady=2)

# Operator Buttons
Button(root, text="+", command=lambda: operatorInsert("+")).grid(row=1, column=3, sticky=W + E, padx=2, pady=2)
Button(root, text="-", command=lambda: operatorInsert("-")).grid(row=2, column=3, sticky=W + E, padx=2, pady=2)
Button(root, text="*", command=lambda: operatorInsert("*")).grid(row=3, column=3, sticky=W + E, padx=2, pady=2)
Button(root, text="/", command=lambda: operatorInsert("/")).grid(row=4, column=3, sticky=W + E, padx=2, pady=2)
Button(root, text="^", command=lambda: operatorInsert("**")).grid(row=1, column=0, sticky=W + E, padx=2, pady=2)

# Other Buttons
Button(root, text="=", command=lambda: Operation()).grid(row=5, column=2, columnspan=2, sticky=W + E, padx=2, pady=2)
Button(root, text="+/-", command=lambda: modulus()).grid(row=5, column=0, sticky=W + E, padx=2, pady=2)
Button(root, text="AC", command=lambda: clearAll()).grid(row=1, column=1, sticky=W + E, padx=2, pady=2)
Button(root, text="<-", command=lambda: erase()).grid(row=1, column=2, sticky=W + E, padx=2, pady=2)


# Operation Functions
def modulus():
    global i
    old_string = display.get()
    if old_string[0] == "-":
        new_string = old_string[1:]
        clearAll()
        display.insert(i, new_string)
    else:
        display.insert(0, "-")
        new_string = display.get()
    i = len(new_string)


def erase():
    global i
    old_string = display.get()
    new_string = old_string[:-1]
    clearAll()
    display.insert(0, new_string)
    i = len(new_string)


def numInsertion(text):
    global i
    display.insert(i, text)
    i += 1


def operatorInsert(oper):
    global i
    Operation()
    length = len(oper)
    display.insert(i, oper)
    i += length


def Operation():
    global i
    txt = display.get()
    sol = eval(txt)
    clearAll()
    display.insert(i, sol)
    sol = str(sol)
    i = len(sol)


def clearAll():
    global i
    display.delete(0, i)
    i = 0


root.mainloop()
