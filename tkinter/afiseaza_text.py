import tkinter as tk

mainwin = tk.Tk()

b1 = tk.Button(master = mainwin, text = "Afiseaza", command= lambda: print(e1.get()))
e1 = tk.Entry(master = mainwin, text = "Text initial")

b1.grid(row=0, column=0)
e1.grid(row=0, column=1)

mainwin.mainloop()
