import xlrd
workbook = xlrd.open_workbook('DormFaculty.xls', on_demand = True)
worksheet = workbook.sheet_by_index(0)

column = 0
row = 0
#list with unverified emails#
list1 = []
#list with verified emails
list2 = []

number_of_faculty = len(worksheet.col(0)) -1
while(row <= number_of_faculty):
    s = worksheet.cell(row, column).value
    if s.find("cranbrook.edu") == -1:
        list1.append(s)
    else:
        list2.append(s)
    row +=1
print ('Emails do not belong to Cranbrook:', list1)
# print (list1)
print ('Verified Emails', list2)
# print (list2)
