import tkinter as tk


def cal():
    if e1.get() and e2.get():
        w = float(e1.get())
        h = float(e2.get())
        bmi = w / (h * h)
        l1.config(text=f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            l1.config(bg="#87B1DB")
        elif 18.5 <= bmi < 24.9:
            l1.config(bg="#3DD365")
        elif 24.9 <= bmi < 29.9 : 
            l1.config(bg="#EDE133")
        elif 29.9 <= bmi < 34.9:
            l1.config(bg="#FD802E")
        elif bmi >= 34.9:
            l1.config(bg="#F95353")
        e1.config(bg="#94f2df")
        e2.config(bg="#94f2df")
    else:
        e1.config(bg="#F8B2B0")
        e2.config(bg="#F8B2B0")

root = tk.Tk()
root.config(bg='#94f2df')
root.title('Maedeh BMI Calculator')
root.resizable(0, 0)
c = {
    'font': ('times', 21),
    'bg': '#94f2df',
}
cb = {
    'font': ('times', 21),
    'bg': '#ffbff5',
}
l1 = tk.Label(root, text="BMI", cnf=c)
l1.grid(row=0, column=0, columnspan=2)
tk.Label(root, text="Weight(KG):", cnf=c).grid(row=1, column=0)
tk.Label(root, text="Hieght(M):", cnf=c).grid(row=2, column=0)

e1 = tk.Entry(root, cnf=c)
e1.grid(row=1, column=1)
e2 = tk.Entry(root, cnf=c)
e2.grid(row=2, column=1)

frame = tk.Frame()
frame.grid(row=3, column=0, columnspan=2)

tk.Button(frame, text="BMI", cnf=cb, command=cal).grid(row=2, column=0)
tk.Button(frame, text="Cancel", cnf=cb, command=root.destroy).grid(row=2, column=1)

root.mainloop()