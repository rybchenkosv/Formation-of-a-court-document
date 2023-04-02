from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

languages = ["Python", "JavaScript", "Java", "C#"]
selected_language = StringVar()  # по умолчанию ничего не выборанно

header = ttk.Label(text="Выберите язык")
header.grid()


def select():
    header.config(text=f"Выбран {selected_language.get()}")
    if selected_language.get() == 'Java':
        print(1)


for lang in languages:
    lang_btn = ttk.Radiobutton(text=lang, value=lang, variable=selected_language, command=select)
    lang_btn.grid()

root.mainloop()
