import tkinter as tk

mainwin = tk.Tk()

def f():
    x = e1.get()
    l1.config(text = x)
    print(x)
    
b1 = tk.Button(master = mainwin, text = "Afiseaza", command = f)
e1 = tk.Entry(master = mainwin, text = "Text initial")
l1 = tk.Label(master = mainwin, text = "text label")

b1.grid(row=0, column=0)
e1.grid(row=0, column=1)
l1.grid(row=1, column=0, columnspan=2)

mainwin.mainloop()
