from tkinter import Tk, Button, Frame, StringVar, filedialog
from tkinter import *
from tkinter.ttk import Combobox, Label, Treeview, Notebook, Scrollbar, Radiobutton, Button
from auto_court_orders import Database
from tkcalendar import Calendar, DateEntry
from tkinter.messagebox import showwarning, showerror, showinfo, askyesno
from docxtpl import DocxTemplate
from ttkthemes import ThemedTk
from datetime import date
import datetime

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
d = [[1,'Иванов Иван Иванович','11.06.2020','', '+', '+'], [2,'Петров Петр Петрович','11.06.2020','', '+', '+'], [3,'Каренина Анна Васильевна','11.06.1990','', '+', '+']]
list_of_owner_in_the_absence = []
list_with_legal_representative = []


def WINDOW_FUNCTION_FOR_SELECTION_OF_LEGAL_REPRESENTATIVE(not_18_old,list_of_adults):
    def end_of_selection():
        if lang.get() == 'Свой вариант' and entry.get() != '':
            showinfo("Информация", f"Для несовершеннолетнего собственника {not_18_old} Вы выбрали законного представителя {entry.get()}")
        elif lang.get() == 'Свой вариант' and entry.get() == '':
            showerror(title="Ошибка", message="Вы не ввели ФИО законного представителя!")
            window_not_18_old.attributes('-topmost', True)
            window_not_18_old.attributes('-topmost', False)
        elif lang.get() == '':
            showerror(title="Ошибка", message="Вы никого не выбрали!")
            window_not_18_old.attributes('-topmost', True)
            window_not_18_old.attributes('-topmost', False)
        else:
            showinfo("Информация",f"Для несовершеннолетнего собственника {not_18_old} Вы выбрали законного представителя {lang.get()}")
            for i in d:
                if not_18_old == i[1]:
                    list_with_legal_representative.append([i[0],i[1],i[2],i[3]+f' в лице законного представителя {lang.get()}',i[4],i[5]])
                else:
                    list_with_legal_representative.append(i)
            print(list_with_legal_representative)
            window_not_18_old.destroy()


    window_not_18_old = ThemedTk(theme="breeze")
    window_not_18_old.title("Укажите законного представителя")
    window_not_18_old.geometry("500x440")
    window_not_18_old.resizable(False, False)

    lang = StringVar(window_not_18_old)  # по умолчанию будет выбран элемент с value=java

    LABEL = Label(window_not_18_old, text=f"Укажите законного представителя для {not_18_old}",
                  font=("Arial", 10, 'bold'))
    LABEL.grid()

    for i in range(len(list_of_adults)):
        python_btn = Radiobutton(window_not_18_old,text=list_of_adults[i], value=list_of_adults[i], variable=lang)
        python_btn.grid()

    python_btn1 = Radiobutton(window_not_18_old, text='Свой вариант', value='Свой вариант', variable=lang)
    python_btn1.grid()

    entry = Entry(window_not_18_old)
    entry.grid()

    btn = Button(window_not_18_old,text="Выбрать", command=end_of_selection)
    btn.grid()

def WINDOW_FOR_SELECTING_THE_OWNER_IF_THERE_ARE_NO_ONE():
    window_no_owner = ThemedTk(theme="breeze")
    window_no_owner.title("Укажите собственника")
    window_no_owner.geometry("400x200")
    window_no_owner.resizable(False, False)

    def end_of_selection():
        if lang.get() == '':
            showerror(title="Ошибка", message="Вы никого не выбрали!")
            window_no_owner.attributes('-topmost', True)
            window_no_owner.attributes('-topmost', False)
        else:
            showinfo("Информация", f"Вы выбрали собственником - {lang.get()}")
            list_of_owner_in_the_absence.append(lang.get())
            print(list_of_owner_in_the_absence)
            window_no_owner.destroy()

    lang = StringVar(window_no_owner)
    LABEL = Label(window_no_owner, text="Необходимо выбрать собственника", font=("Arial", 10, 'bold'))
    LABEL.grid()

    btn1 = Radiobutton(window_no_owner,
                       text='Муниципальное образование поселок Березовка \nБерезовского района Красноярского края',
                       value='Муниципальное образование поселок Березовка Березовского района Красноярского края', variable=lang)
    btn1.grid()

    btn2 = Radiobutton(window_no_owner,
                       text='Муниципальное образование - Березовский район \nКрасноярского края',
                       value='Муниципальное образование - Березовский район Красноярского края', variable=lang)
    btn2.grid()

    btn = Button(window_no_owner, text="Выбрать", command=end_of_selection)
    btn.grid()

def AGE_CHECK_FUNCTION(d):
    list_of_adults = []
    # СОСТАВЛЯЕМ СПИСОК СОВЕРШЕННОЛЕТНИХ
    for i in d:
        if i[2][0] != '0':
            birthday = datetime.date(int(i[2][6:]), int(i[2][3:5]), int(i[2][:2]))
            today = datetime.date.today()
            years = (today.year - birthday.year)
            if birthday.month >= today.month and birthday.day > today.day:
                years -= 1
            if years >= 18:
                list_of_adults.append(i[1])
        else:
            birthday = datetime.date(int(i[2][6:]), int(i[2][3:5]), int(i[2][1]))
            today = datetime.date.today()
            years = (today.year - birthday.year)
            if birthday.month >= today.month and birthday.day > today.day:
                years -= 1
            if years >= 18:
                list_of_adults.append(i[1])
    # ВЫЯВЛЯЕМ НЕСОВЕРШЕННОЛЕТНИХ
    for i in d:
        if i[4] == '+':
            if i[2][0] != '0':
                birthday = datetime.date(int(i[2][6:]), int(i[2][3:5]), int(i[2][:2]))
                today = datetime.date.today()
                years = (today.year - birthday.year)
                if birthday.month >= today.month and birthday.day > today.day:
                    years -= 1
                if years < 18:
                    showwarning(title="Внимание", message=f"Собственник {i[1]} является несовершеннолетним. Необходимо указать законного представителя!")
                    not_18_old = i[1]
                    WINDOW_FUNCTION_FOR_SELECTION_OF_LEGAL_REPRESENTATIVE(not_18_old, list_of_adults)

            else:
                birthday = datetime.date(int(i[2][6:]), int(i[2][3:5]), int(i[2][1]))
                today = datetime.date.today()
                years = (today.year - birthday.year)
                if birthday.month >= today.month and birthday.day > today.day:
                    years -= 1
                if years < 18:
                    showwarning(title="Внимание", message=f"Собственник {i[1]} является несовершеннолетним. Необходимо указать законного представителя!")
                    not_18_old = i[1]
                    WINDOW_FUNCTION_FOR_SELECTION_OF_LEGAL_REPRESENTATIVE(not_18_old, list_of_adults)


def OWNER_SELECTION_FUNCTION(d):
    verification_of_owners = 0
    for i in d:
        if i[4] == '+':
            verification_of_owners+=1
            break
    if verification_of_owners == 0:
        showwarning(title="Внимание", message='Вы при составлении судебного приказа вы не указали ни одного собственника!')
        WINDOW_FOR_SELECTING_THE_OWNER_IF_THERE_ARE_NO_ONE()

def new_window():
    AGE_CHECK_FUNCTION(d)
    OWNER_SELECTION_FUNCTION(d)


# стандартная кнопка
btn = Button(text="Button", command=new_window)
btn.grid()

root.mainloop()