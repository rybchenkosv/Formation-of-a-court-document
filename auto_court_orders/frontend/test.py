from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")


def selected(event):
    # получаем выделенный элемент
    selection = combobox.get()
    print(selection)
    label["text"] = f"вы выбрали: {selection}"


languages = ["Python", "C#", "Java", "JavaScript"]
label = ttk.Label()
label.pack(anchor=NW, fill=X, padx=5, pady=5)

combobox = ttk.Combobox(values=languages, state="readonly")
combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
combobox.bind("<<ComboboxSelected>>", selected)

root.mainloop()