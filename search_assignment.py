import openpyxl as xl


def list_from_xl(sheet):
    all_data = list(sheet.rows)
    mylist = []

    for i in range(0, len(all_data)):
        temp = []
        for j in range(0, len(all_data[i])):
            if all_data[i][j].value != None:
                if type(all_data[i][j].value) == str:
                    temp.append(all_data[i][j].value.replace(' ',''))
        mylist.append(temp)
    return mylist


def search_in_list(mylist, word):
    word = word.replace(' ','')
    for i in range (0, len(mylist)):
        for j in range(1, len(mylist[i])):
            if mylist[i][j] == word:
                return mylist[i][0]
    return 'Word not found!'

#######################################################################

xl_sheet = xl.load_workbook('Test1.xlsx')
sheet = xl_sheet['Sheet1']

word = '  ਛੇਤੀ ਝੜ ਜਾਣ ਵਾਲੇ (ਜੀਵ ਤੇ ਬੂਟੇ)  '
mylist = list_from_xl(sheet)
print(search_in_list(mylist, word))