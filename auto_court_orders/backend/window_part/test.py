from tkinter import *
from tkinter import ttk

OOO_CKY_RAZVITYE = {
    'Береговая':['36','38','40','42Б','44','46'],
    'Дружбы':['1','1А','1Б','1Г','19'],
    'Маяковского':['9','19','21','23'],
    'Мичурина':['1Б','2Б'],
    'Парковая':['2А'],
    'Пархоменко':['1А'],
    'Советской Армии':['20'],
    'Советская':['1А','43А','45','46'],
    'Строителей':['1А','2А'],
    'Сурикова':['8','10','12','14','24','26','28','30'],
    'Центральная':['42','58'],
    'Чкалова':['19'],
    'Полевая':['70','72']
}

root = Tk()
root.title("Формирование судебного приказа в мировой суд") #THE DISPLAYED NAME OF THE PROGRAM
root.geometry("400x600") #SIZE PROGRAM

#DEBTOR'S HOUSE NUMBER SELECTION FUNCTION
#OPENS AFTER SELECTING THE DEBTOR'S ADDRESS
def clear_combobox():
  BOX_NUMBER_HOUSE.pack_forget()

def SELECT_HOUSE_NUMBER(number):
    SELECTED_HOUSE = BOX_HOUSE.get()

    #TEXT PART
    LABEL_SELECT_NUMBER_HOUSE = ttk.Label(text="Укажите номер дома", font=("Arial", 10))
    LABEL_SELECT_NUMBER_HOUSE.pack(anchor=NW, padx=6, pady=12)

    #WINDOW PART
    LIST_OF_NUMBER_HOUSE = [i for i in OOO_CKY_RAZVITYE[SELECTED_HOUSE]] #ПОКА ТЕСТИРУЕМ НА СКУ РАЗВИТИЕ, ПОСЛЕ НЕОБХОДИМО УКАЗАТЬ НА ПОЛНЫЙ СПИСОК ДОМОВ
    BOX_NUMBER_HOUSE = ttk.Combobox(values=LIST_OF_NUMBER_HOUSE)
    BOX_NUMBER_HOUSE.pack(anchor=NW, padx=6, pady=10)

    button = Button(root, text='очистить', command=clear_combobox)
    button.pack()

#SELECT THE DEBTOR'S ADDRESS
#TEXT PART
LABEL_SELECT_DEBTOR = ttk.Label(text="Выберете адрес должника", font=("Arial", 10))
LABEL_SELECT_DEBTOR.pack(anchor=NW, padx=6, pady=8)

#WINDOW PART
LIST_OF_HOUSES = [i for i in OOO_CKY_RAZVITYE]
BOX_HOUSE = ttk.Combobox(values=LIST_OF_HOUSES)
BOX_HOUSE.pack(anchor=NW, padx=6, pady=6)

BOX_HOUSE.bind("<<ComboboxSelected>>", SELECT_HOUSE_NUMBER) #TRACKING VALUE SELECTION


root.mainloop()