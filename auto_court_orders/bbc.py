from docxtpl import DocxTemplate
d = [[1, 'фывфыв', '22.05.1995', 'фывфывфв'], [2, 'фывфыв', '22.05.1995', 'фывфывфв'],
     [3, 'фывфыв', '22.05.1995', 'фывфывфв'], [4, 'фывфыв', '22.05.1995', 'фывфывфв']]

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

doc = DocxTemplate("testing.docx")


context = { 'btc' : DOC_DATA_GENERATION_FUNCTION(d),  #TRANSFERRING COURT DATA

            }


doc.render(context)
doc.save("test1.docx")
