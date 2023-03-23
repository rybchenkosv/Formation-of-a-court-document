from auto_court_orders import Database

d = 'Калинина'
g = '1'

def RESPONSIBLE_MANAGEMENT_COMPANY(d,g):
    if d in Database.OOO_CKY_RAZVITYE:
        if g in Database.OOO_CKY_RAZVITYE[d]:
            return 'ООО "СКУ Развитие"'

    elif d in Database.OOO_BSK_PLUS:
        if g in Database.OOO_BSK_PLUS[d]:
            return 'ООО "БСК Плюс"'

    elif d in Database.OOO_KONCEPT:
        if g in Database.OOO_KONCEPT[d]:
            return 'ООО "КОНЦЕПТ"'

    else:
        return 'ОШИБКА. Управляющая компания не найдена.'

print(RESPONSIBLE_MANAGEMENT_COMPANY(d,g))


