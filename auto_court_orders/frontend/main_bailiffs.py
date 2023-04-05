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
        global found_debtors
        found_debtors = []
        t = 99999
        for row in rows:
            if row[5] == d:
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
                elif cc != '0:00:00' and int(cc) < t:
                    found_debtors.clear()
                    found_debtors.append(row)
                    t = int(cc)
                elif cc != '0:00:00' and int(cc) == t:
                    found_debtors.append(row)
                    t = int(cc)
        print(found_debtors)
    # Теперь распределяем полученные значения по кнопкам после уведомления пользователя о найденных





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

# FUNCTION OF VERIFICATION OF THE CORRECTNESS OF THE ENTERED DATE OF BIRTH OF THE DEBTOR
def CHECKING_THE_CORRECT_ENTRY_OF_THE_DATE_OF_BIRTH(*args):
    global date_of_birth_check_variable
    if len(date_debtors.get()) == 10:
        if '.' in str(date_debtors.get) and len(str(date_debtors.get()).replace('.', "")) == 8:
            result_date_of_birth.set("")
            date_of_birth_check_variable = 'Yes'
        else:
            result_date_of_birth.set("Введите корректную дату dd.mm.yyyy")
            date_of_birth_check_variable = 'No'
    else:
        result_date_of_birth.set("Введите корректную дату dd.mm.yyyy")
        date_of_birth_check_variable = 'No'

# FUNCTION OF VERIFICATION OF CORRECTNESS OF THE INTRODUCED AMOUNT OF DEBT
def FUNCTION_WITH_DISPLAY_OF_THE_AMOUNT_OF_GOVERNMENT(*args):
    try:
        result_of_the_fee_calculation.set(
            Database.AMOUNT_OF_THE_STATE_FEE(float(format_for_entering_the_amount_of_the_debt.get())))
    except:
        return result_of_the_fee_calculation.set('Сумма введена некорректно')

# FUNCTION OF VERIFICATION OF CORRECTNESS OF THE INTRODUCED AMOUNT OF DEBT
def FUNCTION_TO_DISPLAY_THE_TOTAL_AMOUNT_OF_DEBT(*args):
    try:
        total_debt.set('{:.2f}'.format(
            float(format_for_entering_the_amount_of_the_debt.get()) + float(result_of_the_fee_calculation.get())))
    except:
        return total_debt.set('Сумма введена некорректно')

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
BUTTON_OKEY = Button(text="Проверить на наличие в базе", font=("Arial", 8,'bold'), bg='#79abfc', command=VERIFICATION_BY_ADDRESS_OF_DEBTORS)
BUTTON_OKEY.grid(row=6, column=0, sticky=NS)

##
## DEBTORS INDICATION BLOCK
##
# TEXT PART
LABEL_DEBTORS_FULL_NAME = Label(text="Укажите ФИО должника", font=("Arial", 10,'bold'))
LABEL_DEBTORS_FULL_NAME.grid(row=7, column=0, sticky=NS, pady=5)

# FOUR WINDOW PART
DEBTORS_FULL_NAME_LABEL = Entry(width=40)
DEBTORS_FULL_NAME_LABEL.grid(row=8, column=0, sticky=NS)
DEBTORS_FULL_NAME = DEBTORS_FULL_NAME_LABEL.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

# DEBTORS DATE OF BIRTH
# TEXT PART
LABEL_DEBTORS_DATE_OF_BIRTH = Label(text="Укажите дату рождения должника", font=("Arial", 10,'bold'))
LABEL_DEBTORS_DATE_OF_BIRTH.grid(row=9, column=0, sticky=NS, pady=5)

# FIVE WINDOW PART
date_debtors = StringVar()
DEBTORS_DATE_OF_BIRTH_LABEL = Entry(width=15, textvariable=date_debtors)
DEBTORS_DATE_OF_BIRTH_LABEL.grid(row=10, column=0, sticky=NS)
DEBTORS_DATE_OF_BIRTH = DEBTORS_DATE_OF_BIRTH_LABEL.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

# OUTPUT BLOCK OF INCORRECT INPUT OF DATE OF BIRTH
result_date_of_birth = StringVar()
DATE_OF_BIRTH_VERIFICATION_RESULT = Label(textvariable=result_date_of_birth, foreground='red')
DATE_OF_BIRTH_VERIFICATION_RESULT.grid(row=11, column=0, sticky=NS)
date_debtors.trace_add("write", CHECKING_THE_CORRECT_ENTRY_OF_THE_DATE_OF_BIRTH)



# DEBTOR FORMATION BLOCK AND ADDITIONS TO THE TABLE
BUTTON_ADD_DEBTOR = Button(text="Добавить должника", font=("Arial", 8,'bold'), command=ENTER_DATA_IN_THE_TABLE, bg='#79abfc')
BUTTON_ADD_DEBTOR.grid(row=16, column=0, sticky=NS)

# BUTTON FOR REMOVING A DEBTOR FROM THE LIST
DELETE_BUTTON = Button(text="Удалить из списка", font=("Arial", 8,'bold'), bg='#f54c4c', command=delete)
DELETE_BUTTON.grid(row=17, column=0, sticky=NS, pady=5)

# BUTTON TO REMOVE ALL DEBTORS FROM THE LIST
BUTTON_DELETE_ALL_DEBTORS = Button(text="Очистить данные", font=("Arial", 8,'bold'), command=CLEAR_ALL_DATA_FROM_TABLE)
BUTTON_DELETE_ALL_DEBTORS.grid(row=18, column=0, sticky=NS, pady=5)




## BLOCKS ON THE RIGHT
## SIDE OF THE APPLICATION

# BLOCK FOR SPECIFYING THE COMPANY NAME
LABEL_COMPANY_INFORMATION = Label(text="Управляющая компания", font=("Arial", 10,'bold'))
LABEL_COMPANY_INFORMATION.grid(row=0, column=1, sticky=NS)

# COMPANY NAME LABEL BLOCK
COMPANY_NAME_LABEL = Label()
COMPANY_NAME_LABEL.grid(row=1, column=1, sticky=NS)

# BLOCK FOR SPECIFYING THE COMPANY'S ADDRESS
LABEL_COMPANY_INFORMATION = Label(text="Адрес управляющей компании", font=("Arial", 10,'bold'))
LABEL_COMPANY_INFORMATION.grid(row=2, column=1, sticky=NS)

# COMPANY ADDRESS LABEL BLOCK
COMPANY_ADDRESS_LABEL = Label(justify=CENTER)
COMPANY_ADDRESS_LABEL.grid(row=3, column=1, sticky=NS, rowspan=2)

# НОМЕР СУДЕБНОГО ПРИКАЗА
LABEL_COURT_ORDER_NUMBER = Label(text="Номер судебного приказа", font=("Arial", 10,'bold'))
LABEL_COURT_ORDER_NUMBER.grid(row=5, column=1, sticky=NS)

# LABEL AMOUNT OF DEBTOR'S DEBT
COURT_ORDER_NUMBER_LABEL = Entry(width=40)
COURT_ORDER_NUMBER_LABEL.grid(row=6, column=1, sticky=NS)
COURT_ORDER_NUMBER = COURT_ORDER_NUMBER_LABEL.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!


# BLOCK AMOUNT OF DEBTOR'S DEBT
LABEL_DEBTORS_DEBT = Label(text="Сумма задолженности", font=("Arial", 10,'bold'))
LABEL_DEBTORS_DEBT.grid(row=10, column=1, sticky=NS)

# LABEL AMOUNT OF DEBTOR'S DEBT
format_for_entering_the_amount_of_the_debt = StringVar()
DEBTOR_DEBT_LABEL = Entry(width=40, textvariable=format_for_entering_the_amount_of_the_debt)
DEBTOR_DEBT_LABEL.grid(row=11, column=1, sticky=NS)
DEBTOR_DEBT = DEBTOR_DEBT_LABEL.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

# BLOCK AMOUNT OF THE STATE DUTY
LABEL_AMOUNT_OF_THE_STATE_DUTY = Label(text="Сумма гос.пошлины", font=("Arial", 10,'bold'))
LABEL_AMOUNT_OF_THE_STATE_DUTY.grid(row=12, column=1, sticky=NS)

# LABEL AMOUNT OF THE STATE DUTY
result_of_the_fee_calculation = StringVar()
AMOUNT_OF_THE_STATE_DUTY_LABEL = Label(textvariable=result_of_the_fee_calculation)
AMOUNT_OF_THE_STATE_DUTY_LABEL.grid(row=13, column=1, sticky=NS)
format_for_entering_the_amount_of_the_debt.trace_add("write", FUNCTION_WITH_DISPLAY_OF_THE_AMOUNT_OF_GOVERNMENT)
AMOUNT_OF_THE_STATE_DUTY = result_of_the_fee_calculation.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

# BLOCK TOTAL DEBT
LABEL_TOTAL_DEBT = Label(text="Общая сумма задолженности", font=("Arial", 10,'bold'))
LABEL_TOTAL_DEBT.grid(row=14, column=1, sticky=NS)

# LABEL TOTAL DEBT
total_debt = StringVar()
TOTAL_DEBT_LABEL = Label(textvariable=total_debt)
TOTAL_DEBT_LABEL.grid(row=15, column=1, sticky=NS)
result_of_the_fee_calculation.trace_add("write", FUNCTION_TO_DISPLAY_THE_TOTAL_AMOUNT_OF_DEBT)

# DEBTY PERIOD BLOCK
##TEXT PART
LABEL_DEBT_PERIOD = Label(text="Укажите период задолженности", font=("Arial", 10,'bold'))
LABEL_DEBT_PERIOD.grid(row=16, column=1, sticky=NS)

##TEXT PART
LABEL_DEBT_PERIOD1 = Label(text="c", font=("Arial", 10,'bold'))
LABEL_DEBT_PERIOD1.grid(row=17, column=1, padx=50, sticky=W)

# BLOCK BEGINNING OF PERIOD
BEGINNING_OF_PERIOD = DateEntry(root1, width=16, background="grey", date_pattern='dd.mm.yyyy', foreground="white", bd=2, locale='ru_RU')
BEGINNING_OF_PERIOD.grid(row=17, column=1, sticky=NS)

##TEXT PART
LABEL_DEBT_PERIOD2 = Label(text="по", font=("Arial", 10,'bold'))
LABEL_DEBT_PERIOD2.grid(row=18, column=1, sticky=W, padx=50)

# BLOCK END OF PERIOD
END_OF_PERIOD = DateEntry(root1, width=16, background="grey", date_pattern='dd.mm.yyyy', foreground="white", bd=2, locale='ru_RU')
END_OF_PERIOD.grid(row=18, column=1, sticky=NS)














root1.resizable(False, False)
root1.iconbitmap('icon.ico')
root1.mainloop()