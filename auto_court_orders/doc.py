from docxtpl import DocxTemplate
from frontend import main

doc = DocxTemplate("shablonsydybprik.docx")

context = { 'name_of_the_court' : main.JUDICIAL_SECTION_LABEL["text"],  #TRANSFERRING COURT DATA
            'claimant' : main.COMPANY_NAME_LABEL["text"],  #TRANSFER OF CLAIMANTS
            'address_claimant' : main.COMPANY_ADDRESS_LABEL["text"],  #TRANSFER ADDRESS CLAIMANT
            '' : xxxx,  #УКАЗАНИЕ ДОЛЖНИКОВ ПОКА ПОД ВОПРОСОМ!
            'variable_street' : main.VARIABLE_STREET,  #ВЫБОР АДРЕСА ПОКА ПОД ВОПРОСОМ!
            'variable_number' : main.VARIABLE_NUMBER, #ВЫБОР НОМЕРА ДОМА
            'apartment_variable_number' : main.APARTMENT_NUMBER_LABEL.get(), #ВЫБОР НОМЕРА КВАРТИРЫ
            'amount_debt' : main.DEBTOR_DEBT_LABEL.get(),  #TRANSFER THE AMOUNT OF DEBT
            'amount_state_fee' : main.result_of_the_fee_calculation.get(),  #TRANSFER STATE DUTY
            '' : xxx, #СПИСОК СОБСТВЕННИКОВ
            '' : ddd, #СОСТОЯТ ИЛИ НИКТО НЕ СОСТОИТ ПРОПИСАННЫМИ
            '' : yyy, #СПИСОК ПРОПИСАННЫХ
            'management_start' : main.MANAGEMENT_START_DATE_LABEL["text"],  #TRANSFER THE STARTING DATE OF MANAGEMENT
            'debt_period' : main.DEBT_PERIOD,  #TRANSFER DEBT PERIOD не сделал
            'total_debt' : main.total_debt.get(),  #TRANSFER TOTAL DEBT
            '' : ccc, #прописать зависимость в солидарном порядке или нет
            }

save_folder_path = main.NAME_OF_THE_SAVE_ACT_LABEL['text']
save_name = main.NAME_DEBTORS_LABEL.get()
doc.render(context)
doc.save(f"{save_folder_path}/{save_name}.docx")
