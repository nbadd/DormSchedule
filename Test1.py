import datetime
from datetime import timedelta
from datetime import date

import random

import csv
testFaculty = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn'

dM = date(2017, 9, 11)
dT = date(2017, 9, 5)
dW = date(2017, 9, 6)
dTh = date(2017, 9, 7)
dF = date(2017, 9, 8)
dSat = date(2017, 9, 9)
dSun = date(2017, 9, 10)
year = [dT,dW,dTh,dF,dSat,dSun,dM]
count = 0
while count < 39:
    dT = dT + timedelta(days = 7)
    year.append(dT)
    dW = dW + timedelta(days = 7)
    year.append(dW)
    dTh = dTh + timedelta(days = 7)
    year.append(dTh)
    dF = dF + timedelta(days = 7)
    year.append(dF)
    dSat = dSat + timedelta(days = 7)
    year.append(dSat)
    dSun = dSun + timedelta(days = 7)
    year.append(dSun)
    dM = dM + timedelta(days = 7)
    year.append(dM)
    count+=1

monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
saturday = []
sunday = []
weekend = []
faculty = []
floater = []
count = 0
faculty = testFaculty.split(',')

for x in range(8):
    floater.append(str(x))

# print('Input list of faculty separated by spaces:')
# f = input()
# faculty = f.split(' ')
# print(faculty)

for x in range(8):
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


#print(monday, tuesday, wednesday, thursday)



#print(year)tuesday.insert(0,year[1])mondaytuesday
week = [monday,tuesday,wednesday,thursday, friday, saturday, sunday]
countyear = 0
countweek = 0
countweekend = 0
with open('Schedule.csv', 'w') as f:
    writer = csv.writer(f)
    while (countyear < len(year)):
        tempDay = 5
        while (tempDay > 0):
            countweek = 0

            while (countweek < len(week)):
                if countweek == 5:
                    week[countweek].insert(0,year[countyear])
                    week[countweek].extend(week[countweek - tempDay])
                    if tempDay == 1:
                        week[countweek].extend(floater)
                        writer.writerow(week[countweek])
                    else:
                        writer.writerow(week[countweek])
                    week[countweek] = []

                    tempDay -= 1
                    countyear +=1
                else:
                    week[countweek].insert(0,year[countyear])
                    writer.writerow(week[countweek])
                    week[countweek].remove(week[countweek][0])
                    countyear += 1

                countweek +=1

f.close()
