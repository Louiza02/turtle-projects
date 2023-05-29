import tkinter as tk
from math import *


calcul = tk.Tk()
calcul.title("all_buttons")
textVar=tk.StringVar()

ent1 = tk.Entry(calcul,width=56, borderwidth=8, textvar=textVar)
ent1.grid(row=0,column=0,columnspan=5,padx=1,pady=5)


def createButton() :
    b0 = tk.Button(calcul, text="0", command=lambda: clickButton(0), height=2, width=5,borderwidth=8, background = "#f8c146")
    b1 = tk.Button(calcul, text="1", command=lambda: clickButton(1), height=2, width=5,borderwidth=8, background = "#f8c146") 
    b2 = tk.Button(calcul, text="2", command=lambda: clickButton(2), height=2, width=5,borderwidth=8, background = "#f8c146") 
    b3 = tk.Button(calcul, text="3", command=lambda: clickButton(3), height=2, width=5,borderwidth=8, background = "#f8c146") 
    b4 = tk.Button(calcul, text="4", command=lambda: clickButton(4), height=2, width=5,borderwidth=8, background = "#f8c146") 
    b5 = tk.Button(calcul, text="5", command=lambda: clickButton(5), height=2, width=5,borderwidth=8, background = "#f8c146") 
    b6 = tk.Button(calcul, text="6", command=lambda: clickButton(6), height=2, width=5,borderwidth=8, background = "#f8c146") 
    b7 = tk.Button(calcul, text="7", command=lambda: clickButton(7), height=2, width=5,borderwidth=8, background = "#f8c146") 
    b8 = tk.Button(calcul, text="8", command=lambda: clickButton(8), height=2, width=5,borderwidth=8, background = "#f8c146") 
    b9 = tk.Button(calcul, text="9", command=lambda: clickButton(9), height=2, width=5,borderwidth=8, background = "#f8c146") 
    
    bP1 = tk.Button(calcul, text="(", command=lambda: clickButton("("), height=2, width=5,borderwidth=8)
    bP2 = tk.Button(calcul, text=")", command=lambda: clickButton(")"), height=2, width=5,borderwidth=8)
    clear = tk.Button(calcul, text="C", command=clearButton, height=2, width=5,borderwidth=8, background = "#ff0000")
    add= tk.Button(calcul, text="+", command=lambda: clickButton("+"), height=2, width=5,borderwidth=8) 
    sub = tk.Button(calcul, text="-", command=lambda: clickButton("-"), height=2, width=5,borderwidth=8) 
    mult = tk.Button(calcul, text="*", command=lambda: clickButton("*"), height=2, width=5,borderwidth=8) 
    div = tk.Button(calcul, text="/", command=lambda: clickButton("/"), height=2, width=5,borderwidth=8) 
    equal = tk.Button(calcul, text="=", command=equalButton, height=2, width=5,borderwidth=8, background = "#72f846") 
    mod = tk.Button(calcul, text="%", command=lambda: clickButton("%"), height=2, width=5,borderwidth=8) 
    v = tk.Button(calcul, text=".", command=lambda: clickButton("."), height=2, width=5,borderwidth=8) 
    sqrt = tk.Button(calcul, text="√", command=lambda: clickButton("sqrt("), height=2, width=5,borderwidth=8) 
    sq = tk.Button(calcul, text="X²", command=lambda: clickButton('**2'), height=2, width=5,borderwidth=8) 
    M = tk.Button(calcul, text="M", command=lambda: clickButton('M'), height=2, width=5,borderwidth=8) 
    pi = tk.Button(calcul, text="π", command=lambda: clickButton("pi"), height=2, width=5,borderwidth=8)
    cos = tk.Button(calcul, text="cos", command=lambda: clickButton("cos("), height=2, width=5,borderwidth=8)
    sin = tk.Button(calcul, text="sin", command=lambda: clickButton("sin("), height=2, width=5,borderwidth=8)
    tan = tk.Button(calcul, text="tan", command=lambda: clickButton("tan("), height=2, width=5,borderwidth=8)
    log = tk.Button(calcul, text="log", command=lambda: clickButton("log("), height=2, width=5,borderwidth=8)
    e = tk.Button(calcul, text="e", command=lambda: clickButton("exp("), height=2, width=5,borderwidth=8)
    fact = tk.Button(calcul, text="X!", command=lambda: clickButton("fact("), height=2, width=5,borderwidth=8)
    abs = tk.Button(calcul, text="|X|", command=lambda: clickButton("abs("), height=2, width=5,borderwidth=8)
    
    
    all_buttons = [
        [cos,sin,tan, log, e],
        [fact, abs, sq, bP1, bP2],
        [b7, b8, b9,  div, clear],
        [b4, b5, b6,  mult, pi],
        [b1, b2, b3,  sub, sqrt],
        [v,  b0, mod, add, equal]
    ]

    Row = 1
    for button in all_buttons:
        Column=0
        for tk.Button in button:
            tk.Button.grid(row = Row,column = Column)
            Column += 1
        Row += 1



current_equal= ""

def clickButton(num): 
    current_equal=str(ent1.get())
    current_equal = current_equal + str(num) 
    textVar.set(current_equal) 


def equalButton(): 
    try:        
        current_equal=str(ent1.get())
        result = str(eval(current_equal)) 
        textVar.set(result) 
        current_equal = result

    except: 
        textVar.set(" error ") 
        current_equal = "" 
        

def clearButton(): 
    current_equal=str(ent1.get())
    current_equal = "" 
    textVar.set("") 


createButton()    
calcul.mainloop()