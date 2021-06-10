import tkinter as tk


root = tk.Tk()
root.config(bg='#94f2df')

c = {
    'font': ('times', 21),
    'bg': '#94f2df',
}
cb = {
    'font': ('times', 21),
    'bg': '#ffbff5',
}
tk.Label(root, text="Weight:", cnf=c).grid(row=0, column=0)
tk.Label(root, text="Hieght:", cnf=c).grid(row=1, column=0)

e1 = tk.Entry(root, cnf=c)
e1.grid(row=0, column=1)
e2 = tk.Entry(root, cnf=c)
e2.grid(row=1, column=1)

frame = tk.Frame()
frame.grid(row=2, column=0, columnspan=2)

tk.Button(frame, text="BMI", cnf=cb).grid(row=2, column=0)
tk.Button(frame, text="Cancel", cnf=cb).grid(row=2, column=1)

root.mainloop()