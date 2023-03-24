from tkinter import Tk, Button, Frame, StringVar
from tkinter import *
from tkinter.ttk import Combobox, Label
from auto_court_orders import Database

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

root.mainloop()