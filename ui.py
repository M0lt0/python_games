from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=100, row=10)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=20, row=10)
root.mainloop()