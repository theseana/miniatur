import tkinter as tk

def say():
    m.config(text="WELCOME " + e.get())

root = tk.Tk()
root.title('Strawberry Cake')
root.config(bg='#0394fc')

m = tk.Label(root, text='WELCOME!', bg='#0394fc', fg='orange',
    font=('Comic Sans MS', 20))
m.pack()

e =tk.Entry(root, bg='#0394fc', fg='orange', font=('times', 20))
e.pack()

b = tk.Button(root, text="Click Here", command=say, bg='#0394fc',
    fg='orange', font=('Comic Sans MS', 20))
b.pack()

# root.mainloop()