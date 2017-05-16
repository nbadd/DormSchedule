import datetime
from datetime import timedelta
from datetime import date

import random

testFaculty = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn'

monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
faculty = []
floater = []

faculty = testFaculty.split(',')

#testFloater = str(x) for x in range(1,11)
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

    count = random.randint(0,len(faculty)-1)
    friday.append(faculty[count])
    faculty.remove(faculty[count])
    x += 1

    print(monday, tuesday, wednesday, thursday, friday)


d0 = date(2017, 9, 7)
year = [d0]
count = 0
while count < 39:
    d0 = d0 + timedelta(days = 7)
    year.append(d0)
    count+=1
