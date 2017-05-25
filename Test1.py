import datetime
from datetime import timedelta
from datetime import date

import random

import csv

#Lists of faculty for each weekday group
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
saturday = []
sunday = []

testFaculty = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn'
faculty = testFaculty.split(',') #Create test list of faculty for testing

firstDay = input('Input the integer day of the first Sunday of the school year:')

d0 = date(2017, 9, int(firstDay)) #First Sunday of the year

year = [d0 + timedelta(days=d) for d in range(40*7)] #Array of all dates

floater = [str(x) for x in range(8)] #Create floater list for testing

#Input the list of faculty working in the dorms
#Must be at least 40 in length
# print('Input list of faculty last names separated by spaces:')
# f = input()
# faculty = f.split(' ')
# print(faculty)

#Assign the random faculty groups
for x in range(8):
    count = random.randint(0,len(faculty)-1) #Sunday faculty group
    sunday.append(faculty[count])
    faculty.remove(faculty[count])

    count = random.randint(0,len(faculty)-1) #Monday faculty group
    monday.append(faculty[count])
    faculty.remove(faculty[count])

    count = random.randint(0,len(faculty)-1) #Tuesday faculty group
    tuesday.append(faculty[count])
    faculty.remove(faculty[count])

    count = random.randint(0,len(faculty)-1) #Wednesday faculty group
    wednesday.append(faculty[count])
    faculty.remove(faculty[count])

    count = random.randint(0,len(faculty)-1) #Thursday faculty group
    thursday.append(faculty[count])
    faculty.remove(faculty[count])

week = [sunday, monday, tuesday, wednesday, thursday, friday, saturday]
    #Array of all faculty groups

with open('Schedule.csv', 'w') as f: #Open the csv Schedule
    writer = csv.writer(f)
    countyear = 0

    while (countyear < len(year)): #Iterates through one year
        countweek = 0

        for x in range(6): #Iterates through one cycle of weeks
            countday = 0

            while (countday < len(week) and countyear < len(year)):
                #Iterates through one week
                if (countday == 6): #If it is Saturday, assign weekend duty
                    week[countday].insert(0,year[countyear])

                    if (countweek == 5): #If it is week 7, Assign floaters
                        week[countday].extend(floater)
                        writer.writerow(week[countday])

                    else:
                        week[countday].extend(week[countweek])
                        writer.writerow(week[countday])

                    week[countday] = []
                    countweek += 1

                #Swap in floaters if it is weekend duty's day
                elif (countday == countweek and countday != 5):
                    floater.insert(0,year[countyear])
                    writer.writerow(floater)
                    floater.remove(floater[0])

                #Does the normal assignment of faculty to a day
                else:
                    week[countday].insert(0,year[countyear])
                    writer.writerow(week[countday])
                    week[countday].remove(week[countday][0])

                countyear += 1 #Increment the counter integers
                countday += 1
f.close()
