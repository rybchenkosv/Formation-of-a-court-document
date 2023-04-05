from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

# создаем пару фреймвов
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)

# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Создать судебный приказ")
notebook.add(frame2, text="Заявление в приставы")

def window1(h):
    BUTTON_ADD_DEBTOR = Button(h, text="Добавить должника", font=("Arial", 8, 'bold'), bg='#79abfc')
    BUTTON_ADD_DEBTOR.pack()

class hrt:
    window1(frame1)

class hrt1:
    window1(frame2)

root.mainloop()