from docxtpl import DocxTemplate
from frontend import main

class MyClass():
    #THE FUNCTION OF FORMING FROM THE RECEIVED DATA A STRING WITH \n HYPHENATIONS
    #FOR TRANSMISSION TO DOC
    def DOC_DATA_GENERATION_FUNCTION(data):
        assembly_variable = ''
        for i in data:
            for j in range(len(i)):
                if j != 0:
                    if j == 2:
                        assembly_variable+= i[j] + ' года рождения'
                        assembly_variable+= '\n'
                    else:
                        assembly_variable+= i[j]
                        assembly_variable+= '\n'
            assembly_variable+='\n'
        return assembly_variable

    def FUNCTION_OF_COLLECTION_FROM_OWNERS_OF_DEBTORS(data):
        assembly_variable = ''
        for i in data:
            if i[4] == '+':
                assembly_variable+= i[1] + ', '
        return assembly_variable[:len(assembly_variable)-2]

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
            return 'в солидарном порядке с следующих должников'
        else:
            return 'с следующих должников'

    def LIST_OF_DEBTORS_FUNCTION(data):
        assembly_variable = ''
        for i in data:
            for j in range(len(i)):
                if j != 0:
                    if j == 2:
                        assembly_variable+= i[j] + ' года рождения'
                        assembly_variable += ', '
                    else:
                        assembly_variable+= i[j] + ' '
        return assembly_variable

    def DEBT_PERIOD_FUNCTION(start, end):
        text = 'c ' + start + ' по ' + end
        return text

    doc = DocxTemplate("shablonsydybprik.docx")

    context = { 'name_of_the_court' : main.JUDICIAL_SECTION_LABEL["text"],  #TRANSFERRING COURT DATA
                'claimant' : main.COMPANY_NAME_LABEL["text"],  #TRANSFER OF CLAIMANTS
                'address_claimant' : main.COMPANY_ADDRESS_LABEL["text"],  #TRANSFER ADDRESS CLAIMANT
                'debtors' : DOC_DATA_GENERATION_FUNCTION(main.general_list_of_debtors_second_window),  #УКАЗАНИЕ ДОЛЖНИКОВ ПОКА ПОД ВОПРОСОМ!
                'variable_street' : main.VARIABLE_STREET,  #ВЫБОР АДРЕСА
                'variable_number' : main.VARIABLE_NUMBER, #ВЫБОР НОМЕРА ДОМА
                'apartment_variable_number' : main.APARTMENT_NUMBER_LABEL.get(), #ВЫБОР НОМЕРА КВАРТИРЫ
                'amount_debt' : main.DEBTOR_DEBT_LABEL.get(),  #TRANSFER THE AMOUNT OF DEBT
                'amount_state_fee' : main.result_of_the_fee_calculation.get(),  #TRANSFER STATE DUTY
                'owners_of_debtors' : FUNCTION_OF_COLLECTION_FROM_OWNERS_OF_DEBTORS(main.general_list_of_debtors), #СПИСОК СОБСТВЕННИКОВ
                'check' : FUNCTION_TO_CHECK_REGISTERED_FOR_DOC(main.general_list_of_debtors), #СОСТОЯТ ИЛИ НИКТО НЕ СОСТОИТ ПРОПИСАННЫМИ
                'registered_debtors' : FUNCTION_OF_COLLECTION_REGISTERED_DEBTORS(main.general_list_of_debtors), #СПИСОК ПРОПИСАННЫХ
                'management_start' : main.MANAGEMENT_START_DATE_LABEL["text"],  #TRANSFER THE STARTING DATE OF MANAGEMENT
                'debt_period' : DEBT_PERIOD_FUNCTION(main.BEGINNING_OF_PERIOD.get(), main.END_OF_PERIOD.get()),  #период задолженности
                'total_debt' : main.total_debt.get(),  #TRANSFER TOTAL DEBT
                'check_quantity' : FUNCTION_TO_CHECK_THE_NUMBER_OF_OBLIGERS_FOR_DOC(main.general_list_of_debtors), #прописать зависимость в солидарном порядке или нет
                'list_of_debtors' : LIST_OF_DEBTORS_FUNCTION(main.general_list_of_debtors_second_window), # список должников в строчку
                }

    save_folder_path = main.NAME_OF_THE_SAVE_ACT_LABEL['text']
    save_name = main.NAME_DEBTORS_LABEL.get()
    doc.render(context)
    doc.save(f"{save_folder_path}/{save_name}.docx")
