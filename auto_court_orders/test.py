from tkinter import *
from tkinter import ttk


def check(*args):
    print(name)
    if len(name.get()) == 10:
        if '.' in str(name.get) and len(str(name.get()).replace('.',"")) == 8:
            result.set("")
    else:
        result.set("Введите корректную дату \ndd.mm.yyyy")

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

name = StringVar()
result = StringVar()

name_entry = ttk.Entry(textvariable=name)
name_entry.pack(padx=5, pady=5, anchor=NW)

check_label = ttk.Label(textvariable=result)
check_label.pack(padx=5, pady=5, anchor=NW)


# отслеживаем изменение значения переменной name
name.trace_add("write", check)

root.mainloop()
