from tkinter import Tk, Button, Frame, StringVar
from tkinter.ttk import Combobox


options = {'A': [1, 2, 3], 'B': [4, 5, 6]}


def get_var_1(event):
    value = cb1_var.get()
    cb2_var.set(options[value][0])
    cb2.config(values=options[value])


def get_info():
    print(cb1_var.get(), cb2_var.get())


root = Tk()

cb_frame = Frame(root)
cb_frame.pack(side='left')

cb1_values = list(options.keys())

cb1_var = StringVar()
cb1_var.set(cb1_values[0])
cb1 = Combobox(cb_frame, values=list(options.keys()), textvariable=cb1_var)
cb1.pack(side='top')
cb1.bind('<<ComboboxSelected>>', get_var_1)


cb2_var = StringVar()
cb2_var.set(options[cb1_values[0]][0])
cb2 = Combobox(cb_frame, values=options[cb1_values[0]], textvariable=cb2_var)
cb2.pack(side='bottom')


btn_frame = Frame(root)
btn_frame.pack(side='right')
Button(btn_frame, text='Confirm', command=get_info).pack()


root.mainloop()