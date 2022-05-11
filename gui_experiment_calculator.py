from tkinter import *
from math import * 

root = Tk()


def show_frame(frame):
    frame.tkraise()

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)

for frame in (frame1, frame2, frame3, frame4):
    frame.grid(row=0, column=0, sticky='nsew')


#=============================================================================================================================================================================================
#frame 1 code: Decimal Calculator

#frame1_title = Label(frame1, text="Decimal Calculator")
#frame1_title.grid(row=6, column= 0)

my_input_text = []

e = Entry(frame1, width=80)
e.grid(row=0, column=5, padx=40, pady=10)

my_text = Text(frame1, width=60, height=20)
my_text.grid(row=1, rowspan=5, column=5, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    if current == "sqrt(":
        sqroot = current + number
        e.insert(0, sqroot)
    else:
        e.insert(0, current + number)
    return

def button_clear():
    e.delete(0, END)

def button_clear_memory():
    my_text.delete(1.0, END)
    i = 0
    while len(my_input_text) != 0:
        my_input_text.pop(0)

def sc(event):
    key = event.widget
    text=key['text']
    no = e.get()
    result = ''
    
    if text == '+':
        result = str(float(no))
    if text == '-':
        result = str(float(no))
    if text == '*':
        result = str(float(no))
    if text == '/':
        result = str(float(no))
    if text == 'sqrt(':
        result = str(float(no))
    if text == '**2':
        result = str(float(no))
    
    e.delete(0, END)
    e.insert(0, result)



    
def button_equal():
    current = e.get()
    ans = eval(current)
    e.delete(0, END)
    my_text.delete(1.0, END)
    e.delete(0, END)
    my_input_text.append(str(current) + "=" + str(ans))
    i = 0
    while i < len(my_input_text):
        my_text.insert(1.0, my_input_text[i] + "\n")
        i += 1
    

    

    
    
#=============================================================================================================================================================================================
#define Buttons


button_1 = Button(frame1, text="1", padx=40, pady=20, command=lambda: button_click("1"))
button_2 = Button(frame1, text="2", padx=40, pady=20, command=lambda: button_click("2"))
button_3 = Button(frame1, text="3", padx=40, pady=20, command=lambda: button_click("3"))
button_4 = Button(frame1, text="4", padx=40, pady=20, command=lambda: button_click("4"))
button_5 = Button(frame1, text="5", padx=40, pady=20, command=lambda: button_click("5"))
button_6 = Button(frame1, text="6", padx=40, pady=20, command=lambda: button_click("6"))
button_7 = Button(frame1, text="7", padx=40, pady=20, command=lambda: button_click("7"))
button_8 = Button(frame1, text="8", padx=40, pady=20, command=lambda: button_click("8"))
button_9 = Button(frame1, text="9", padx=40, pady=20, command=lambda: button_click("9"))
button_0 = Button(frame1, text="0", padx=40, pady=20, command=lambda: button_click("0"))
button_dot = Button(frame1, text= ".", padx= 40, pady=20, command=lambda: button_click("."))

button_add = Button(frame1, text="+", padx=39, pady=20, command=lambda: button_click("+"))
button_subtract = Button(frame1, text="-", padx=39, pady=20, command=lambda: button_click("-"))
button_multiply = Button(frame1, text="*", padx=39, pady=20, command=lambda: button_click("*"))
button_divide = Button(frame1, text="/", padx=39, pady=20, command=lambda: button_click("/"))
button_squareroot = Button(frame1, text="sqrt", padx=33, pady=20, command=lambda: button_click("sqrt("))
button_square = Button(frame1, text="x^2", padx=33, pady=20, command=lambda: button_click("**2"))
button_paranthesis_left = Button(frame1, text="(", padx=17, pady=20, command=lambda: button_click("("))
button_paranthesis_right = Button(frame1, text=")", padx=17, pady=20, command=lambda: button_click(")"))

button_equal = Button(frame1, text="=", padx=38, pady=20, command=button_equal)
button_clear = Button(frame1, text="Clear", padx=28, pady=20, command=button_clear)
button_clear_memory = Button(frame1, text="Clear Memory", padx=6, pady=20, command=button_clear_memory)

button_hex = Button(frame1, text="Hex calc", padx=20, pady=20, command=lambda: show_frame(frame4)) # goes to frame 4, aka the hexadecimal calculator
button_oct = Button(frame1, text="Oct calc", padx=20, pady=20, command=lambda: show_frame(frame3)) # goes to frame 3, aka the octal calculator
button_bin = Button(frame1, text="Bin calc", padx=22, pady=20, command=lambda: show_frame(frame2)) # goes to frame 2, aka the binary calculator

#===============================================================================================================================================================================================
#Put the buttons on the screen

button_squareroot.grid(row=0, column=0)
button_square.grid(row=0, column=1)
button_paranthesis_left.grid(row=0, column=2)
button_paranthesis_right.grid(row=0, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2, columnspan=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2, columnspan=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2, columnspan=2)

button_0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)

button_add.grid(row=4, column=2, columnspan=2)
button_subtract.grid(row=3, column=4)
button_multiply.grid(row=2, column=4)
button_divide.grid(row=1, column=4)

button_clear.grid(row=0, column=4)
button_equal.grid(row=4, column=4)

button_bin.grid(row=5, column=0)
button_oct.grid(row=5, column=1)
button_hex.grid(row=5, column=2, columnspan=2)
button_clear_memory.grid(row=5, column=4)

#=============================================================================================================================================================================================
# Frame 2 code

my_input_text2 = []

e2 = Entry(frame2, width=80)
e2.grid(row=0, column=4, padx=40, pady=5)

my_text2 = Text(frame2, width=60, height=8)
my_text2.grid(row=1, rowspan=2, column=4, pady=5)

def frame2_button_click(number):
    current2 = e2.get()
    e2.delete(0, END)
    e2.insert(0, current2 + number)
    return

def frame2_button_clear():
    e2.delete(0, END)

def frame2_button_clear_memory():
    my_text2.delete(1.0, END)
    i = 0
    while len(my_input_text2) != 0:
        my_input_text2.pop(0)

def frame2_sc(event):
    key = event.widget
    text2=key['text']
    no = e2.get()
    result2 = ''
    
    if text2 == '+':
        result2 = str(bin(no))
    if text2 == '-':
        result2 = str(bin(no))
    if text2 == '*':
        result2 = str(bin(no))
    if text2 == '/':
        result2 = str(bin(no))
    
    e2.delete(0, END)
    e2.insert(0, result)



    
def frame2_button_equal():
    current2 = e2.get()
    current2_str = str(current2)

    x1 = 1
    x2 = 1
    i1 = 0
    i2= 0
    nr = 1
    
    current2_1 = []
    current2_2 = []

    count = 0

    while count < len(current2_str):
        if current2_str[count] == "+":
            a = count-1
            b = count+1
            global var1
            var1 = current2_str[0:current2_str[a]]
            global var2
            var2 = current2_str[current2_str[b]:len(current2_str)]
        else:
            count += 1
        

    while i1 < len(var1):
        index1 = len(var1) - x1
        if var1[i1]== "1":
            var = 2**(index1)
            current2_1.append(var)
            i1 += 1
            x1 += 1
        else:
            i1 += 1
            x1 += 1
    
    while i2 < len(var2):
        index2 = len(var2) - x2
        if var2[i2]== "1":
            var = 2**(index2)
            current2_2.append(var)
            i2 += 1
            x2 += 1
        else:
            i2 += 1
            x2 += 1

    nr1 = sum(current2_1)
    nr2 = sum(current2_2)
    ans = nr1+nr2
    ans_x = bin(ans)
    ans_bin = str(ans_x[2:len(ans_x)])



    ans2 = current2
    e2.delete(0, END)
    my_text2.delete(1.0, END)
    e2.delete(0, END)
    my_input_text2.append(str(current2) + "=" + str(ans_bin) + "|" + str(nr1) + str(nr2) + "=" + str(ans))
    i = 0
    while i < len(my_input_text2):
        my_text2.insert(1.0, my_input_text2[i] + "\n")
        i += 1


# Defined Buttons
frame2_button_0 = Button(frame2, text="0", padx=40, pady=20, command=lambda: frame2_button_click("0"))
frame2_button_1 = Button(frame2, text="1", padx=40, pady=20, command=lambda: frame2_button_click("1"))

frame2_button_add = Button(frame2, text="+", padx=39, pady=20, command=lambda: frame2_button_click("+"))
frame2_button_subtract = Button(frame2, text="-", padx=39, pady=20, command=lambda: frame2_button_click("-"))
frame2_button_multiply = Button(frame2, text="*", padx=39, pady=20, command=lambda: frame2_button_click("*"))
frame2_button_divide = Button(frame2, text="/", padx=39, pady=20, command=lambda: frame2_button_click("/"))

frame2_button_equal = Button(frame2, text="=", padx=38, pady=20, command=frame2_button_equal)
frame2_button_clear = Button(frame2, text="Clear", padx=28, pady=20, command=frame2_button_clear)
frame2_button_clear_memory = Button(frame2, text="Clear Memory", padx=6, pady=20, command=frame2_button_clear_memory)

frame2_button_hex = Button(frame2, text="Hex Calc", padx=22, pady=20, command=lambda: show_frame(frame4)) # goes to frame 4, aka the hexadecimal calculator
frame2_button_oct = Button(frame2, text="Oct Calc", padx=20, pady=20, command=lambda: show_frame(frame3)) # goes to frame 3, aka the octal calculator
frame2_button_dec = Button(frame2, text="Dec Calc", padx=20, pady=20, command=lambda: show_frame(frame1)) # goes to frame 2, aka the decimal calculator


# Puts Buttons on the screen
frame2_button_0.grid(row=0, column=2)
frame2_button_1.grid(row=1, column=2)

frame2_button_add.grid(row=0, column=0)
frame2_button_subtract.grid(row=0, column=1)
frame2_button_multiply.grid(row=1, column=0)
frame2_button_divide.grid(row=1, column=1)

frame2_button_equal.grid(row=1, column=3)
frame2_button_clear.grid(row=0, column=3)
frame2_button_clear_memory.grid(row=2, column=3)

frame2_button_dec.grid(row=2, column=0)
frame2_button_oct.grid(row=2, column=1)
frame2_button_hex.grid(row=2, column=2)

#=============================================================================================================================================================================================
# function that shows the frame
show_frame(frame1)

root.mainloop()
