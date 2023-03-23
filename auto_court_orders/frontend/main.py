from tkinter import Tk, Button, Frame, StringVar
from tkinter import *
from tkinter.ttk import Combobox, Label
from auto_court_orders import Database

root = Tk()
root.title("Формирование судебного приказа в мировой суд") #THE DISPLAYED NAME OF THE PROGRAM
root.geometry("400x600") #SIZE PROGRAM

#FUNCTION RETURNING A LIST OF NUMBERS OF THE SELECTED HOUSE
def SELECT_HOUSE_NUMBER(event):
    VALUE = TYPE_LIST_OF_HOUSE.get()
    NUMBER_LIST_OF_HOUSE.set(Database.RESIDENTIAL_FUND[VALUE][0])
    BOX_NUMBER.config(values=Database.RESIDENTIAL_FUND[VALUE])

#SELECT THE DEBTOR'S ADDRESS
#TEXT PART
LABEL_SELECT_DEBTOR = Label(text="Выберете адрес должника", font=("Arial", 10))
LABEL_SELECT_DEBTOR.pack(anchor=NW, padx=2, pady=2)

LIST_OF_HOUSES = list(Database.RESIDENTIAL_FUND.keys())

#ONE WINDOW PART
TYPE_LIST_OF_HOUSE = StringVar()
TYPE_LIST_OF_HOUSE.set(LIST_OF_HOUSES[0])
BOX_HOUSE = Combobox(values=list(Database.RESIDENTIAL_FUND.keys()), textvariable=TYPE_LIST_OF_HOUSE)
BOX_HOUSE.pack(anchor=NW, padx=2, pady=2)
BOX_HOUSE.bind('<<ComboboxSelected>>', SELECT_HOUSE_NUMBER)

#SELECT THE DEBTOR'S NUMBER HOUSE
#TEXT PART
LABEL_SELECT_NUMBER_HOUSE = Label(text="Укажите номер дома", font=("Arial", 10))
LABEL_SELECT_NUMBER_HOUSE.pack(anchor=NW, padx=2, pady=2)

#TWO WINDOW PART
NUMBER_LIST_OF_HOUSE = StringVar()
NUMBER_LIST_OF_HOUSE.set(Database.RESIDENTIAL_FUND[LIST_OF_HOUSES[0]][0])
BOX_NUMBER = Combobox(values=Database.RESIDENTIAL_FUND[LIST_OF_HOUSES[0]], textvariable=NUMBER_LIST_OF_HOUSE)
BOX_NUMBER.pack(anchor=NW, padx=2, pady=2)


root.mainloop()