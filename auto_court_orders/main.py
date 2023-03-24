NAME_DEBROT = input()
SURNAME_DEBTOR = input()
ADDRESS_NAME = input()
ADDRESS_NUMBER = None #ПОКА НЕ РЕАЛИЗОВАННАЯ ФУНКЦИЯ

RECOVERER = []
COURT_NUMBER = ['Мировому судье судебного участка №9 в Березовском районе Красноярского края Пашковскому А.Д.'
                if ADDRESS_NAME in JUDICIAL_PRECINCT_9
                else 'Мировому судье судебного участка №8 в Березовском районе Красноярского края Белявцевой Е.А.']

DEBTORS = {i:[input('Full name of the debtor: '),input('Date of birth of the debtor: '),input('Debtors passport details: ')]
           for i in range(1, int(input('Number of debtors: ')) + 1)}

TOTAL_DEBT = AMOUNT_OF_THE_STATE_FEE + AMOUNT_OF_DEBT

#OPERATIONS RELATED TO REGISTERED AND RESIDENTIAL OWNERS
REGISTERED_DEBTORS = None #ПОКА НЕ РЕАЛИЗОВАННАЯ ФУНКЦИЯ
PROPERTY_OWNERS = None #ПОКА НЕ РЕАЛИЗОВАННАЯ ФУНКЦИЯ

DEBT_PERIOD = f'с {input("Enter the beginning of the debt period: ")} г.' \
              f'по {input("Enter the end of the debt period: ")} г.'

SOLIDARY_DEBT = None #ПОКА НЕ РЕАЛИЗОВАННАЯ ФУНКЦИЯ