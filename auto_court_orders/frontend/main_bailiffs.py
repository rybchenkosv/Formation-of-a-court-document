from tkinter import Tk, Button, Frame, StringVar, filedialog
from tkinter import *
from tkinter.ttk import Combobox, Label, Treeview, Notebook, Scrollbar
from auto_court_orders import Database
from tkcalendar import Calendar, DateEntry
from tkinter.messagebox import showwarning, showerror, showinfo, askyesno
from docxtpl import DocxTemplate
from ttkthemes import ThemedTk
from datetime import date
import datetime
import sqlite3

sqlite_file = 'C:/python373/lawyer_project/auto_court_orders/frontend/base_of_debtors.db'
con = sqlite3.connect(sqlite_file)

root1 = ThemedTk(theme="breeze")
root1.title("Формирование заявления судебным приставам")  # THE DISPLAYED NAME OF THE PROGRAM
root1.geometry("870x750")  # SIZE PROGRAM

date_now = date.today()

# ФУНКЦИИ
# THIS FUNCTION IS RESPONSIBLE FOR ASSIGNING VALUES TO THE RIGHT SIDE OF THE APPLICATION
def VERIFICATION_BY_ADDRESS_OF_DEBTORS():
    d = f'{VARIABLE_STREET}, {VARIABLE_NUMBER}-{APARTMENT_NUMBER_LABEL.get()}'
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM base_of_debtors")
        rows = cur.fetchall()

        # НЕОБХОДИМЫ ТЕСТЫ НА ПРОВЕРКУ УСЛОВИЙ!
        for row in rows:
            if row[5] == d:
                found_debtors = []
                t = 99999
                a = row[11].split('.')
                aa = datetime.date(int(a[2]), int(a[1]), int(a[0]))
                bb = datetime.date.today()
                cc = (str(abs(aa - bb))).split()[0]
                if cc == '0:00:00' and t == 0:
                    found_debtors.append(row)
                    t = 0
                elif cc == '0:00:00' and t != 0:
                    found_debtors.clear()
                    found_debtors.append(row)
                    t = 0
                elif cc != '0:00:00' and cc < t:
                    found_debtors.clear()
                    found_debtors.append(row)
                    t = cc
                elif cc != '0:00:00' and cc == t:
                    found_debtors.append(row)
                    t = cc

            else:
                pass





def ASSIGNING_VALUES_TO_VARIABLES_ON_THE_RIGHT_SIDE(event):
    global VARIABLE_STREET, VARIABLE_NUMBER
    VARIABLE_STREET = BOX_HOUSE.get()
    VARIABLE_NUMBER = BOX_NUMBER.get()
    COMPANY_NAME_LABEL["text"] = f"{Database.NAME_OF_THE_CLAIMANT(VARIABLE_STREET, VARIABLE_NUMBER)}"
    COMPANY_ADDRESS_LABEL["text"] = f"{Database.ADDRESS_OF_THE_CLAIMANT(VARIABLE_STREET, VARIABLE_NUMBER)}"
    JUDICIAL_SECTION_LABEL["text"] = f"{Database.COURT_NUMBER(VARIABLE_STREET, VARIABLE_NUMBER)}"
    MANAGEMENT_START_DATE_LABEL["text"] = f"{Database.MANAGEMENT_START_DATE(VARIABLE_STREET, VARIABLE_NUMBER)}"


# FUNCTION RETURNING A LIST OF NUMBERS OF THE SELECTED HOUSE
def SELECT_HOUSE_NUMBER(event):
    VALUE = TYPE_LIST_OF_HOUSE.get()
    NUMBER_LIST_OF_HOUSE.set(Database.RESIDENTIAL_FUND[VALUE][0])
    BOX_NUMBER.config(values=Database.RESIDENTIAL_FUND[VALUE])

# SELECT THE DEBTOR'S ADDRESS
# TEXT PART
LABEL_SELECT_DEBTOR = Label(text="Выберете адрес должника", font=("Arial", 10,'bold'))
LABEL_SELECT_DEBTOR.grid(row=0, column=0, sticky=NS)

LIST_OF_HOUSES = list(Database.RESIDENTIAL_FUND.keys())

# ONE WINDOW PART
TYPE_LIST_OF_HOUSE = StringVar()
TYPE_LIST_OF_HOUSE.set(LIST_OF_HOUSES[0])
BOX_HOUSE = Combobox(values=list(Database.RESIDENTIAL_FUND.keys()), textvariable=TYPE_LIST_OF_HOUSE)
BOX_HOUSE.grid(row=1, column=0, sticky=NS)
BOX_HOUSE.bind('<<ComboboxSelected>>', SELECT_HOUSE_NUMBER)

# SELECT THE DEBTOR'S NUMBER HOUSE
# TEXT PART
LABEL_SELECT_NUMBER_HOUSE = Label(text="Укажите номер дома", font=("Arial", 10,'bold'))
LABEL_SELECT_NUMBER_HOUSE.grid(row=2, column=0, sticky=NS)

# TWO WINDOW PART
NUMBER_LIST_OF_HOUSE = StringVar()
NUMBER_LIST_OF_HOUSE.set(Database.RESIDENTIAL_FUND[LIST_OF_HOUSES[0]][0])
BOX_NUMBER = Combobox(values=Database.RESIDENTIAL_FUND[LIST_OF_HOUSES[0]], textvariable=NUMBER_LIST_OF_HOUSE)
BOX_NUMBER.grid(row=3, column=0, sticky=NS)
BOX_NUMBER.bind('<<ComboboxSelected>>', ASSIGNING_VALUES_TO_VARIABLES_ON_THE_RIGHT_SIDE)

# SELECT THE DEBTOR'S APARTMENT NUMBER
# TEXT PART
LABEL_SELECT_APARTMENT_NUMBER = Label(text="Укажите номер квартиры", font=("Arial", 10,'bold'))
LABEL_SELECT_APARTMENT_NUMBER.grid(row=4, column=0, sticky=NS, pady=5)

# THREE WINDOW PART
APARTMENT_NUMBER_LABEL = Entry(width=10)
APARTMENT_NUMBER_LABEL.grid(row=5, column=0, sticky=NS)
NUMBER_APARTMENT = APARTMENT_NUMBER_LABEL.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

#
BUTTON_OKEY = Button(text="Выбрать", font=("Arial", 8,'bold'), bg='#79abfc', command=VERIFICATION_BY_ADDRESS_OF_DEBTORS)
BUTTON_OKEY.grid(row=6, column=0, sticky=NS)




















root1.resizable(False, False)
root1.iconbitmap('icon.ico')
root1.mainloop()