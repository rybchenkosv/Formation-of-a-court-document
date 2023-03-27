from tkinter import Tk, Button, Frame, StringVar, filedialog
from tkinter import *
from tkinter.ttk import Combobox, Label, Treeview
from auto_court_orders import Database
from tkcalendar import Calendar, DateEntry
from tkinter.messagebox import showwarning
from docxtpl import DocxTemplate

root = Tk()
root.title("Формирование судебного приказа в мировой суд")  # THE DISPLAYED NAME OF THE PROGRAM
root.geometry("1000x600")  # SIZE PROGRAM

# LOCATION CONFIGURATION
for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=0)


# THIS FUNCTION IS RESPONSIBLE FOR ASSIGNING VALUES TO THE RIGHT SIDE OF THE APPLICATION
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


# FUNCTION OF COLLECTING DEBTORS TO THE BASE AND DISPLAYING TO THE APPLICATION TABLE
def ENTER_DATA_IN_THE_TABLE(*args):
    list_for_a_new_debtor = []
    if PROPERTY_CONFIRMATION_STR.get() == '' or REGISTRATION_CHECK_STR.get() == '':  # OUTPUT OF THE ERROR WINDOW OF NOT SPECIFIED DATA ABOUT REGISTERED OR OWNERS
        return showwarning(title="Ошибка",
                           message="Вы не указали данные о том, является ли Должник собственником или прописанным")
    else:
        if DEBTORS_FULL_NAME_LABEL.get() == '' or DEBTORS_DATE_OF_BIRTH_LABEL.get() == '' or PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get() == '':
            return showwarning(title="Ошибка", message="Заполните все поля")
        else:
            if date_of_birth_check_variable == 'Yes':
                if PROPERTY_CONFIRMATION_STR.get() == '1' and REGISTRATION_CHECK_STR.get() == '1':  # CHECKING WHETHER THE DEBTOR IS OWNER OR REGISTERED
                    general_list_of_debtors.append((len(general_list_of_debtors) + 1, DEBTORS_FULL_NAME_LABEL.get(),
                                                    DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                                                    PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '+', '+'))
                    list_for_a_new_debtor.append(
                        (len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '+', '+'))
                    general_list_of_debtors_second_window.append(
                        [len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get()])
                elif PROPERTY_CONFIRMATION_STR.get() == '1' and REGISTRATION_CHECK_STR.get() == '0':
                    general_list_of_debtors.append((len(general_list_of_debtors) + 1, DEBTORS_FULL_NAME_LABEL.get(),
                                                    DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                                                    PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '+', '-'))
                    list_for_a_new_debtor.append(
                        (len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '+', '-'))
                    general_list_of_debtors_second_window.append(
                        [len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get()])
                elif PROPERTY_CONFIRMATION_STR.get() == '0' and REGISTRATION_CHECK_STR.get() == '1':
                    general_list_of_debtors.append((len(general_list_of_debtors) + 1, DEBTORS_FULL_NAME_LABEL.get(),
                                                    DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                                                    PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '-', '+'))
                    list_for_a_new_debtor.append(
                        (len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '-', '+'))
                    general_list_of_debtors_second_window.append(
                        [len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get()])
                elif PROPERTY_CONFIRMATION_STR.get() == '0' and REGISTRATION_CHECK_STR.get() == '0':
                    general_list_of_debtors.append((len(general_list_of_debtors) + 1, DEBTORS_FULL_NAME_LABEL.get(),
                                                    DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                                                    PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '-', '-'))
                    list_for_a_new_debtor.append(
                        (len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '-', '-'))
                    general_list_of_debtors_second_window.append(
                        [len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get()])
                for person in list_for_a_new_debtor:
                    TABLE_PARAMETERS.insert("", END, values=person)
            else:
                return showwarning(title="Ошибка", message="Вы неверно заполнили поле 'Дата рождения должника'")


# FUNCTION OF CREATING A DATA CHECK WINDOW AND FORMING A JUDICIAL ACT
def VALIDATION_AND_DATA_GENERATION_FUNCTION():
    window = Tk()
    window.title("Проверьте введенные данные:")
    window.geometry("500x300")

    DATA_VERIFICATION_LABEL = Label(window, text="Проверьте введенные данные:", font=("Arial", 10))
    DATA_VERIFICATION_LABEL.grid(row=0, column=0)

    DEBTORS_ADDRESS_VERIFICATION_LABEL = Label(window, text="Адрес должника(-ов):", font=("Arial", 10))
    DEBTORS_ADDRESS_VERIFICATION_LABEL.grid(row=1, column=0)

    DEBTOR_STREET_LABEL = Label(window, text="ул." + BOX_HOUSE.get(), font=("Arial", 10))
    DEBTOR_STREET_LABEL.grid(row=1, column=1)

    DEBTOR_HOUSE_NUMBER_LABEL = Label(window, text="д." + BOX_NUMBER.get(), font=("Arial", 10))
    DEBTOR_HOUSE_NUMBER_LABEL.grid(row=1, column=2)

    DEBTOR_APARTMENT_NUMBER_LABEL = Label(window, text="кв." + APARTMENT_NUMBER_LABEL.get(), font=("Arial", 10))
    DEBTOR_APARTMENT_NUMBER_LABEL.grid(row=1, column=3)

    AMOUNT_OWED_LABEL = Label(window, text="Сумма задолженности: " + DEBTOR_DEBT_LABEL.get(), font=("Arial", 10))
    AMOUNT_OWED_LABEL.grid(row=2, column=0)

    WITHDRAWAL_OF_STATE_DUTY_LABEL = Label(window, text="Сумма гос.пошлины: " + result_of_the_fee_calculation.get(),
                                           font=("Arial", 10))
    WITHDRAWAL_OF_STATE_DUTY_LABEL.grid(row=2, column=1)

    DISPLAY_TOTAL_DEBT_LABEL = Label(window, text="Общая сумма задолженности: " + total_debt.get(), font=("Arial", 10))
    DISPLAY_TOTAL_DEBT_LABEL.grid(row=3, column=0)

    DISPLAYING_THE_PERIOD_OF_DEBTS_LABEL = Label(window, text=f'Период задолженности: c {BEGINNING_OF_PERIOD.get()} по {END_OF_PERIOD.get()}', font=("Arial", 10))
    DISPLAYING_THE_PERIOD_OF_DEBTS_LABEL.grid(row=4, column=0)

    DISPLAY_OF_DEBTORS_LABEL = Label(window, text="Должники", font=("Arial", 10))
    DISPLAY_OF_DEBTORS_LABEL.grid(row=5, column=0)

    counter_t = 0
    for i in general_list_of_debtors_second_window:
        OUTPUT_TABLE_LABEL = Label(window, text=i, font=("Arial", 10))
        OUTPUT_TABLE_LABEL.grid(row=6 + counter_t, column=0)
        counter_t += 1

    def save_file():
        filepath = filedialog.askdirectory()
        NAME_OF_THE_SAVE_ACT_LABEL['text'] = filepath
        print(NAME_OF_THE_SAVE_ACT_LABEL['text'])

    BUTTON_SAVE_AS_LABEL = Button(window, text="Сохранить файл как", command=save_file)
    BUTTON_SAVE_AS_LABEL.grid(row=7 + counter_t, column=0)

    NAME_OF_THE_SAVE_ACT_LABEL = Label(window, text='')
    NAME_OF_THE_SAVE_ACT_LABEL.grid(row=7 + counter_t, column=1)

    TEXT_NAME_DEBTORS_LABEL = Label(window, text="Имя файла: ", font=("Arial", 10))
    TEXT_NAME_DEBTORS_LABEL.grid(row=8 + counter_t, column=0)

    NAME_DEBTORS_LABEL = Entry(window)
    NAME_DEBTORS_LABEL.insert(0, f'{VARIABLE_STREET} {VARIABLE_NUMBER}-{APARTMENT_NUMBER_LABEL.get()}')
    NAME_DEBTORS_LABEL.grid(row=8 + counter_t, column=1)

#FUNCTION OF DATA CONVERSION TO DOC FORMAT AND SAVING OF THE FINISHED DOCUMENT
    def TEXT_DOCUMENT():
        # THE FUNCTION OF FORMING FROM THE RECEIVED DATA A STRING WITH \n HYPHENATIONS
        # FOR TRANSMISSION TO DOC
        def DOC_DATA_GENERATION_FUNCTION(data):
            assembly_variable = ''
            for i in data:
                for j in range(len(i)):
                    if j != 0:
                        if j == 2:
                            assembly_variable += i[j] + ' года рождения'
                            assembly_variable += '\n'
                        else:
                            assembly_variable += i[j]
                            assembly_variable += '\n'
                assembly_variable += '\n'
            return assembly_variable

        def FUNCTION_OF_COLLECTION_FROM_OWNERS_OF_DEBTORS(data):
            assembly_variable = ''
            for i in data:
                if i[4] == '+':
                    assembly_variable += i[1] + ', '
            return assembly_variable[:len(assembly_variable) - 2]

        def FUNCTION_OF_COLLECTION_REGISTERED_DEBTORS(data):
            assembly_variable = ''
            for i in data:
                if i[5] == '+':
                    assembly_variable += i[1] + ', '
            if len(assembly_variable) != 0:
                return assembly_variable[:len(assembly_variable) - 2]
            else:
                return assembly_variable

        def FUNCTION_TO_CHECK_REGISTERED_FOR_DOC(data):
            assembly_variable = ''
            for i in data:
                if i[5] == '+':
                    assembly_variable += i[1] + ', '
            if len(assembly_variable) == 0:
                return 'никто не состоит'
            else:
                return 'состоят'

        def FUNCTION_TO_CHECK_THE_NUMBER_OF_OBLIGERS_FOR_DOC(data):
            if len(data) > 1:
                return 'в солидарном порядке с следующих должников:'
            else:
                return 'с следующих должников:'

        def LIST_OF_DEBTORS_FUNCTION(data):
            assembly_variable = ''
            for i in data:
                for j in range(len(i)):
                    if j != 0 and j != 3:
                        if j == 2:
                            assembly_variable += i[j] + ' года рождения'
                            assembly_variable += ', '
                        else:
                            assembly_variable += i[j] + ' '
            return assembly_variable

        def DEBT_PERIOD_FUNCTION(start, end):
            text = 'c ' + start + ' г.' + ' по ' + end + ' г.'
            return text

        doc = DocxTemplate("shablonsydybprik.docx") #DOCUMENT TEMPLATE

        context = {'name_of_the_court': JUDICIAL_SECTION_LABEL["text"],  # TRANSFERRING COURT DATA
                   'claimant': COMPANY_NAME_LABEL["text"],  # TRANSFER OF CLAIMANTS
                   'address_claimant': COMPANY_ADDRESS_LABEL["text"],  # TRANSFER ADDRESS CLAIMANT
                   'debtors': DOC_DATA_GENERATION_FUNCTION(general_list_of_debtors_second_window), # DEBTORS
                   'variable_street': VARIABLE_STREET,  # TRANSFER OF THE DEBTOR'S ADDRESS
                   'variable_number': VARIABLE_NUMBER,  # TRANSFER OF THE HOUSE NUMBER OF THE DEBTOR
                   'apartment_variable_number': APARTMENT_NUMBER_LABEL.get(),  # TRANSFER OF THE APARTMENT NUMBER OF THE DEBTOR
                   'amount_debt': DEBTOR_DEBT_LABEL.get(),  # TRANSFER THE AMOUNT OF DEBT
                   'amount_state_fee': result_of_the_fee_calculation.get(),  # TRANSFER STATE DUTY
                   'owners_of_debtors': FUNCTION_OF_COLLECTION_FROM_OWNERS_OF_DEBTORS(general_list_of_debtors), # DEBTORS IN LIST FORMAT
                   'check': FUNCTION_TO_CHECK_REGISTERED_FOR_DOC(general_list_of_debtors),
                   # FORMATION OF THE TEXT DEPENDING ON WHETHER THE REGISTERED DEBTORS
                   'registered_debtors': FUNCTION_OF_COLLECTION_REGISTERED_DEBTORS(general_list_of_debtors), # LIST OF REGISTERED
                   'management_start': MANAGEMENT_START_DATE_LABEL["text"],  # TRANSFER THE STARTING DATE OF MANAGEMENT
                   'debt_period': DEBT_PERIOD_FUNCTION(BEGINNING_OF_PERIOD.get(), END_OF_PERIOD.get()), # DEBT PERIOD
                   'total_debt': total_debt.get(),  # TRANSFER TOTAL DEBT
                   'check_quantity': FUNCTION_TO_CHECK_THE_NUMBER_OF_OBLIGERS_FOR_DOC(general_list_of_debtors),
                   # FORMATION OF THE TEXT DEPENDING ON THE NUMBER OF DEBTORS
                   'list_of_debtors': LIST_OF_DEBTORS_FUNCTION(general_list_of_debtors_second_window), # LIST OF DEBTORS
                   }

        save_folder_path = NAME_OF_THE_SAVE_ACT_LABEL['text'] # COMPUTER SAVE PATH VARIABLE
        save_name = NAME_DEBTORS_LABEL.get() # VARIABLE ADDRESS AND APARTMENTS OF THE DEBTOR FOR TEXT FORMAT
        doc.render(context) # GENERATION OF ALL DATA
        doc.save(f"{save_folder_path}/{save_name}.docx") # TRANSFER AND SAVING DATA

    # BUTTON FOR SENDING GENERATED DATA TO THE FUNCTION OF AUTOMATIC GENERATION AND SAVING DATA
    SENDING_FILES_TO_A_DOC_LABEL = Button(window, text="ОТПРАВИТЬ", command=TEXT_DOCUMENT)
    SENDING_FILES_TO_A_DOC_LABEL.grid(row=9 + counter_t, column=0)


## BLOCKS ON THE LEFT
## SIDE OF THE APPLICATION

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
LABEL_SELECT_APARTMENT_NUMBER.grid(row=4, column=0, sticky=NS)

# THREE WINDOW PART
APARTMENT_NUMBER_LABEL = Entry(width=10)
APARTMENT_NUMBER_LABEL.grid(row=5, column=0, sticky=NS)
NUMBER_APARTMENT = APARTMENT_NUMBER_LABEL.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

##
## DEBTORS INDICATION BLOCK
##
# TEXT PART
LABEL_DEBTORS_FULL_NAME = Label(text="Укажите ФИО должника", font=("Arial", 10,'bold'))
LABEL_DEBTORS_FULL_NAME.grid(row=6, column=0, sticky=NS)

# FOUR WINDOW PART
DEBTORS_FULL_NAME_LABEL = Entry(width=40)
DEBTORS_FULL_NAME_LABEL.grid(row=7, column=0, sticky=NS)
DEBTORS_FULL_NAME = DEBTORS_FULL_NAME_LABEL.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

# DEBTORS DATE OF BIRTH
# TEXT PART
LABEL_DEBTORS_DATE_OF_BIRTH = Label(text="Укажите дату рождения должника", font=("Arial", 10,'bold'))
LABEL_DEBTORS_DATE_OF_BIRTH.grid(row=8, column=0, sticky=NS)

# FIVE WINDOW PART
date_debtors = StringVar()
DEBTORS_DATE_OF_BIRTH_LABEL = Entry(width=15, textvariable=date_debtors)
DEBTORS_DATE_OF_BIRTH_LABEL.grid(row=9, column=0, sticky=NS)
DEBTORS_DATE_OF_BIRTH = DEBTORS_DATE_OF_BIRTH_LABEL.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

# OUTPUT BLOCK OF INCORRECT INPUT OF DATE OF BIRTH
result_date_of_birth = StringVar()
DATE_OF_BIRTH_VERIFICATION_RESULT = Label(textvariable=result_date_of_birth)
DATE_OF_BIRTH_VERIFICATION_RESULT.grid(row=10, column=0, sticky=NS)
date_debtors.trace_add("write", CHECKING_THE_CORRECT_ENTRY_OF_THE_DATE_OF_BIRTH)

# DEBTORS DATE OF BIRTH
# TEXT PART
LABEL_PASSPORT_DATA_OF_THE_DEBTOR = Label(text="Укажите паспортные данные должника", font=("Arial", 10,'bold'))
LABEL_PASSPORT_DATA_OF_THE_DEBTOR.grid(row=11, column=0, sticky=NS)

# SIX WINDOW PART
PASSPORT_DATA_OF_THE_DEBTOR_LABEL = Entry(width=40)
PASSPORT_DATA_OF_THE_DEBTOR_LABEL.grid(row=12, column=0, sticky=NS)
PASSPORT_DATA_OF_THE_DEBTOR = PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

# CONFIRMATION OF REGISTRATION AND PROPERTY
# SEVEN WINDOW PART
PROPERTY_CONFIRMATION_STR = StringVar()
PROPERTY_CONFIRMATION_LABEL = Checkbutton(text="Является собственником", variable=PROPERTY_CONFIRMATION_STR)
PROPERTY_CONFIRMATION_LABEL.grid(row=13, column=0, sticky=NS)
PROPERTY_CONFIRMATION = PROPERTY_CONFIRMATION_STR.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!
# EIGHT WINDOW PART
REGISTRATION_CHECK_STR = StringVar()
REGISTRATION_CHECK_LABEL = Checkbutton(text="Прописан", variable=REGISTRATION_CHECK_STR)
REGISTRATION_CHECK_LABEL.grid(row=14, column=0, sticky=NS)
REGISTRATION_CHECK = REGISTRATION_CHECK_STR.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

# DEBTOR FORMATION BLOCK AND ADDITIONS TO THE TABLE
BUTTON_ADD_DEBTOR = Button(text="Добавить должника", command=ENTER_DATA_IN_THE_TABLE)
BUTTON_ADD_DEBTOR.grid(row=15, column=0, sticky=NS)

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
COMPANY_ADDRESS_LABEL.grid(row=3, column=1, sticky=NS)

# BLOCK FOR SPECIFYING THE JUDICIAL AREA
LABEL_JUDICIAL_AREA = Label(text="Судебный участок", font=("Arial", 10,'bold'))
LABEL_JUDICIAL_AREA.grid(row=4, column=1, sticky=NS)

# LABEL BLOCK WITH JUDICIAL SECTION
JUDICIAL_SECTION_LABEL = Label(justify=CENTER)
JUDICIAL_SECTION_LABEL.grid(row=5, column=1, sticky=NS)

# BLOCK FOR MANAGEMENT START DATE
LABEL_MANAGEMENT_START_DATE = Label(text="Дата начала управления МКД", font=("Arial", 10,'bold'))
LABEL_MANAGEMENT_START_DATE.grid(row=6, column=1, sticky=NS)

# LABEL BLOCK WITH MANAGEMENT START DATE
MANAGEMENT_START_DATE_LABEL = Label()
MANAGEMENT_START_DATE_LABEL.grid(row=7, column=1, sticky=NS)

# BLOCK AMOUNT OF DEBTOR'S DEBT
LABEL_DEBTORS_DEBT = Label(text="Сумма задолженности", font=("Arial", 10,'bold'))
LABEL_DEBTORS_DEBT.grid(row=8, column=1, sticky=NS)

# LABEL AMOUNT OF DEBTOR'S DEBT
format_for_entering_the_amount_of_the_debt = StringVar()
DEBTOR_DEBT_LABEL = Entry(width=40, textvariable=format_for_entering_the_amount_of_the_debt)
DEBTOR_DEBT_LABEL.grid(row=9, column=1, sticky=NS)
DEBTOR_DEBT = DEBTOR_DEBT_LABEL.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

# BLOCK AMOUNT OF THE STATE DUTY
LABEL_AMOUNT_OF_THE_STATE_DUTY = Label(text="Сумма гос.пошлины", font=("Arial", 10,'bold'))
LABEL_AMOUNT_OF_THE_STATE_DUTY.grid(row=10, column=1, sticky=NS)

# LABEL AMOUNT OF THE STATE DUTY
result_of_the_fee_calculation = StringVar()
AMOUNT_OF_THE_STATE_DUTY_LABEL = Label(textvariable=result_of_the_fee_calculation)
AMOUNT_OF_THE_STATE_DUTY_LABEL.grid(row=11, column=1, sticky=NS)
format_for_entering_the_amount_of_the_debt.trace_add("write", FUNCTION_WITH_DISPLAY_OF_THE_AMOUNT_OF_GOVERNMENT)
AMOUNT_OF_THE_STATE_DUTY = result_of_the_fee_calculation.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

# BLOCK TOTAL DEBT
LABEL_TOTAL_DEBT = Label(text="Общая сумма задолженности", font=("Arial", 10,'bold'))
LABEL_TOTAL_DEBT.grid(row=12, column=1, sticky=NS)

# LABEL TOTAL DEBT
total_debt = StringVar()
TOTAL_DEBT_LABEL = Label(textvariable=total_debt)
TOTAL_DEBT_LABEL.grid(row=13, column=1, sticky=NS)
result_of_the_fee_calculation.trace_add("write", FUNCTION_TO_DISPLAY_THE_TOTAL_AMOUNT_OF_DEBT)

# DEBTY PERIOD BLOCK
##TEXT PART
LABEL_DEBT_PERIOD = Label(text="Укажите период задолженности", font=("Arial", 10,'bold'))
LABEL_DEBT_PERIOD.grid(row=14, column=1, sticky=NS)

##TEXT PART
LABEL_DEBT_PERIOD1 = Label(text="c", font=("Arial", 10,'bold'))
LABEL_DEBT_PERIOD1.grid(row=15, column=1, sticky=NS)

# BLOCK BEGINNING OF PERIOD
BEGINNING_OF_PERIOD = DateEntry(root, width=16, background="magenta3", date_pattern='dd.mm.yyyy', foreground="white", bd=2)
BEGINNING_OF_PERIOD.grid(row=15, column=2, sticky=W, padx=10)

##TEXT PART
LABEL_DEBT_PERIOD2 = Label(text="по", font=("Arial", 10,'bold'))
LABEL_DEBT_PERIOD2.grid(row=15, column=3, sticky=W, padx=10)

# BLOCK END OF PERIOD
END_OF_PERIOD = DateEntry(root, width=16, background="magenta3", date_pattern='dd.mm.yyyy', foreground="white", bd=2)
END_OF_PERIOD.grid(row=15, column=4, sticky=W, padx=10)

# CENTRAL BLOCK
# TABLE

# GENERAL LIST OF DEBTORS AND DATA ABOUT THEM
general_list_of_debtors = []
general_list_of_debtors_second_window = []

# ZERO BLOCK FOR EMPTY FIELD
ZERO_BLOCK = Label(text="", font=("Arial", 10))
ZERO_BLOCK.grid(columnspan=5)

# TABLE CREATION BLOCK
TABLE_HEADINGS = ("number", "name", "date_of_birth", "passport_data", "debtor_owner", "debtor_is_registered")
TABLE_PARAMETERS = Treeview(columns=TABLE_HEADINGS, show="headings")
TABLE_PARAMETERS.grid(columnspan=5)

# TABLE HEADING BLOCK
TABLE_PARAMETERS.heading("number", text="№", anchor=W)
TABLE_PARAMETERS.heading("name", text="ФИО должника", anchor=W)
TABLE_PARAMETERS.heading("date_of_birth", text="Дата рождения должника", anchor=W)
TABLE_PARAMETERS.heading("passport_data", text="Паспортные данные должника", anchor=W)
TABLE_PARAMETERS.heading("debtor_owner", text="Собственник", anchor=W)
TABLE_PARAMETERS.heading("debtor_is_registered", text="Прописан", anchor=W)

TABLE_PARAMETERS.column("#1", stretch=NO, width=25)
TABLE_PARAMETERS.column("#2", stretch=NO, width=200)
TABLE_PARAMETERS.column("#3", stretch=NO, width=200)
TABLE_PARAMETERS.column("#4", stretch=NO, width=300)
TABLE_PARAMETERS.column("#5", stretch=NO, width=85)
TABLE_PARAMETERS.column("#6", stretch=NO, width=85)

# ORDER FORMATION BUTTON
btn = Button(text="СФОРМИРОВАТЬ ПРИКАЗ", command=VALIDATION_AND_DATA_GENERATION_FUNCTION)
btn.grid(row=18, column=0)


root.mainloop()