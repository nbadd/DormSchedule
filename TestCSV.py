import csv
import sys

with open('Schedule.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
f.close()
