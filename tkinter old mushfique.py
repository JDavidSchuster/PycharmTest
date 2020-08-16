import tkinter as tk

sample = []

window = tk.Tk()
window.rowconfigure(18, minsize=150, weight=1)
window.columnconfigure(18, minsize=150, weight=1)

w1 = tk.Spinbox(master=window, from_=0, to=9, width=10, state="readonly")
w1.grid(row=5, column=6, padx=10, pady=10)

w2 = tk.Spinbox(master=window, from_=0, to=9, width=10, state="readonly")
w2.grid(row=6, column=7, padx=10, pady=10)

spins = [w1, w2]

def setvalue():

    for i in range (2):
        sample.append(int(spins[i].get()))
    window.destroy()
    return

button = tk.Button(window, text="Get value", command=setvalue)
button.grid(row=8, column=9, padx=10, pady=10)

window.mainloop()

print(sample)