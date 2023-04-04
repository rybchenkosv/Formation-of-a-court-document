#HOUSING FUND
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
OOO_BSK_PLUS = {
    'Мичурина':['1','2','3','4','5','6','7','8','9','11','12','13','14','16','17','18','19','20'],
    'Сурикова':['9','11','13','15'],
    'Тургенева':['1','2','3','6','7','8','9','10','11','12','14'],
    'Ленина':['12'],
    'Маяковского':['7'],
    'Нестерова':['12','14','16','18','20'],
    'Пархоменко':['1','3','3А','5','5А'],
    'Советская':['42'],
    'Солнечная':['3','6','18','20'],
    'Строителей':['6'],
    'Центральная':['8Б','46','56','65']
}
OOO_KONCEPT = {
    'Парковая':['1','3','6','8'],
    'Центральная':['45','47','48','50','51','53','55','57','59','61','63','67'],
    'Дзержинского':['17','38'],
    'Горького':['15','17'],
    'Полевая':['2А'],
    'Калинина':['1','2','3'],
    'Октябрьская':['4','5','6','7','8','9','10'],
    'Олейникова':['64'],
    'Советская':['40','52','53'],
    'Солнечная':['8','10','12'],
    'Строителей':['1','2','3','5','7','9'],
    'Сурикова':['3','5','7'],
    'Юбилейный':['2','4'],
    'Юности':['5'],
    'Дружбы':['96','98','100','102','104','106','108','108А','112','114','114А','116','118','120Б','124','132','136','138','142','144'],
    'Заводская':['55']
}
RESIDENTIAL_FUND = {
    'Береговая':['36','38','40','42Б','44','46'],
    'Дружбы':['1','1А','1Б','1Г','19','96','98','100','102','104','106','108','108А','112','114','114А','116','118','120Б','124','132','136','138','142','144'],
    'Маяковского':['7','9','19','21','23'],
    'Мичурина':['1','1Б','2','2Б','3','4','5','6','7','8','9','11','12','13','14','16','17','18','19','20'],
    'Парковая':['1','2А','3','6','8'],
    'Пархоменко':['1','1А','3','3А','5','5А'],
    'Советской Армии':['20'],
    'Советская':['1А','40','42','43А','45','46','52','53'],
    'Строителей':['1А','1','2А','2','3','5','6','7','9'],
    'Сурикова':['3','5','7','8','9','10','11','12','13','14','15','24','26','28','30'],
    'Центральная':['8Б','42','45','46','47','48','50','51','53','55','56','57','58','59','61','63','65','67'],
    'Ленина':['12'],
    'Солнечная':['3','6','8','10','12','18','20'],
    'Нестерова':['12','14','16','18','20'],
    'Тургенева':['1','2','3','6','7','8','9','10','11','12','14'],
    'Чкалова':['19'],
    'Октябрьская': ['4', '5', '6', '7', '8', '9', '10'],
    'Олейникова': ['64'],
    'Горького':['15','17'],
    'Дзержинского':['17','38'],
    'Калинина':['1','2','3'],
    'Полевая':['2А','70','72'],
    'Юбилейный': ['2', '4'],
    'Юности': ['5'],
    'Заводская': ['55']
}


#JURISDICTION OF THE COURT
JUDICIAL_PRECINCT_9 = ['Белинского', 'Горького', 'Заводская', 'Калинина', 'Маяковского', 'Мичурина',
                       'Нестерова', 'Октябрьская', 'Советской Армии', 'Сурикова', 'Солнечная',
                       'Тургенева',{'Дружбы':['1', '1А', '1Б', '1Г', '19']},'Полевая']

JUDICIAL_PRECINCT_8 = ['Береговая', 'Дзержинского', {'Дружбы':['96','98','100','102','104','106','108','108А','112','114','114А','116','118','120Б','124','132','136','138','142','144']},
                       'Ленина','Парковая','Строителей','Пархоменко','Советская','Центральная','Чкалова','Юбилейный','Юности','Олейникова']


def NAME_OF_THE_CLAIMANT(street,number):
    if street in OOO_CKY_RAZVITYE and number in OOO_CKY_RAZVITYE[street]:
        return 'ООО "СКУ Развитие"'
    elif street in OOO_BSK_PLUS and number in OOO_BSK_PLUS[street]:
        return 'ООО "БСК Плюс"'
    elif street in OOO_KONCEPT and number in OOO_KONCEPT[street]:
        return 'ООО "Концепт"'
    else:
        return 'ОШИБКА. Управляющая компания не найдена.'

def ADDRESS_OF_THE_CLAIMANT(street,number):
    if street in OOO_CKY_RAZVITYE and number in OOO_CKY_RAZVITYE[street]:
        return '662520 Красноярский край, Березовский район, \nп. Березовка ул. Юности, пом. 2 каб. 2'
    elif street in OOO_BSK_PLUS and number in OOO_BSK_PLUS[street]:
        return '662520 Красноярский край, Березовский район, \nп. Березовка ул. Юности, д. 19/2'
    elif street in OOO_KONCEPT and number in OOO_KONCEPT[street]:
        return '662520 Красноярский край, Березовский район, \nп. Березовка ул. Юности, д. 19/2'
    else:
        return ''

def COURT_NUMBER(street,number):
    if street in JUDICIAL_PRECINCT_9:
        return 'Мировому судье судебного участка №9 \nв Березовском районе Красноярского края \nПашковскому А.Д.'
    elif street == 'Дружбы' and number in JUDICIAL_PRECINCT_9[12][street]:
        return 'Мировому судье судебного участка №9 \nв Березовском районе Красноярского края \nПашковскому А.Д.'
    elif street in JUDICIAL_PRECINCT_8:
        return 'Мировому судье судебного участка №8 \nв Березовском районе Красноярского края \nБелявцевой Е.А.'
    elif street == 'Дружбы' and number in JUDICIAL_PRECINCT_8[2][street]:
        return 'Мировому судье судебного участка №8 \nв Березовском районе Красноярского края \nБелявцевой Е.А.'
    else:
        return 'ОШИБКА! Не найден судебный участок!'

def COURT_NUMBER_FOR_BAILIFFS(street,number):
    if street in JUDICIAL_PRECINCT_9:
        return 'мировым судьей судебного участка №9 в Березовском районе Красноярского края Пашковским А.Д.'
    elif street == 'Дружбы' and number in JUDICIAL_PRECINCT_9[12][street]:
        return 'мировым судьей судебного участка №9 в Березовском районе Красноярского края Пашковским А.Д.'
    elif street in JUDICIAL_PRECINCT_8:
        return 'мировым судьей судебного участка №8 в Березовском районе Красноярского края Белявцевой Е.А.'
    elif street == 'Дружбы' and number in JUDICIAL_PRECINCT_8[2][street]:
        return 'мировым судьей судебного участка №8 в Березовском районе Красноярского края Белявцевой Е.А.'
    else:
        return 'ОШИБКА! Не найден судебный участок!'


def MANAGEMENT_START_DATE(street,number):
    if street in OOO_CKY_RAZVITYE and number in OOO_CKY_RAZVITYE[street]:
        return '2019 года'
    elif street in OOO_BSK_PLUS and number in OOO_BSK_PLUS[street]:
        return '2020 года'
    elif street in OOO_KONCEPT and number in OOO_KONCEPT[street]:
        return '2020 года '
    else:
        return 'ОШИБКА! Невозможно найти дату начала управления!'

def AMOUNT_OF_THE_STATE_FEE(AMOUNT_OF_DEBT):
    if AMOUNT_OF_DEBT <= float(10000):
        return '{:.2f}'.format(float(200))
    elif AMOUNT_OF_DEBT <= float(20001):
        return '{:.2f}'.format(AMOUNT_OF_DEBT / 100 * 2)
    else:
        return '{:.2f}'.format(400 + (AMOUNT_OF_DEBT - 20000) / 100 * 1.5)

