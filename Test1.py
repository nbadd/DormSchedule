import datetime
from datetime import timedelta
from datetime import date

import random

import csv
#Lists of faculty for each weekday group
monday = ['Monday']
tuesday = ['Tuesday']
wednesday = ['Wednesday']
thursday = ['Thursday']
friday = ['Friday']
saturday = ['Saturday']
sunday = ['Sunday']
year = []

testFaculty = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn'
faculty = testFaculty.split(',') #Create list of faculty for testing

firstDay = input('Input the integer day of the first Sunday of the school year:')

d0 = date(2017, 9, int(firstDay)) #First Sunday of the year
year = [d0 + timedelta(days=d) for d in range(40*7)]

floater = [str(x) for x in range(8)] #Create floater list for testing
floater.insert(0,'Floater')

# print('Input list of faculty separated by spaces:')
# f = input()
# faculty = f.split(' ')
# print(faculty)

#Assign the random faculty groups
for x in range(8):
    count = random.randint(0,len(faculty)-1)
    sunday.append(faculty[count])
    faculty.remove(faculty[count])

    count = random.randint(0,len(faculty)-1)
    monday.append(faculty[count])
    faculty.remove(faculty[count])

    count = random.randint(0,len(faculty)-1)
    tuesday.append(faculty[count])
    faculty.remove(faculty[count])

    count = random.randint(0,len(faculty)-1)
    wednesday.append(faculty[count])
    faculty.remove(faculty[count])

    count = random.randint(0,len(faculty)-1)
    thursday.append(faculty[count])
    faculty.remove(faculty[count])

week = [sunday, monday, tuesday, wednesday, thursday, friday, saturday]
countyear = 0
countday = 0
countweek = 0
with open('Schedule.csv', 'w') as f:
    writer = csv.writer(f)
    while (countyear < len(year)): #Years
        countweek = 6
        #while (countweek > 0): #Weeks
        for x in range(6):
            countday = 0
            while (countday < len(week) and countyear < len(year)): #Days
                if (countday == 6):
                    week[countday].insert(0,year[countyear])
                    if (countweek == 1):
                        week[countday].extend(floater)
                        writer.writerow(week[countday])
                    else:
                        week[countday].extend(week[countday - countweek])
                        writer.writerow(week[countday])

                    week[countday] = ['Saturday']
                    countweek -= 1
                else:
                    week[countday].insert(0,year[countyear])
                    writer.writerow(week[countday])
                    week[countday].remove(week[countday][0])

                countyear += 1
                countday += 1
f.close()
