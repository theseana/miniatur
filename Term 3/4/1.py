import tkinter as tk
import datetime
import time

def toTime(sec):
    return str(datetime.timedelta(seconds=sec))


def b1():
    global t1
    while True:
        timer1.set(toTime(t1))
        time.sleep(1)
        t1 = t1 - 1

def b2():
    pass


root = tk.Tk()

t1 = 120
t2 = 120

root.config(bg='#94f2df')
root.title('Maedeh')
root.resizable(0, 0)
m = {
'font': ('verdana', 15),
'bg': '#94f2df',
}
cb = {
'font': ('verdana', 15),
'bg': '#ffbff5',
}

timer1 = tk.StringVar()
timer1.set("0:02:00")
tk.Label(root, textvariable=timer1, cnf=m).grid(row=0, column=0)

timer2 = tk.StringVar()
timer2.set("0:02:00")
tk.Label(root, textvariable=timer2, cnf=m).grid(row=0, column=1)

tk.Button(root, text="pause", cnf=cb , command=b1).grid(row=1, column=0)
tk.Button(root, text="pause", cnf=cb , command=b2).grid(row=1, column=1)

b1()

root.mainloop()