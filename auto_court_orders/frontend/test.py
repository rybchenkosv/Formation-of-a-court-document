from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

#FUNCTION OF DISPLAYING THE MANAGEMENT COMPANY TO WHICH THE SELECTED HOUSE BELONS
def RESPONSIBLE_MANAGEMENT_COMPANY(event):
    # получаем выделенный элемент
    selection = # НЕОБХОДИМО ПРОПИСАТЬ ЗАВИСИМОСТЬ ВЫБОРА УПРАВЛЯЮЩЕЙ КОМПАНИИ
    label["text"] = f"вы выбрали: {selection}"


languages = ["Python", "C#", "Java", "JavaScript"]
label = ttk.Label()
label.pack(anchor=NW, fill=X, padx=5, pady=5)

combobox = ttk.Combobox(values=languages, state="readonly")
combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
combobox.bind("<<ComboboxSelected>>", RESPONSIBLE_MANAGEMENT_COMPANY)

root.mainloop()


