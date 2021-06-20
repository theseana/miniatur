from tkinter import *
import json
from tkinter import messagebox

def read_json(address):
    with open(address) as file:
        return json.load(file)


def write_json(address, data):
    with open(address, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def register():
    def register_close():
        register_top.destroy()
        l_r_top.deiconify()

    def register_confirm():
        person = {}
        person['username'] = r_username.get()
        person['fullname'] = r_fullname.get()
        person['card'] = r_card.get()
        person['password'] = r_password.get()
        person['dob'] = r_bod.get()
        person['balance'] = 1000000

        file_json = read_json('list.json')
        file_json.append(person)
        r_username.set('')
        r_fullname.set('')
        r_card.set('')
        r_password.set('')
        r_bod.set('')
        write_json('list.json', file_json)

    l_r_top.withdraw()
    register_top = Toplevel()

    Label(register_top, text='Username').grid(row=0, column=0)
    r_username = StringVar()
    Entry(register_top, textvariable=r_username).grid(row=0, column=1)

    Label(register_top, text='Full Name').grid(row=1, column=0)
    r_fullname = StringVar()
    Entry(register_top, textvariable=r_fullname).grid(row=1, column=1)

    Label(register_top, text='Card Num.').grid(row=2, column=0)
    r_card = StringVar()
    Entry(register_top, textvariable=r_card).grid(row=2, column=1)

    Label(register_top, text='Password').grid(row=3, column=0)
    r_password = StringVar()
    Entry(register_top, textvariable=r_password).grid(row=3, column=1)

    Label(register_top, text='D.O.B.').grid(row=4, column=0)
    r_bod = StringVar()
    Entry(register_top, textvariable=r_bod).grid(row=4, column=1)

    Button(register_top, text="Register", bg="gray", activebackground="pink",
           activeforeground="white", highlightthickness=0,
           command=register_confirm).grid(row=5, column=0, columnspan=2, sticky='NESW')
    Button(register_top, text="Back", bg="gray", activebackground="pink",
           activeforeground="white", highlightthickness=0, command=register_close).grid(row=6, column=0, columnspan=2,
                                                                                        sticky='NESW')


def login():
    def login_close():
        login_top.destroy()
        l_r_top.deiconify()

    def login_confirm():
        file_json = read_json('list.json')
        for p in file_json:
            if p['username'] == l_username.get():
                if p['password'] == l_password.get():
                    p_index.set(file_json.index(p))
                    login_top.deiconify()
                    main_menu()

                    return None
                else:
                    messagebox.showerror('Error', 'your password is wrong')
                    return None
            # else:
            #     messagebox.showerror('Eror', 'your username is wrong')
            #     return None

    l_r_top.withdraw()
    login_top = Toplevel()
    Label(login_top, text='Username').grid(row=0, column=0)
    l_username = StringVar()
    Entry(login_top, textvariable=l_username).grid(row=0, column=1)

    Label(login_top, text='Password').grid(row=2, column=0)
    l_password = StringVar()
    Entry(login_top, textvariable=l_password).grid(row=2, column=1)

    Button(login_top, text="login", bg="gray", activebackground="pink",
           activeforeground="white", highlightthickness=0,
           command=login_confirm).grid(row=4, column=0, columnspan=2, sticky='NESW')
    Button(login_top, text="Back", bg="gray", activebackground="pink",
           activeforeground="white", highlightthickness=0, command=login_close
           ).grid(row=5, column=0, columnspan=2, sticky='NESW')


def main_menu():
    file_json = read_json('list.json')
    main_name.set(file_json[p_index.get()]['fullname'])
    main_balance.set(file_json[p_index.get()]['balance'])
    root.deiconify()


root = Tk()
p_index = IntVar()
root.config(bg='black')
root.resizable(0, 0)
lframe = Frame(root, bg="black", width=200, height=450)
lframe.grid(row=0, column=0, sticky='NESW', padx=(15, 15), pady=(0, 15))
rframe = Frame(root, bg="black", width=350, height=450)
rframe.grid(row=0, column=1, padx=(0, 15))
# ###
Label(lframe, text='ATM', fg='white', bg="black",
      font=('Times', 20)).grid(row=0, column=0, pady=15)
Label(lframe, text='Welcome', fg='white', bg="black").grid(row=1, column=0)
main_name = StringVar()
main_name.set('Maedeh Ashouri')
Label(lframe, textvariable=main_name, fg='white', bg="black").grid(row=2, column=0)

Label(lframe, text='Balance', fg='white', bg='black',
      font=('Times', 15)).grid(row=3, column=0, pady=(20, 0))
main_balance = StringVar()
main_balance.set('$1000000')
Label(lframe, textvariable=main_balance, fg='white', bg='black', font=('Times', 10)).grid(row=4, column=0)
# ###
Button(rframe, text="Get Cash", bg="gray", activebackground="pink",
       activeforeground="white", highlightthickness=0).grid(row=1, column=0, sticky='NESW')
Button(rframe, text="Deposite", bg="gray", activebackground="pink",
       activeforeground="white", highlightthickness=0).grid(row=1, column=1, sticky='NESW')
Button(rframe, text="Payments", bg="gray", activebackground="pink",
       activeforeground="white", highlightthickness=0).grid(row=2, column=0, sticky='NESW')
Button(rframe, text="Account Setting", bg="gray", activebackground="pink",
       activeforeground="white", highlightthickness=0).grid(row=2, column=1, sticky='NESW')
Button(rframe, text="Credite Card", bg="gray", activebackground="pink",
       activeforeground="white", highlightthickness=0).grid(row=3, column=0, sticky='NESW')
Button(rframe, text="other", bg="gray", activebackground="pink",
       activeforeground="white", highlightthickness=0).grid(row=3, column=1, sticky='NESW')
Button(rframe, text="Quick Cash", bg="red", activebackground="pink",
       activeforeground="white", highlightthickness=0).grid(row=4, column=0, columnspan=2, sticky='NESW')
# ###
root.withdraw()
l_r_top = Toplevel()
Label(l_r_top, text="Miniator Bank").grid(row=0, column=0)

Button(l_r_top, text="Register", bg="gray", activebackground="pink",
       activeforeground="white", highlightthickness=0, command=register).grid(row=1, column=0)
Button(l_r_top, text="Login", bg="gray", activebackground="pink",
       activeforeground="white", highlightthickness=0, command=login).grid(row=2, column=0)
Button(l_r_top, text="Close", bg="gray", activebackground="pink",
       activeforeground="white", highlightthickness=0, command=root.destroy).grid(row=3, column=0)

root.mainloop()
