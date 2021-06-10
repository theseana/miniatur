import tkinter as tk
from tkinter import ttk

root = tk.Tk()

style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='en')
#we  wn  ws  se sw sn  ns ne nw es en ew
notebook = ttk.Notebook(root, style='lefttab.TNotebook')
f1 = tk.Frame(notebook, bg='red', width=200, height=200)
f2 = tk.Frame(notebook, bg='blue', width=200, height=200)
notebook.add(f1, text='Frame 1')
notebook.add(f2, text='Frame 2')
notebook.pack()

root.mainloop()