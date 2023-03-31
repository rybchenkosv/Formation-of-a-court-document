from tkinter import Tk, Button, Frame, StringVar, filedialog
from tkinter import *
from tkinter.ttk import Combobox, Label, Treeview, Notebook, Scrollbar
from auto_court_orders import Database
from tkcalendar import Calendar, DateEntry
from tkinter.messagebox import showwarning, showerror, showinfo, askyesno
from docxtpl import DocxTemplate
from ttkthemes import ThemedTk
from datetime import date


root = ThemedTk(theme="breeze")
root.title("Формирование судебного приказа в мировой суд")  # THE DISPLAYED NAME OF THE PROGRAM
root.geometry("870x750")  # SIZE PROGRAM


# LOCATION CONFIGURATION
for c in range(20): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=1)

# GENERAL LIST OF DEBTORS AND DATA ABOUT THEM
general_list_of_debtors = []
general_list_of_debtors_second_window = []

LIST_OF_EXCLUDED_DEBTORS_NUMBERS = []
all_del = []

# STATE FEE LIST AND COURT FILE LISTS
LIST_OF_THE_REGISTER_OF_THE_STATE_DUTY = []
LIST_OF_DEBTORS_FOR_THE_COURT = []

# REGISTRY WINDOW FUNCTIONS

def STATE_DUTY_REGISTRY_WINDOW_FUNCTIONS():
    state_duty_register_generation_window = ThemedTk(theme="breeze")
    state_duty_register_generation_window.title("Реестр на оплату госпошлины")
    state_duty_register_generation_window.geometry("825x440")
    state_duty_register_generation_window.iconbitmap('icon.ico')
    state_duty_register_generation_window.resizable(False, False)

    def save_file():
        filepath = filedialog.askdirectory()
        NAME_OF_THE_SAVE_ACT_LABEL['text'] = filepath
        state_duty_register_generation_window.attributes('-topmost', True)
        state_duty_register_generation_window.attributes('-topmost', False)

    # TABLE CREATION BLOCK
    TABLE_HEADINGS_register = ("number", "address", "name", "amount_of_state_duty", "management_company")
    TABLE_PARAMETERS_register = Treeview(state_duty_register_generation_window, columns=TABLE_HEADINGS_register, show="headings")
    TABLE_PARAMETERS_register.grid(row=0, column=0, sticky="nsew")

    # БЛОКИРУЕМ НАЖАТИЕ ПОВТОРНО
    asasas = Button(text="РЕЕСТР НА ОПЛАТУ \nГОСПОШЛИНЫ", font=("Arial", 8, 'bold'))
    asasas.grid(row=14, column=2, rowspan=2)

    ### НАПОЛНЯЕМ ТАБЛИЦУ
    for i in LIST_OF_THE_REGISTER_OF_THE_STATE_DUTY:
        TABLE_PARAMETERS_register.insert("", END, values=i)

    # TABLE HEADING BLOCK
    TABLE_PARAMETERS_register.heading("number", text="№")
    TABLE_PARAMETERS_register.heading("address", text="Адрес")
    TABLE_PARAMETERS_register.heading("name", text="ФИО должника")
    TABLE_PARAMETERS_register.heading("amount_of_state_duty", text="Сумма гос.пошлины")
    TABLE_PARAMETERS_register.heading("management_company", text="Управляющая компания")

    TABLE_PARAMETERS_register.column("#1", stretch=True, width=50)
    TABLE_PARAMETERS_register.column("#2", stretch=True, width=200)
    TABLE_PARAMETERS_register.column("#3", stretch=True, width=200)
    TABLE_PARAMETERS_register.column("#4", stretch=True, width=150)
    TABLE_PARAMETERS_register.column("#5", stretch=True, width=180)

    # добавляем вертикальную прокрутку
    scrollbar = Scrollbar(state_duty_register_generation_window, orient=VERTICAL, command=TABLE_PARAMETERS_register.yview)
    TABLE_PARAMETERS_register.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    NULL_BLOCK = Label(state_duty_register_generation_window, text='')
    NULL_BLOCK.grid(column=0, sticky=W)

    BUTTON_SAVE_AS_LABEL = Button(state_duty_register_generation_window, text="Путь сохранения", font=("Arial", 10, 'bold'), command=save_file)
    BUTTON_SAVE_AS_LABEL.grid(column=0, sticky=W, padx=2)

    NAME_OF_THE_SAVE_ACT_LABEL = Label(state_duty_register_generation_window, text='')
    NAME_OF_THE_SAVE_ACT_LABEL.grid(column=0, sticky=W, padx=2)

    NULL_BLOCK = Label(state_duty_register_generation_window, text='')
    NULL_BLOCK.grid(column=0, sticky=W, padx=2)

    TEXT_NAME_DEBTORS_LABEL = Label(state_duty_register_generation_window, text="Сохранить файл как: ", font=("Arial", 10, 'bold'))
    TEXT_NAME_DEBTORS_LABEL.grid(column=0, sticky=W, padx=2)

    NAME_DEBTORS_LABEL = Entry(state_duty_register_generation_window, width=40)
    NAME_DEBTORS_LABEL.insert(0, 'Реестр на оплату госпошлины')
    NAME_DEBTORS_LABEL.grid(column=0, sticky=W, padx=2)

    NULL_BLOCK = Label(state_duty_register_generation_window, text='')
    NULL_BLOCK.grid(column=0, sticky=W, padx=2)

    def finish():
        asasas = Button(text="РЕЕСТР НА ОПЛАТУ \nГОСПОШЛИНЫ", font=("Arial", 8, 'bold'),
                        command=STATE_DUTY_REGISTRY_WINDOW_FUNCTIONS)
        asasas.grid(row=14, column=2, rowspan=2)
        state_duty_register_generation_window.destroy()


    def distribution_function_by_management_companies():
        SKY_R = []
        BSK_P = []
        KONCEPT = []
        for i in LIST_OF_THE_REGISTER_OF_THE_STATE_DUTY:
            if i[4] == 'ООО "СКУ Развитие"':
                SKY_R.append(i)
            elif i[4] == 'ООО "БСК Плюс"':
                BSK_P.append(i)
            elif i[4] == 'ООО "Концепт"':
                KONCEPT.append(i)
            else:
                showerror(title="Ошибка", message=f"Не смогли найти управляющую компанию по адресу {i[2]}")
                break

        def TEXT_DOCUMENT(list):
            # FOR TRANSMISSION TO DOC
            # list = [[1, ФИО, Адрес, Сумма, УК]]
            number, name, address, amount_state_duty = '', '', '', ''
            k = 1
            M_company = list[0][4].replace('"', '')
            date_now = date.today()

            for i in list:
                name += i[1] + '\n'
                address += i[2] + '\n'
                amount_state_duty += i[3] + '\n'
                number += str(k) + '\n'
                k += 1

            doc = DocxTemplate("for_payment_of_state_duty.docx")  # DOCUMENT TEMPLATE

            context = {'m_company': M_company,  # НАЗВАНИЕ УК
                       'n_1': number,  # НОМЕР
                       'n_2': name,  # ФИО
                       'n_3': address,  # АДРЕС
                       'n_4': amount_state_duty,  # СУММА
                       }

            save_folder_path = NAME_OF_THE_SAVE_ACT_LABEL['text']  # COMPUTER SAVE PATH VARIABLE
            save_name = f'{NAME_DEBTORS_LABEL.get()} {M_company} от {date_now.day}.{date_now.month}.{date_now.year} года'  # VARIABLE ADDRESS AND APARTMENTS OF THE DEBTOR FOR TEXT FORMAT
            doc.render(context)  # GENERATION OF ALL DATA
            doc.save(f"{save_folder_path}/{save_name}.docx")  # TRANSFER AND SAVING DATA
            showinfo(title="Информация", message=f'Реестр на оплату госпошлины для {M_company} создан!')


        if len(SKY_R) >= 1:
            TEXT_DOCUMENT(SKY_R)
        if len(BSK_P) >= 1:
            TEXT_DOCUMENT(BSK_P)
        if len(KONCEPT) >= 1:
            TEXT_DOCUMENT(KONCEPT)

        finish()


    state_duty_register_generation_window.protocol("WM_DELETE_WINDOW", finish)


    CREATE_BUTTON_LABEL = Button(state_duty_register_generation_window, text="СОЗДАТЬ", font=("Arial", 10, 'bold'), bg='#79abfc', command=distribution_function_by_management_companies)
    CREATE_BUTTON_LABEL.grid(column=0, sticky=W, padx=2)



def REGISTRY_WINDOW_FUNCTION_TO_COURT():
    window_for_the_formation_of_the_registry_to_the_court = ThemedTk(theme="breeze")
    window_for_the_formation_of_the_registry_to_the_court.title("Реестр на подачу в мировой суд")
    window_for_the_formation_of_the_registry_to_the_court.geometry("975x440")
    window_for_the_formation_of_the_registry_to_the_court.iconbitmap('icon.ico')
    window_for_the_formation_of_the_registry_to_the_court.resizable(False, False)

    def save_file():
        filepath = filedialog.askdirectory()
        NAME_OF_THE_SAVE_ACT_LABEL['text'] = filepath
        window_for_the_formation_of_the_registry_to_the_court.attributes('-topmost', True)
        window_for_the_formation_of_the_registry_to_the_court.attributes('-topmost', False)

    # TABLE CREATION BLOCK
    TABLE_HEADINGS_register = ("number", "address", "name", "court_number", "management_company")
    TABLE_PARAMETERS_register = Treeview(window_for_the_formation_of_the_registry_to_the_court, columns=TABLE_HEADINGS_register,
                                         show="headings")
    TABLE_PARAMETERS_register.grid(row=0, column=0, sticky="nsew")

    # БЛОКИРУЕМ НАЖАТИЕ ПОВТОРНО
    asasas1 = Button(text="РЕЕСТР НА ПОДАЧУ \nВ МИРОВОЙ СУД", font=("Arial", 8, 'bold'))
    asasas1.grid(row=16, column=2, rowspan=2)

    ### НАПОЛНЯЕМ ТАБЛИЦУ
    for i in LIST_OF_DEBTORS_FOR_THE_COURT:
        TABLE_PARAMETERS_register.insert("", END, values=i)

    # TABLE HEADING BLOCK
    TABLE_PARAMETERS_register.heading("number", text="№")
    TABLE_PARAMETERS_register.heading("address", text="Адрес")
    TABLE_PARAMETERS_register.heading("name", text="ФИО должника")
    TABLE_PARAMETERS_register.heading("court_number", text="Номер судебного участка")
    TABLE_PARAMETERS_register.heading("management_company", text="Управляющая компания")

    TABLE_PARAMETERS_register.column("#1", stretch=True, width=50)
    TABLE_PARAMETERS_register.column("#2", stretch=True, width=200)
    TABLE_PARAMETERS_register.column("#3", stretch=True, width=200)
    TABLE_PARAMETERS_register.column("#4", stretch=True, width=250)
    TABLE_PARAMETERS_register.column("#5", stretch=True, width=230)

    # добавляем вертикальную прокрутку
    scrollbar = Scrollbar(window_for_the_formation_of_the_registry_to_the_court, orient=VERTICAL,
                          command=TABLE_PARAMETERS_register.yview)
    TABLE_PARAMETERS_register.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    NULL_BLOCK = Label(window_for_the_formation_of_the_registry_to_the_court, text='')
    NULL_BLOCK.grid(column=0, sticky=W)

    BUTTON_SAVE_AS_LABEL = Button(window_for_the_formation_of_the_registry_to_the_court, text="Путь сохранения",
                                  font=("Arial", 10, 'bold'), command=save_file)
    BUTTON_SAVE_AS_LABEL.grid(column=0, sticky=W, padx=2)

    NAME_OF_THE_SAVE_ACT_LABEL = Label(window_for_the_formation_of_the_registry_to_the_court, text='')
    NAME_OF_THE_SAVE_ACT_LABEL.grid(column=0, sticky=W, padx=2)

    NULL_BLOCK = Label(window_for_the_formation_of_the_registry_to_the_court, text='')
    NULL_BLOCK.grid(column=0, sticky=W, padx=2)

    TEXT_NAME_DEBTORS_LABEL = Label(window_for_the_formation_of_the_registry_to_the_court, text="Сохранить файл как: ",
                                    font=("Arial", 10, 'bold'))
    TEXT_NAME_DEBTORS_LABEL.grid(column=0, sticky=W, padx=2)

    NAME_DEBTORS_LABEL = Entry(window_for_the_formation_of_the_registry_to_the_court, width=40)
    NAME_DEBTORS_LABEL.insert(0, 'Реестр на подачу в мировой суд')
    NAME_DEBTORS_LABEL.grid(column=0, sticky=W, padx=2)

    NULL_BLOCK = Label(window_for_the_formation_of_the_registry_to_the_court, text='')
    NULL_BLOCK.grid(column=0, sticky=W, padx=2)

    def finish():
        asasas1 = Button(text="РЕЕСТР НА ПОДАЧУ \nВ МИРОВОЙ СУД", font=("Arial", 8, 'bold'),
                         command=REGISTRY_WINDOW_FUNCTION_TO_COURT)
        asasas1.grid(row=16, column=2, rowspan=2)
        window_for_the_formation_of_the_registry_to_the_court.destroy()

    def distribution_function_by_management_companies():
        court_number_8 = []
        court_number_9 = []

        for i in LIST_OF_DEBTORS_FOR_THE_COURT:
            street = ''
            number = ''
            street = i[1][:i[1].find(',')]
            number = i[1][i[1].find(' ') + 1:i[1].find('-')]
            if Database.COURT_NUMBER(street, number) == 'Мировому судье судебного участка №9 \nв Березовском районе Красноярского края \nПашковскому А.Д.':
                court_number_9.append(i)
            elif Database.COURT_NUMBER(street, number) == 'Мировому судье судебного участка №8 \nв Березовском районе Красноярского края \nБелявцевой Е.А.':
                court_number_8.append(i)
            else:
                showerror(title="Ошибка", message=f"Не смогли найти судебный участок по адресу {i[1]}")
                break

        def TEXT_DOCUMENT(list, court_number_s):
            # FOR TRANSMISSION TO DOC
            # list = [[1, ФИО, Адрес, Сумма, УК]]
            number, name, address = [i+1 for i in range(len(list))], [i[1] for i in list], [i[2] for i in list]

            if list[0][4] == 'ООО "СКУ Развитие"':
                Address_UK = '662520 Красноярский край, Березовский район, п. Березовка ул. Юности, пом. 2 каб. 2'
            elif list[0][4] == 'ООО "БСК Плюс"' or list[0][4] == 'ООО "Концепт"':
                Address_UK = '662520 Красноярский край, Березовский район, п. Березовка ул. Юности, д. 19/2'
            else:
                showerror(title="Ошибка", message=f"Не смогли найти управляющую компанию при формировании реестра!")
            text_M_company = list[0][4]
            M_company = list[0][4].replace('"', '')
            date_now = date.today()

            doc = DocxTemplate("court_register.docx")  # DOCUMENT TEMPLATE

            tbl_contents = [{'n_1': n_number, 'n_2': n_name, 'n_3': n_address}
                            for n_number, n_name, n_address in zip(number, name, address)]

            context = {'tbl_contents': tbl_contents, #ЗАПОЛНЕНИЕ ТАБЛИЦЫ ПОСТРОЧНО
                       'm_company': text_M_company,  # НАЗВАНИЕ УК
                       'address_uk' : Address_UK,  # Адрес УК
                       'court_number' : court_number_s, #Номер и адрес суда
                       }

            save_folder_path = NAME_OF_THE_SAVE_ACT_LABEL['text']  # COMPUTER SAVE PATH VARIABLE
            save_name = f'Реестр на подачу в мировой суд {M_company} {court_number_s[15:21]}ый {court_number_s[25:30]}ок {court_number_s[33:35]} от {date_now.day}.{date_now.month}.{date_now.year} года'  # VARIABLE ADDRESS AND APARTMENTS OF THE DEBTOR FOR TEXT FORMAT
            doc.render(context)  # GENERATION OF ALL DATA
            doc.save(f"{save_folder_path}/{save_name}.docx")  # TRANSFER AND SAVING DATA
            showinfo(title="Информация", message=f'Реестр на подачу в мировой суд для {M_company} создан!')

        if len(court_number_8) >= 1:
            for i in court_number_8:
                court_number_s = 'Мировому судье судебного участка №8 в Березовском районе Красноярского края Белявцевой Е.А.'
                SKY_R = []
                BSK_P = []
                KONCEPT = []
                for i in LIST_OF_DEBTORS_FOR_THE_COURT:
                    if i[4] == 'ООО "СКУ Развитие"':
                        SKY_R.append(i)
                    elif i[4] == 'ООО "БСК Плюс"':
                        BSK_P.append(i)
                    elif i[4] == 'ООО "Концепт"':
                        KONCEPT.append(i)
                    else:
                        showerror(title="Ошибка", message=f"Не смогли найти управляющую компанию по адресу {i[2]}")
                        break
                if len(SKY_R) >= 1:
                    n_s = '8'
                    TEXT_DOCUMENT(SKY_R, court_number_s)
                if len(BSK_P) >= 1:
                    n_s = '8'
                    TEXT_DOCUMENT(BSK_P, court_number_s)
                if len(KONCEPT) >= 1:
                    n_s = '8'
                    TEXT_DOCUMENT(KONCEPT, court_number_s)

        if len(court_number_9) >= 1:
            for i in court_number_9:
                court_number_s = 'Мировому судье судебного участка №9 в Березовском районе Красноярского края Пашковскому А.Д.'
                SKY_R = []
                BSK_P = []
                KONCEPT = []
                for i in LIST_OF_DEBTORS_FOR_THE_COURT:
                    if i[4] == 'ООО "СКУ Развитие"':
                        SKY_R.append(i)
                    elif i[4] == 'ООО "БСК Плюс"':
                        BSK_P.append(i)
                    elif i[4] == 'ООО "Концепт"':
                        KONCEPT.append(i)
                    else:
                        showerror(title="Ошибка", message=f"Не смогли найти управляющую компанию по адресу {i[2]}")
                        break
                if len(SKY_R) >= 1:
                    TEXT_DOCUMENT(SKY_R, court_number_s)
                if len(BSK_P) >= 1:
                    TEXT_DOCUMENT(BSK_P, court_number_s)
                if len(KONCEPT) >= 1:
                    TEXT_DOCUMENT(KONCEPT, court_number_s)


        finish()

    window_for_the_formation_of_the_registry_to_the_court.protocol("WM_DELETE_WINDOW", finish)

    CREATE_BUTTON_LABEL = Button(window_for_the_formation_of_the_registry_to_the_court, text="СОЗДАТЬ", font=("Arial", 10, 'bold'),
                                 bg='#79abfc', command=distribution_function_by_management_companies)
    CREATE_BUTTON_LABEL.grid(column=0, sticky=W, padx=2)


# COLLECTION FUNCTION LIST OF EXCLUDED DEBTORS NUMBERS
def delete():
    selection = TABLE_PARAMETERS.selection()[0]
    TABLE_PARAMETERS.delete(selection)
    LIST_OF_EXCLUDED_DEBTORS_NUMBERS.append(selection[3:])
    print(selection)

# LISTING FUNCTION OF ALL REMOTE
def CLEAR_ALL_DATA_FROM_TABLE():
    s = TABLE_PARAMETERS.get_children()
    for i in s:
        all_del.append(i[3:])
        TABLE_PARAMETERS.delete(i)
    general_list_of_debtors.clear()
    general_list_of_debtors_second_window.clear()
    DEBTORS_FULL_NAME_LABEL.delete(0, END)
    DEBTORS_DATE_OF_BIRTH_LABEL.delete(0, END)
    PASSPORT_DATA_OF_THE_DEBTOR_LABEL.delete(0, END)
    DEBTOR_DEBT_LABEL.delete(0, END)
    APARTMENT_NUMBER_LABEL.delete(0, END)
    showinfo(title="Информация", message='Все данные очищены!')


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
        if DEBTORS_FULL_NAME_LABEL.get() == '' or DEBTORS_DATE_OF_BIRTH_LABEL.get() == '':
            return showwarning(title="Ошибка", message="Заполните все поля")
        else:
            if date_of_birth_check_variable == 'Yes':
                if PROPERTY_CONFIRMATION_STR.get() == '1' and REGISTRATION_CHECK_STR.get() == '1' and PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get() == '':  # CHECKING WHETHER THE DEBTOR IS OWNER OR REGISTERED
                    general_list_of_debtors.append((len(general_list_of_debtors) + 1, DEBTORS_FULL_NAME_LABEL.get(),
                                                    DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                                                    'п.д. отсутствуют', '+', '+'))
                    list_for_a_new_debtor.append(
                        (len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         'п.д. отсутствуют', '+', '+'))
                    general_list_of_debtors_second_window.append(
                        [len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         'п.д. отсутствуют'])
                elif PROPERTY_CONFIRMATION_STR.get() == '1' and REGISTRATION_CHECK_STR.get() == '1' and PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get() != '':  # CHECKING WHETHER THE DEBTOR IS OWNER OR REGISTERED
                    general_list_of_debtors.append((len(general_list_of_debtors) + 1, DEBTORS_FULL_NAME_LABEL.get(),
                                                    DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                                                    PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '+', '+'))
                    list_for_a_new_debtor.append(
                        (len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '+', '+'))
                    general_list_of_debtors_second_window.append(
                        [len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get()])
                elif PROPERTY_CONFIRMATION_STR.get() == '1' and REGISTRATION_CHECK_STR.get() == '0' and PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get() == '':
                    general_list_of_debtors.append((len(general_list_of_debtors) + 1, DEBTORS_FULL_NAME_LABEL.get(),
                                                    DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                                                    'п.д. отсутствуют', '+', '-'))
                    list_for_a_new_debtor.append(
                        (len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         'п.д. отсутствуют', '+', '-'))
                    general_list_of_debtors_second_window.append(
                        [len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         'п.д. отсутствуют'])
                elif PROPERTY_CONFIRMATION_STR.get() == '1' and REGISTRATION_CHECK_STR.get() == '0' and PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get() != '':
                    general_list_of_debtors.append((len(general_list_of_debtors) + 1, DEBTORS_FULL_NAME_LABEL.get(),
                                                    DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                                                    PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '+', '-'))
                    list_for_a_new_debtor.append(
                        (len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '+', '-'))
                    general_list_of_debtors_second_window.append(
                        [len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get()])
                elif PROPERTY_CONFIRMATION_STR.get() == '0' and REGISTRATION_CHECK_STR.get() == '1' and PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get() == '':
                    general_list_of_debtors.append((len(general_list_of_debtors) + 1, DEBTORS_FULL_NAME_LABEL.get(),
                                                    DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                                                    'п.д. отсутствуют', '-', '+'))
                    list_for_a_new_debtor.append(
                        (len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         'п.д. отсутствуют', '-', '+'))
                    general_list_of_debtors_second_window.append(
                        [len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         'п.д. отсутствуют'])
                elif PROPERTY_CONFIRMATION_STR.get() == '0' and REGISTRATION_CHECK_STR.get() == '1' and PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get() != '':
                    general_list_of_debtors.append((len(general_list_of_debtors) + 1, DEBTORS_FULL_NAME_LABEL.get(),
                                                    DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                                                    PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '-', '+'))
                    list_for_a_new_debtor.append(
                        (len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '-', '+'))
                    general_list_of_debtors_second_window.append(
                        [len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get()])
                elif PROPERTY_CONFIRMATION_STR.get() == '0' and REGISTRATION_CHECK_STR.get() == '0'and PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get() != '':
                    general_list_of_debtors.append((len(general_list_of_debtors) + 1, DEBTORS_FULL_NAME_LABEL.get(),
                                                    DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                                                    PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '-', '-'))
                    list_for_a_new_debtor.append(
                        (len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get(), '-', '-'))
                    general_list_of_debtors_second_window.append(
                        [len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get()])
                elif PROPERTY_CONFIRMATION_STR.get() == '0' and REGISTRATION_CHECK_STR.get() == '0'and PASSPORT_DATA_OF_THE_DEBTOR_LABEL.get() == '':
                    general_list_of_debtors.append((len(general_list_of_debtors) + 1, DEBTORS_FULL_NAME_LABEL.get(),
                                                    DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                                                    'п.д. отсутствуют', '-', '-'))
                    list_for_a_new_debtor.append(
                        (len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         'п.д. отсутствуют', '-', '-'))
                    general_list_of_debtors_second_window.append(
                        [len(general_list_of_debtors), DEBTORS_FULL_NAME_LABEL.get(), DEBTORS_DATE_OF_BIRTH_LABEL.get(),
                         'п.д. отсутствуют'])
                for person in list_for_a_new_debtor:
                    TABLE_PARAMETERS.insert("", END, values=person[1:])
            else:
                return showwarning(title="Ошибка", message="Вы неверно заполнили поле 'Дата рождения должника'")



# FUNCTION OF CREATING A DATA CHECK WINDOW AND FORMING A JUDICIAL ACT
def VALIDATION_AND_DATA_GENERATION_FUNCTION():
    window = ThemedTk(theme="breeze")
    window.title("Проверьте введенные данные")
    window.geometry("500x300")
    window.iconbitmap('icon.ico')

    # WE FORM LISTS OF DEBTORS WITHOUT DELETES FOR DISPLAY IN THE CONFIRMATION WINDOW AND SEND TO DOC
    for i in set(all_del + LIST_OF_EXCLUDED_DEBTORS_NUMBERS): # ADD TO THE LIST OF DELETES A LIST OF ALL DELETES
        if str(i) not in LIST_OF_EXCLUDED_DEBTORS_NUMBERS:
            LIST_OF_EXCLUDED_DEBTORS_NUMBERS.append(str(i))
    FIRST_LIST_OF_DEBTORS_EXCEPT_EXCLUDED = []
    SECOND_LIST_OF_DEBTORS_EXCEPT_EXCLUDED = []
    for i in general_list_of_debtors_second_window:
        if str(i[0]) not in LIST_OF_EXCLUDED_DEBTORS_NUMBERS:
            FIRST_LIST_OF_DEBTORS_EXCEPT_EXCLUDED.append(i)
    for i in general_list_of_debtors:
        if str(i[0]) not in LIST_OF_EXCLUDED_DEBTORS_NUMBERS:
            SECOND_LIST_OF_DEBTORS_EXCEPT_EXCLUDED.append(i)

    DATA_VERIFICATION_LABEL = Label(window, text="ПРОВЕРЬТЕ ВВЕДЕННЫЕ ДАННЫЕ:", font=("Arial", 10,'bold'))
    DATA_VERIFICATION_LABEL.grid(row=0, column=0, columnspan=4, padx=10)

    DEBTORS_ADDRESS_VERIFICATION_LABEL = Label(window, text=f"Адрес должника(-ов): ул. {BOX_HOUSE.get()} "
                                                            f"д. {BOX_NUMBER.get()} кв. {APARTMENT_NUMBER_LABEL.get()}", font=("Arial", 10, 'bold'))
    DEBTORS_ADDRESS_VERIFICATION_LABEL.grid(row=1, column=0, sticky=W, padx=10)

    AMOUNT_OWED_LABEL = Label(window, text="Сумма задолженности: " + DEBTOR_DEBT_LABEL.get(), font=("Arial", 10, 'bold'))
    AMOUNT_OWED_LABEL.grid(row=2, column=0, sticky=W, padx=10)

    WITHDRAWAL_OF_STATE_DUTY_LABEL = Label(window, text="Сумма гос.пошлины: " + result_of_the_fee_calculation.get(),
                                           font=("Arial", 10, 'bold'))
    WITHDRAWAL_OF_STATE_DUTY_LABEL.grid(row=3, column=0, sticky=W, padx=10)

    DISPLAY_TOTAL_DEBT_LABEL = Label(window, text="Общая сумма задолженности: " + total_debt.get(), font=("Arial", 10, 'bold'))
    DISPLAY_TOTAL_DEBT_LABEL.grid(row=4, column=0, sticky=W, padx=10)

    DISPLAYING_THE_PERIOD_OF_DEBTS_LABEL = Label(window, text=f'Период задолженности: c {BEGINNING_OF_PERIOD.get()} г. по {END_OF_PERIOD.get()} г.', font=("Arial", 10, 'bold'))
    DISPLAYING_THE_PERIOD_OF_DEBTS_LABEL.grid(row=5, column=0, sticky=W, padx=10)

    NULL_BLOCK1_LABEL = Label(window, text="")
    NULL_BLOCK1_LABEL.grid(row=6, column=0, sticky=W, padx=10)

    DISPLAY_OF_DEBTORS_LABEL = Label(window, text="ДОЛЖНИКИ", font=("Arial", 10, 'bold'))
    DISPLAY_OF_DEBTORS_LABEL.grid(row=7, column=0, columnspan=4, padx=10)

    counter_t = 0
    for i in FIRST_LIST_OF_DEBTORS_EXCEPT_EXCLUDED:
        # CREATING A STRING WITHOUT ADDITIONAL CHARACTERS
        v_x = i[1:]
        vv_x = ''
        for j in v_x:
            vv_x += j + ' '
        OUTPUT_TABLE_LABEL = Label(window, text=vv_x, font=("Arial", 10))
        OUTPUT_TABLE_LABEL.grid(row=8 + counter_t, column=0, sticky=W, padx=10, columnspan=4)
        counter_t += 1

    def save_file():
        filepath = filedialog.askdirectory()
        NAME_OF_THE_SAVE_ACT_LABEL['text'] = filepath

    NULL_BLOCK2_LABEL_LABEL = Label(window, text="")
    NULL_BLOCK2_LABEL_LABEL.grid(row=9 + counter_t, column=0, sticky=W, padx=10)

    BUTTON_SAVE_AS_LABEL = Button(window, text="Путь сохранения", font=("Arial", 10,'bold'), command=save_file)
    BUTTON_SAVE_AS_LABEL.grid(row=12 + counter_t, column=0, sticky=W, padx=10)

    NAME_OF_THE_SAVE_ACT_LABEL = Label(window, text='')
    NAME_OF_THE_SAVE_ACT_LABEL.grid(row=13 + counter_t, column=0, sticky=W, padx=10)

    TEXT_NAME_DEBTORS_LABEL = Label(window, text="Сохранить файл как: ", font=("Arial", 10, 'bold'))
    TEXT_NAME_DEBTORS_LABEL.grid(row=10 + counter_t, column=0, sticky=W, padx=10)

    NAME_DEBTORS_LABEL = Entry(window)
    NAME_DEBTORS_LABEL.insert(0, f'{VARIABLE_STREET} {VARIABLE_NUMBER}-{APARTMENT_NUMBER_LABEL.get()}')
    NAME_DEBTORS_LABEL.grid(row=11 + counter_t, column=0, sticky=W, padx=10)

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
                   'debtors': DOC_DATA_GENERATION_FUNCTION(FIRST_LIST_OF_DEBTORS_EXCEPT_EXCLUDED), # DEBTORS
                   'variable_street': VARIABLE_STREET,  # TRANSFER OF THE DEBTOR'S ADDRESS
                   'variable_number': VARIABLE_NUMBER,  # TRANSFER OF THE HOUSE NUMBER OF THE DEBTOR
                   'apartment_variable_number': APARTMENT_NUMBER_LABEL.get(),  # TRANSFER OF THE APARTMENT NUMBER OF THE DEBTOR
                   'amount_debt': DEBTOR_DEBT_LABEL.get(),  # TRANSFER THE AMOUNT OF DEBT
                   'amount_state_fee': result_of_the_fee_calculation.get(),  # TRANSFER STATE DUTY
                   'owners_of_debtors': FUNCTION_OF_COLLECTION_FROM_OWNERS_OF_DEBTORS(SECOND_LIST_OF_DEBTORS_EXCEPT_EXCLUDED), # DEBTORS IN LIST FORMAT
                   'check': FUNCTION_TO_CHECK_REGISTERED_FOR_DOC(SECOND_LIST_OF_DEBTORS_EXCEPT_EXCLUDED),
                   # FORMATION OF THE TEXT DEPENDING ON WHETHER THE REGISTERED DEBTORS
                   'registered_debtors': FUNCTION_OF_COLLECTION_REGISTERED_DEBTORS(SECOND_LIST_OF_DEBTORS_EXCEPT_EXCLUDED), # LIST OF REGISTERED
                   'management_start': MANAGEMENT_START_DATE_LABEL["text"],  # TRANSFER THE STARTING DATE OF MANAGEMENT
                   'debt_period': DEBT_PERIOD_FUNCTION(BEGINNING_OF_PERIOD.get(), END_OF_PERIOD.get()), # DEBT PERIOD
                   'total_debt': total_debt.get(),  # TRANSFER TOTAL DEBT
                   'check_quantity': FUNCTION_TO_CHECK_THE_NUMBER_OF_OBLIGERS_FOR_DOC(SECOND_LIST_OF_DEBTORS_EXCEPT_EXCLUDED),
                   # FORMATION OF THE TEXT DEPENDING ON THE NUMBER OF DEBTORS
                   'list_of_debtors': LIST_OF_DEBTORS_FUNCTION(FIRST_LIST_OF_DEBTORS_EXCEPT_EXCLUDED), # LIST OF DEBTORS
                   }

        save_folder_path = NAME_OF_THE_SAVE_ACT_LABEL['text'] # COMPUTER SAVE PATH VARIABLE
        save_name = NAME_DEBTORS_LABEL.get() # VARIABLE ADDRESS AND APARTMENTS OF THE DEBTOR FOR TEXT FORMAT
        doc.render(context) # GENERATION OF ALL DATA
        doc.save(f"{save_folder_path}/{save_name}.docx") # TRANSFER AND SAVING DATA

    # BUTTON FOR SENDING GENERATED DATA TO THE FUNCTION OF AUTOMATIC GENERATION AND SAVING DATA
    SENDING_FILES_TO_A_DOC_LABEL = Button(window, text="ОТПРАВИТЬ", font=("Arial", 10,'bold'), command=TEXT_DOCUMENT, bg='#79abfc')
    SENDING_FILES_TO_A_DOC_LABEL.grid(row=14 + counter_t, column=0, sticky=W, padx=10)


# FUNCTION OF ADDING DATA TO THE LIST OF PAYMENT OF THE STATE DUTY
def THE_FUNCTION_OF_FORMING_THE_REGISTER_FOR_THE_PAYMENT_OF_THE_STATE_FEE():
    if len(general_list_of_debtors) == 0:
        showerror(title="Ошибка", message="Вы не добавили ни одного должника!")
    else:
        if APARTMENT_NUMBER_LABEL.get() == '' or VARIABLE_STREET == '' or VARIABLE_NUMBER == '':
            showerror(title="Ошибка", message="Вы не указали адрес должника!")
        else:
            if result_of_the_fee_calculation.get() == '' or result_of_the_fee_calculation.get() == 'Сумма введена некорректно':
                showerror(title="Ошибка", message="Укажите сумму задолженности!")
            else:
                p = [len(LIST_OF_THE_REGISTER_OF_THE_STATE_DUTY)+1,f'{VARIABLE_STREET}, {VARIABLE_NUMBER}-{APARTMENT_NUMBER_LABEL.get()}',general_list_of_debtors[0][1], result_of_the_fee_calculation.get(), COMPANY_NAME_LABEL["text"]]
                LIST_OF_THE_REGISTER_OF_THE_STATE_DUTY.append(p)
                showinfo(title="Информация", message=f'В реестр добавлен {general_list_of_debtors[0][1]}')

def THE_FUNCTION_OF_FORMING_A_LIST_OF_DEBTORS_FOR_THE_COURT():
    if len(general_list_of_debtors) == 0:
        showerror(title="Ошибка", message="Вы не добавили ни одного должника!")
    else:
        if APARTMENT_NUMBER_LABEL.get() == '' or VARIABLE_STREET == '' or VARIABLE_NUMBER == '':
            showerror(title="Ошибка", message="Вы не указали адрес должника!")
        else:
            if result_of_the_fee_calculation.get() == '' or result_of_the_fee_calculation.get() == 'Сумма введена некорректно':
                showerror(title="Ошибка", message="Укажите сумму задолженности!")
            else:
                s = ''
                for i in range(len(general_list_of_debtors)):
                    s+= general_list_of_debtors[i][1]
                    if i+1 != len(general_list_of_debtors):
                        s+= ', '
                p = [len(LIST_OF_DEBTORS_FOR_THE_COURT)+1, f'{VARIABLE_STREET}, {VARIABLE_NUMBER}-{APARTMENT_NUMBER_LABEL.get()}', s, JUDICIAL_SECTION_LABEL["text"][:35], COMPANY_NAME_LABEL["text"]]
                LIST_OF_DEBTORS_FOR_THE_COURT.append(p)
                showinfo("Информация", f"В реестр добавлены: {s}")


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
LABEL_SELECT_APARTMENT_NUMBER.grid(row=4, column=0, sticky=NS, pady=5)

# THREE WINDOW PART
APARTMENT_NUMBER_LABEL = Entry(width=10)
APARTMENT_NUMBER_LABEL.grid(row=5, column=0, sticky=NS)
NUMBER_APARTMENT = APARTMENT_NUMBER_LABEL.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

##
## DEBTORS INDICATION BLOCK
##
# TEXT PART
LABEL_DEBTORS_FULL_NAME = Label(text="Укажите ФИО должника", font=("Arial", 10,'bold'))
LABEL_DEBTORS_FULL_NAME.grid(row=6, column=0, sticky=NS, pady=5)

# FOUR WINDOW PART
DEBTORS_FULL_NAME_LABEL = Entry(width=40)
DEBTORS_FULL_NAME_LABEL.grid(row=7, column=0, sticky=NS)
DEBTORS_FULL_NAME = DEBTORS_FULL_NAME_LABEL.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

# DEBTORS DATE OF BIRTH
# TEXT PART
LABEL_DEBTORS_DATE_OF_BIRTH = Label(text="Укажите дату рождения должника", font=("Arial", 10,'bold'))
LABEL_DEBTORS_DATE_OF_BIRTH.grid(row=8, column=0, sticky=NS, pady=5)

# FIVE WINDOW PART
date_debtors = StringVar()
DEBTORS_DATE_OF_BIRTH_LABEL = Entry(width=15, textvariable=date_debtors)
DEBTORS_DATE_OF_BIRTH_LABEL.grid(row=9, column=0, sticky=NS)
DEBTORS_DATE_OF_BIRTH = DEBTORS_DATE_OF_BIRTH_LABEL.get()  # ПОКА ПУСТОЕ ПРИСВАИВАНИЕ, ПОСЛЕ НЕОБХОДИМО ВНЕДРИТЬ С ПРОВЕРКОЙ!

# OUTPUT BLOCK OF INCORRECT INPUT OF DATE OF BIRTH
result_date_of_birth = StringVar()
DATE_OF_BIRTH_VERIFICATION_RESULT = Label(textvariable=result_date_of_birth, foreground='red')
DATE_OF_BIRTH_VERIFICATION_RESULT.grid(row=10, column=0, sticky=NS)
date_debtors.trace_add("write", CHECKING_THE_CORRECT_ENTRY_OF_THE_DATE_OF_BIRTH)

# DEBTORS DATE OF BIRTH
# TEXT PART
LABEL_PASSPORT_DATA_OF_THE_DEBTOR = Label(text="Укажите паспортные данные должника", font=("Arial", 10,'bold'))
LABEL_PASSPORT_DATA_OF_THE_DEBTOR.grid(row=11, column=0, sticky=NS, pady=5)

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

# BLOCK FOR SPECIFYING THE JUDICIAL AREA
LABEL_JUDICIAL_AREA = Label(text="Судебный участок", font=("Arial", 10,'bold'))
LABEL_JUDICIAL_AREA.grid(row=5, column=1, sticky=NS)

# LABEL BLOCK WITH JUDICIAL SECTION
JUDICIAL_SECTION_LABEL = Label(justify=CENTER)
JUDICIAL_SECTION_LABEL.grid(row=6, column=1, sticky=NS,rowspan=3)

# BLOCK FOR MANAGEMENT START DATE
LABEL_MANAGEMENT_START_DATE = Label(text="Дата начала управления МКД", font=("Arial", 10,'bold'))
LABEL_MANAGEMENT_START_DATE.grid(row=8, column=1, sticky=NS)

# LABEL BLOCK WITH MANAGEMENT START DATE
MANAGEMENT_START_DATE_LABEL = Label()
MANAGEMENT_START_DATE_LABEL.grid(row=9, column=1, sticky=NS)

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
BEGINNING_OF_PERIOD = DateEntry(root, width=16, background="grey", date_pattern='dd.mm.yyyy', foreground="white", bd=2, locale='ru_RU')
BEGINNING_OF_PERIOD.grid(row=17, column=1, sticky=NS)

##TEXT PART
LABEL_DEBT_PERIOD2 = Label(text="по", font=("Arial", 10,'bold'))
LABEL_DEBT_PERIOD2.grid(row=18, column=1, sticky=W, padx=50)

# BLOCK END OF PERIOD
END_OF_PERIOD = DateEntry(root, width=16, background="grey", date_pattern='dd.mm.yyyy', foreground="white", bd=2, locale='ru_RU')
END_OF_PERIOD.grid(row=18, column=1, sticky=NS)

# CENTRAL BLOCK
# TABLE

# ZERO BLOCK FOR EMPTY FIELD
ZERO_BLOCK = Label(text="", font=("Arial", 10))
ZERO_BLOCK.grid()

# TABLE CREATION BLOCK
TABLE_HEADINGS = ("name", "date_of_birth", "passport_data", "debtor_owner", "debtor_is_registered")
TABLE_PARAMETERS = Treeview(columns=TABLE_HEADINGS, show="headings")
TABLE_PARAMETERS.grid(row=20, column=0, columnspan=3)

# TABLE HEADING BLOCK
TABLE_PARAMETERS.heading("name", text="ФИО должника")
TABLE_PARAMETERS.heading("date_of_birth", text="Дата рождения должника")
TABLE_PARAMETERS.heading("passport_data", text="Паспортные данные должника")
TABLE_PARAMETERS.heading("debtor_owner", text="Собственник")
TABLE_PARAMETERS.heading("debtor_is_registered", text="Прописан")

TABLE_PARAMETERS.column("#1", stretch=NO, width=200)
TABLE_PARAMETERS.column("#2", stretch=NO, width=200)
TABLE_PARAMETERS.column("#3", stretch=NO, width=300)
TABLE_PARAMETERS.column("#4", stretch=NO, width=85)
TABLE_PARAMETERS.column("#5", stretch=NO, width=85)

# ORDER FORMATION BUTTON
DATA_CHECK_BUTTON = Button(text="СФОРМИРОВАТЬ ПРИКАЗ", font=("Arial", 8,'bold'), command=VALIDATION_AND_DATA_GENERATION_FUNCTION, bg='#79abfc')
DATA_CHECK_BUTTON.grid(row=2, column=2)

# BUTTON FOR SENDING DEBTORS TO THE LIST FOR PAYMENT OF STATE DUTIES
BUTTON_PAYMENT_OF_STATE_DUTIES = Button(text="ДОБАВИТЬ В РЕЕСТР НА \nОПЛАТУ ГОСПОШЛИНЫ", font=("Arial", 8,'bold'), bg='#79abfc', command=THE_FUNCTION_OF_FORMING_THE_REGISTER_FOR_THE_PAYMENT_OF_THE_STATE_FEE)
BUTTON_PAYMENT_OF_STATE_DUTIES.grid(row=3, column=2, rowspan=2)

# BUTTON FOR SENDING DEBTORS TO THE LIST TO SEND TO COURT
BUTTON_SEND_TO_COURT = Button(text="ДОБАВИТЬ В РЕЕСТР НА \nПОДАЧУ В МИРОВОЙ СУД", font=("Arial", 8,'bold'), bg='#79abfc', command=THE_FUNCTION_OF_FORMING_A_LIST_OF_DEBTORS_FOR_THE_COURT)
BUTTON_SEND_TO_COURT.grid(row=5, column=2, rowspan=2)

#####
asasas = Button(text="РЕЕСТР НА ОПЛАТУ \nГОСПОШЛИНЫ", font=("Arial", 8,'bold'), command=STATE_DUTY_REGISTRY_WINDOW_FUNCTIONS)
asasas.grid(row=14, column=2, rowspan=2)

#####
asasas1 = Button(text="РЕЕСТР НА ПОДАЧУ \nВ МИРОВОЙ СУД", font=("Arial", 8,'bold'), command=REGISTRY_WINDOW_FUNCTION_TO_COURT)
asasas1.grid(row=16, column=2, rowspan=2)


root.resizable(False, False)
root.iconbitmap('icon.ico')
root.mainloop()