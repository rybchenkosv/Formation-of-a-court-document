from docxtpl import DocxTemplate
import Database, main

doc = DocxTemplate("shablonsydybprik.docx")

context = { 'name_of_the_court' : main.COURT_NUMBER,  #TRANSFERRING COURT DATA
            'claimant' : Database.NAME_OF_THE_CLAIMANT,  #TRANSFER OF CLAIMANTS
            'address_claimant' : Database.ADDRESS_OF_THE_CLAIMANT,  #TRANSFER ADDRESS CLAIMANT
            '' : main.DEBTORS,  #УКАЗАНИЕ ДОЛЖНИКОВ ПОКА ПОД ВОПРОСОМ!
            '' : None,  #ВЫБОР АДРЕСА ПОКА ПОД ВОПРОСОМ!
            'amount_debt' : main.AMOUNT_OF_DEBT,  #TRANSFER THE AMOUNT OF DEBT
            'amount_state_fee' : main.AMOUNT_OF_THE_STATE_FEE,  #TRANSFER STATE DUTY
            'management_start' : Database.MANAGEMENT_START_DATE,  #TRANSFER THE STARTING DATE OF MANAGEMENT
            'debt_period' : main.DEBT_PERIOD,  #TRANSFER DEBT PERIOD
            'total_debt' : main.TOTAL_DEBT,  #TRANSFER TOTAL DEBT
            }

doc.render(context)
doc.save(f"{Streetdolg}, {Numberhomdolg}-{KVnumberhomdolg} {n1}.docx")