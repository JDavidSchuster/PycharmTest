import tkinter as tk
import numpy as np

inputs = []
widget = []
from sdk3 import sdk3_main

widget = []

win = tk.Tk()
win.geometry('900x900')

for x in range(9):
    widget.append([])

    for y in range(9):
        a = 0.1 * x + .05
        b = 0.1 * y + .05

        widget[x].append(tk.Entry(master=win, width=6))
        widget[x][y].place(relx=a, rely=b)


def data(i):
    inputs.append(i)

    print(inputs)


sample = []


def setvalue():
    for i, spinbox_list in enumerate(widget):
        sample.append([])
        for spinbox in spinbox_list:
            sample[i] = []
            sample[i].append(spinbox.get())
    win.destroy()
    return


button = tk.Button(win, text="Get value", command=setvalue)
button.grid(row=8, column=9, padx=10, pady=10)

win.mainloop()
sdk3_main(sample)