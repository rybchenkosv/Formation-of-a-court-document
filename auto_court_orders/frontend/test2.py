from tkinter import Tk, Button, Frame, StringVar
from tkinter import *
from tkinter.ttk import Combobox, Label, Treeview
from auto_court_orders import Database
from tkcalendar import Calendar, DateEntry

root = Tk()
root.title("Формирование судебного приказа в мировой суд") #THE DISPLAYED NAME OF THE PROGRAM
root.geometry("1000x600") #SIZE PROGRAM

#LOCATION CONFIGURATION
for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=0)

#THIS FUNCTION IS RESPONSIBLE FOR ASSIGNING VALUES TO THE RIGHT SIDE OF THE APPLICATION
def ASSIGNING_VALUES_TO_VARIABLES_ON_THE_RIGHT_SIDE(event):
    VARIABLE_STREET = BOX_HOUSE.get()
    VARIABLE_NUMBER = BOX_NUMBER.get()
    COMPANY_NAME_LABEL["text"] = f"{Database.NAME_OF_THE_CLAIMANT(VARIABLE_STREET, VARIABLE_NUMBER)}"
    COMPANY_ADDRESS_LABEL["text"] = f"{Database.ADDRESS_OF_THE_CLAIMANT(VARIABLE_STREET, VARIABLE_NUMBER)}"
    JUDICIAL_SECTION_LABEL["text"] = f"{Database.COURT_NUMBER(VARIABLE_STREET, VARIABLE_NUMBER)}"
    MANAGEMENT_START_DATE_LABEL["text"] = f"{Database.MANAGEMENT_START_DATE(VARIABLE_STREET, VARIABLE_NUMBER)}"

#FUNCTION RETURNING A LIST OF NUMBERS OF THE SELECTED HOUSE
def SELECT_HOUSE_NUMBER(event):
    VALUE = TYPE_LIST_OF_HOUSE.get()
    NUMBER_LIST_OF_HOUSE.set(Database.RESIDENTIAL_FUND[VALUE][0])
    BOX_NUMBER.config(values=Database.RESIDENTIAL_FUND[VALUE])

def CHECKING_THE_CORRECT_ENTRY_OF_THE_DATE_OF_BIRTH(*args):
    if len(date_debtors.get()) == 10:
        if '.' in str(date_debtors.get) and len(str(date_debtors.get()).replace('.',"")) == 8:
            result_date_of_birth.set("")
        else:
            result_date_of_birth.set("Введите корректную дату dd.mm.yyyy")
    else:
        result_date_of_birth.set("Введите корректную дату dd.mm.yyyy")

def FUNCTION_WITH_DISPLAY_OF_THE_AMOUNT_OF_GOVERNMENT(*args):
    try:
        result_of_the_fee_calculation.set(Database.AMOUNT_OF_THE_STATE_FEE(float(format_for_entering_the_amount_of_the_debt.get())))
    except:
        return result_of_the_fee_calculation.set('Сумма введена некорректно')

def FUNCTION_TO_DISPLAY_THE_TOTAL_AMOUNT_OF_DEBT(*args):
    try:
        total_debt.set('{:.2f}'.format(float(format_for_entering_the_amount_of_the_debt.get()) + float(result_of_the_fee_calculation.get())))
    except:
        return total_debt.set('Сумма введена некорректно')


## BLOCKS ON THE LEFT
## SIDE OF THE APPLICATION

#SELECT THE DEBTOR'S ADDRESS
#TEXT PART
LABEL_SELECT_DEBTOR = Label(text="Выберете адрес должника", font=("Arial", 10))
LABEL_SELECT_DEBTOR.grid(row=0, column=0)

LIST_OF_HOUSES = list(Database.RESIDENTIAL_FUND.keys())

#ONE WINDOW PART
TYPE_LIST_OF_HOUSE = StringVar()
TYPE_LIST_OF_HOUSE.set(LIST_OF_HOUSES[0])
BOX_HOUSE = Combobox(values=list(Database.RESIDENTIAL_FUND.keys()), textvariable=TYPE_LIST_OF_HOUSE)
BOX_HOUSE.grid(row=1, column=0)
BOX_HOUSE.bind('<<ComboboxSelected>>', SELECT_HOUSE_NUMBER)

#SELECT THE DEBTOR'S NUMBER HOUSE
#TEXT PART
LABEL_SELECT_NUMBER_HOUSE = Label(text="Укажите номер дома", font=("Arial", 10))
LABEL_SELECT_NUMBER_HOUSE.grid(row=2, column=0)

#TWO WINDOW PART
NUMBER_LIST_OF_HOUSE = StringVar()
NUMBER_LIST_OF_HOUSE.set(Database.RESIDENTIAL_FUND[LIST_OF_HOUSES[0]][0])
BOX_NUMBER = Combobox(values=Database.RESIDENTIAL_FUND[LIST_OF_HOUSES[0]], textvariable=NUMBER_LIST_OF_HOUSE)
BOX_NUMBER.grid(row=3, column=0)
BOX_NUMBER.bind('<<ComboboxSelected>>', ASSIGNING_VALUES_TO_VARIABLES_ON_THE_RIGHT_SIDE)

#SELECT THE DEBTOR'S APARTMENT NUMBER
#TEXT PART
LABEL_SELECT_APARTMENT_NUMBER = Label(text="Укажите номер квартиры", font=("Arial", 10))
LABEL_SELECT_APARTMENT_NUMBER.grid(row=4, column=0)

#THREE WINDOW PART
APARTMENT_NUMBER_LABEL = Entry(width=10)
APARTMENT_NUMBER_LABEL.grid(row=5, column=0)
NUMBER_APARTMENT = APARTMENT_NUMBER_LABEL.get() #ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

##
## DEBTORS INDICATION BLOCK
##
#TEXT PART
LABEL_DEBTORS_FULL_NAME = Label(text="Укажите ФИО должника", font=("Arial", 10))
LABEL_DEBTORS_FULL_NAME.grid(row=6, column=0)

#FOUR WINDOW PART
DEBTORS_FULL_NAME_LABEL = Entry(width=40)
DEBTORS_FULL_NAME_LABEL.grid(row=7, column=0)
DEBTORS_FULL_NAME = DEBTORS_FULL_NAME_LABEL.get() #ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

#DEBTORS DATE OF BIRTH
#TEXT PART
LABEL_DEBTORS_DATE_OF_BIRTH = Label(text="Укажите дату рождения должника", font=("Arial", 10))
LABEL_DEBTORS_DATE_OF_BIRTH.grid(row=8, column=0)

#FIVE WINDOW PART
date_debtors = StringVar()
DEBTORS_DATE_OF_BIRTH_LABEL = Entry(width=15, textvariable=date_debtors)
DEBTORS_DATE_OF_BIRTH_LABEL.grid(row=9, column=0)
DEBTORS_DATE_OF_BIRTH = DEBTORS_DATE_OF_BIRTH_LABEL.get() #ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

#OUTPUT BLOCK OF INCORRECT INPUT OF DATE OF BIRTH
result_date_of_birth = StringVar()
DATE_OF_BIRTH_VERIFICATION_RESULT = Label(textvariable=result_date_of_birth)
DATE_OF_BIRTH_VERIFICATION_RESULT.grid(row=10, column=0)
date_debtors.trace_add("write", CHECKING_THE_CORRECT_ENTRY_OF_THE_DATE_OF_BIRTH)

#DEBTORS DATE OF BIRTH
#TEXT PART
LABEL_PASSPORT_DATA_OF_THE_DEBTOR = Label(text="Укажите паспортные данные должника", font=("Arial", 10))
LABEL_PASSPORT_DATA_OF_THE_DEBTOR.grid(row=11, column=0)

#SIX WINDOW PART
PASSPORT_DATA_OF_THE_DEBTOR_LABEL = Entry(width=40)
PASSPORT_DATA_OF_THE_DEBTOR_LABEL.grid(row=12, column=0)
PASSPORT_DATA_OF_THE_DEBTOR = PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get() #ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

#CONFIRMATION OF REGISTRATION AND PROPERTY
#SEVEN WINDOW PART
PROPERTY_CONFIRMATION_STR = StringVar()
PROPERTY_CONFIRMATION_LABEL = Checkbutton(text="Является собственником", variable=PROPERTY_CONFIRMATION_STR)
PROPERTY_CONFIRMATION_LABEL.grid(row=13, column=0)
PROPERTY_CONFIRMATION = PROPERTY_CONFIRMATION_STR.get() #ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!
#EIGHT WINDOW PART
REGISTRATION_CHECK_STR = StringVar()
REGISTRATION_CHECK_LABEL = Checkbutton(text="Прописан", variable=REGISTRATION_CHECK_STR)
REGISTRATION_CHECK_LABEL.grid(row=14, column=0)
REGISTRATION_CHECK = REGISTRATION_CHECK_STR.get() #ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

#DEBTOR FORMATION BLOCK AND ADDITIONS TO THE TABLE
btn = Button(text="Добавить должника")
btn.grid(row=15, column=0)



## BLOCKS ON THE RIGHT
## SIDE OF THE APPLICATION

#BLOCK FOR SPECIFYING THE COMPANY NAME
LABEL_COMPANY_INFORMATION = Label(text="Управляющая компания", font=("Arial", 10))
LABEL_COMPANY_INFORMATION.grid(row=0, column=2)

#COMPANY NAME LABEL BLOCK
COMPANY_NAME_LABEL = Label()
COMPANY_NAME_LABEL.grid(row=1, column=2)

#BLOCK FOR SPECIFYING THE COMPANY'S ADDRESS
LABEL_COMPANY_INFORMATION = Label(text="Адрес управляющей компании", font=("Arial", 10))
LABEL_COMPANY_INFORMATION.grid(row=2, column=2)

#COMPANY ADDRESS LABEL BLOCK
COMPANY_ADDRESS_LABEL = Label()
COMPANY_ADDRESS_LABEL.grid(row=3, column=2)

#BLOCK FOR SPECIFYING THE JUDICIAL AREA
LABEL_JUDICIAL_AREA = Label(text="Судебный участок", font=("Arial", 10))
LABEL_JUDICIAL_AREA.grid(row=4, column=2)

#LABEL BLOCK WITH JUDICIAL SECTION
JUDICIAL_SECTION_LABEL = Label()
JUDICIAL_SECTION_LABEL.grid(row=5, column=2)

#BLOCK FOR MANAGEMENT START DATE
LABEL_MANAGEMENT_START_DATE = Label(text="Дата начала управления МКД", font=("Arial", 10))
LABEL_MANAGEMENT_START_DATE.grid(row=6, column=2)

#LABEL BLOCK WITH MANAGEMENT START DATE
MANAGEMENT_START_DATE_LABEL = Label()
MANAGEMENT_START_DATE_LABEL.grid(row=7, column=2)

#BLOCK AMOUNT OF DEBTOR'S DEBT
LABEL_DEBTORS_DEBT = Label(text="Сумма задолженности", font=("Arial", 10))
LABEL_DEBTORS_DEBT.grid(row=8, column=2)

#LABEL AMOUNT OF DEBTOR'S DEBT
format_for_entering_the_amount_of_the_debt = StringVar()
DEBTOR_DEBT_LABEL = Entry(width=40, textvariable=format_for_entering_the_amount_of_the_debt)
DEBTOR_DEBT_LABEL.grid(row=9, column=2)
DEBTOR_DEBT = DEBTOR_DEBT_LABEL.get() #ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

#BLOCK AMOUNT OF THE STATE DUTY
LABEL_AMOUNT_OF_THE_STATE_DUTY = Label(text="Сумма гос.пошлины", font=("Arial", 10))
LABEL_AMOUNT_OF_THE_STATE_DUTY.grid(row=10, column=2)

#LABEL AMOUNT OF THE STATE DUTY
result_of_the_fee_calculation = StringVar()
AMOUNT_OF_THE_STATE_DUTY_LABEL = Label(textvariable=result_of_the_fee_calculation)
AMOUNT_OF_THE_STATE_DUTY_LABEL.grid(row=11, column=2)
format_for_entering_the_amount_of_the_debt.trace_add("write", FUNCTION_WITH_DISPLAY_OF_THE_AMOUNT_OF_GOVERNMENT)
AMOUNT_OF_THE_STATE_DUTY = result_of_the_fee_calculation.get() #ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

#BLOCK TOTAL DEBT
LABEL_TOTAL_DEBT = Label(text="Общая сумма задолженности", font=("Arial", 10))
LABEL_TOTAL_DEBT.grid(row=12, column=2)

#LABEL TOTAL DEBT
total_debt = StringVar()
TOTAL_DEBT_LABEL = Label(textvariable=total_debt)
TOTAL_DEBT_LABEL.grid(row=13, column=2)
result_of_the_fee_calculation.trace_add("write", FUNCTION_TO_DISPLAY_THE_TOTAL_AMOUNT_OF_DEBT)

#DEBTY PERIOD BLOCK
##TEXT PART
LABEL_DEBT_PERIOD = Label(text="Укажите период задолженности", font=("Arial", 10))
LABEL_DEBT_PERIOD.grid(row=14, column=2)

##TEXT PART
LABEL_DEBT_PERIOD1 = Label(text="c", font=("Arial", 10))
LABEL_DEBT_PERIOD1.grid(row=15, column=2)

#BLOCK BEGINNING OF PERIOD
BEGINNING_OF_PERIOD = DateEntry(root, width=16, background="magenta3", foreground="white", bd=2)
BEGINNING_OF_PERIOD.grid(row=15, column=3)

##TEXT PART
LABEL_DEBT_PERIOD2 = Label(text="по", font=("Arial", 10))
LABEL_DEBT_PERIOD2.grid(row=15, column=4)

#BLOCK END OF PERIOD
END_OF_PERIOD = DateEntry(root, width=16, background="magenta3", foreground="white", bd=2)
END_OF_PERIOD.grid(row=15, column=5)

#CENTRAL BLOCK
#TABLE

#NULL BLOCK
N_BLOCK = Label(text="", font=("Arial", 10))
N_BLOCK.grid(row=16, column=0)

#
columns = ("number", "name", "date_of_birth", "passport_data","debtor_owner","debtor_is_registered")
tree = Treeview(columns=columns, show="headings")
tree.grid(row=17, column=0, sticky="nsew")

# определяем заголовки
tree.heading("number", text="№", anchor=W)
tree.heading("name", text="ФИО должника", anchor=W)
tree.heading("date_of_birth", text="Дата рождения должника", anchor=W)
tree.heading("passport_data", text="Паспортные данные должника", anchor=W)
tree.heading("debtor_owner", text="Собственник", anchor=W)
tree.heading("debtor_is_registered", text="Прописан", anchor=W)

tree.column("#1", stretch=NO, width=25)
tree.column("#2", stretch=NO, width=200)
tree.column("#3", stretch=NO, width=200)
tree.column("#4", stretch=NO, width=300)
tree.column("#5", stretch=NO, width=85)
tree.column("#6", stretch=NO, width=85)

# ТАБЛИЦУ СОСТАВИЛ. ИЗ ТЕСТА В ГЛАВНОЙ ПАПКЕ НЕОБХОДИМО СДЕЛАТЬ ИНТЕГРАЦИЮ ДАННЫХ В ТАБЛИЦУ.

root.mainloop()