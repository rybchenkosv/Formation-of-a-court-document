data = [[1,'FIO','22.05.1995','pd ots'], [2,'FIOSS','22.05.2323','pd ots']]
data1 = [[1,'FIO','22.05.1995','pd ots v lice zak pred']]

def DOC_DATA_GENERATION_FUNCTION(data,data1):
    assembly_variable = ''
    for i in range(len(data1)):
        for j in range(len(data)):
            if data1[i][1] == data[j][1] and data1[i][2] == data[j][2]:
                data[j][3] = data1[i][3]
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


def LIST_OF_DEBTORS_FUNCTION(data, data1):
    assembly_variable = ''
    for i in range(len(data1)):
        for j in range(len(data)):
            if data1[i][1] == data[j][1] and data1[i][2] == data[j][2]:
                data[j][3] = data1[i][3]
    for i in data:
        z = 0
        for j in range(len(i)):
            if j != 0:
                if j == 2:
                    assembly_variable += i[j] + ' года рождения'
                    assembly_variable += ' '
                else:
                    assembly_variable += i[j]
                    if z == 0:
                        assembly_variable += ' '
                        z+=1
        if i != data[len(data)-1]:
            assembly_variable += ', '
    return assembly_variable

print(LIST_OF_DEBTORS_FUNCTION(data, data1))