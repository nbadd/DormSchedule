import datetime
from datetime import timedelta

from datetime import date
d0 = date(2017, 9, 7)
year = [d0]
count = 0
while count < 39:
    d0 = d0 + timedelta(days = 7)
    year.append(d0)
    count+=1
print (year)
