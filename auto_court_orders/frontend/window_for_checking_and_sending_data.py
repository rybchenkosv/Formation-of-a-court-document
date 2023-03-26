from tkinter import Tk, Button, Frame, StringVar
from tkinter import *
from tkinter.ttk import Combobox, Label, Treeview

# ФУНКЦИЯ ПРОВЕРКИ ДАННЫХ И СОЗДАНИЯ ПРИКАЗА
def VALIDATION_AND_DATA_GENERATION_FUNCTION():

    window = Tk()
    window.title("Проверьте введенные данные")
    window.geometry("250x200")

    s1 = Label(window, text="Проверьте введенные данные", font=("Arial", 10))
    s1.grid(row=0, column=0)

    s2 = Label(window, text="Адрес должника(-ов)", font=("Arial", 10))
    s2.grid(row=1, column=0)

    s3 = Label(window, text='111', font=("Arial", 10))
    s3.grid(row=1, column=1)