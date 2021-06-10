import tkinter as tk
import tkinter.ttk as ttk


def cnt1_callback(a, b ,c):
    if cnt1.get() != '0':
        factor['Garlic'] = cnt1.get()
    else:
        factor.pop('Garlic', None)


def cnt2_callback(a, b ,c):
    if cnt2.get() != '0':
        factor['Vegetarian'] = cnt2.get()
    else:
        factor.pop('Vegetarian', None)


def cnt1_s_callback(a, b ,c):
    if cnt1_s.get() != '0':
        factor['Bruschetta'] = cnt1_s.get()
    else:
        factor.pop('Bruschetta', None)


def cnt1_d_callback(a, b ,c):
    if cnt1_d.get() != '0':
        factor['Orange'] = cnt1_d.get()
    else:
        factor.pop('Orange', None)


def apply():
    msg = msgTitle +'\n\n'
    index = 1
    for food in factor:
        msg += f'{index}- {food}\t\t{factor[food]}\n'
        index += 1
    final = f'Total price: {get_price()}$'
    msg += final
    textTitle.delete("1.0","end")
    textTitle.insert('insert', msg)

def get_price():
    p = 0
    for food in factor:
        p += factor[food] * price[food]
    return p


factor = {}
price = {
    'Garlic': 7,
    'Vegetarian': 5,
    'Bruschetta': 4,
    'Orange': 2,
}
root = tk.Tk()
root.config(bg="purple")

frame = tk.Frame()
frame.grid(row=0, column=0, padx=10, pady=10)

leftFrame = tk.Frame(frame)
leftFrame.grid(row=0, column=0)
rightFrame = tk.Frame(frame)
rightFrame.grid(row=0, column=1)

msgTitle = "Table: 0 | OrderNumber: #452154"
textTitle = tk.Text(leftFrame, height=20, width=52)
textTitle.grid(row=0, column=0, sticky='nsew')
textTitle.insert('insert', msgTitle)

tk.Button(leftFrame, text="Apply", command=apply).grid(row=1, column=0)

s = ttk.Style()
s.configure('TNotebook', tabposition='en')

box = ttk.Notebook(rightFrame)
tab1 = tk.Frame(root)
tab2 = tk.Frame(root)
tab3 = tk.Frame(root)
box.add(tab1, text="Pizza       ")
box.add(tab2, text="Sandwich")
box.add(tab3, text="Drink       ")
box.grid(row=0, column=0)
# ############################## Pizza ############################# #
frm1 = tk.Frame(tab1)
frm1.grid(row=0, column=0)
img1 = tk.PhotoImage(file='pizza-garlic.png').subsample(2)
tk.Label(frm1, image=img1).grid(row=0, column=0)
tk.Label(frm1, text="Garlic").grid(row=1, column=0)
cnt1 = tk.IntVar()
tk.Spinbox(frm1, textvariable=cnt1, from_=0, to=20, width=2, state='readonly').grid(row=2, column=0)
cnt1.trace('w', cnt1_callback)
# --------- #
frm2 = tk.Frame(tab1)
frm2.grid(row=0, column=1)
img2 = tk.PhotoImage(file='pizza-vegetarian.png').subsample(2)
tk.Label(frm2, image=img2).grid(row=0, column=0)
tk.Label(frm2, text="Vegetarian").grid(row=1, column=0)
cnt2 = tk.IntVar()
tk.Spinbox(frm2, textvariable=cnt2, from_=0, to=20, width=2, state='readonly').grid(row=2, column=0)
cnt2.trace('w', cnt2_callback)

# --------- #
# frm3 = tk.Frame(tab1)
# frm3.grid(row=0, column=2)
# img3 = tk.PhotoImage(file='pizza-pepperoni.png').subsample(2)
# tk.Label(frm3, image=img3).grid(row=0, column=0)
# tk.Label(frm3, text="Pepperoni").grid(row=1, column=0)
# cnt3 = tk.StringVar()
# tk.Spinbox(frm3, textvariable=cnt3, from_=0, to=20, width=2, state='readonly').grid(row=2, column=0)
# cnt3.set('')
# cnt3.trace('w', cnt3_callback)
# # --------- #
# frm4 = tk.Frame(tab1)
# frm4.grid(row=1, column=0)
# img4 = tk.PhotoImage(file='pizza-pepperoni.png').subsample(2)
# tk.Label(frm4, image=img4).grid(row=0, column=0)
# tk.Label(frm4, text="Pepperoni").grid(row=1, column=0)
# cnt4 = tk.StringVar()
# tk.Spinbox(frm4, textvariable=cnt4, from_=0, to=20, width=2, state='readonly').grid(row=2, column=0)
# cnt4.set('')
# cnt4.trace('w', cnt4_callback)

# ################################################################## #
# ############################ Sandwich ############################ #
frm1_s = tk.Frame(tab2)
frm1_s.grid(row=0, column=0)
img1_s = tk.PhotoImage(file='bruschetta.png').subsample(2)
tk.Label(frm1_s, image=img1_s).grid(row=0, column=0)
tk.Label(frm1_s, text="Bruschetta").grid(row=1, column=0)
cnt1_s = tk.IntVar()
tk.Spinbox(frm1_s, textvariable=cnt1_s, from_=0, to=20, width=2, state='readonly').grid(row=2, column=0)
cnt1_s.trace('w', cnt1_s_callback)
# --------- #
# ################################################################## #
# ############################## Drink ############################# #
frm1_d = tk.Frame(tab3)
frm1_d.grid(row=0, column=0)
img1_d = tk.PhotoImage(file='orange.png').subsample(2)
tk.Label(frm1_d, image=img1_d).grid(row=0, column=0)
tk.Label(frm1_d, text="Orange").grid(row=1, column=0)
cnt1_d = tk.IntVar()
tk.Spinbox(frm1_d, textvariable=cnt1_d, from_=0, to=20, width=2, state='readonly').grid(row=2, column=0)
cnt1_d.trace('w', cnt1_d_callback)
# --------- #
# ################################################################## #

root.mainloop()