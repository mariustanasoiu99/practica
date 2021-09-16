import tkinter as tk    #importa pachetul tkinter, care pune la dispozitie interfata grafica Tk.

mainwin = tk.Tk()       #creeaza fereastra principala.

b1 = tk.Button(master = mainwin, text = "Salut", command = lambda: print("Afisez ceva"))    #creeaza butonul
b1.pack()               #afiseaza butonul

mainwin.mainloop()      #porneste bucla de evenimente.
