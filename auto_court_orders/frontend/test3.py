d = [[1, 'фывфыв', '22.05.1995', 'фывфывфв'], [2, 'фывфыв', '22.05.1995', 'фывфывфв'],
     [3, 'фывфыв', '22.05.1995', 'фывфывфв'], [4, 'фывфыв', '22.05.1995', 'фывфывфв']]

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

print(LIST_OF_DEBTORS_FUNCTION(d))