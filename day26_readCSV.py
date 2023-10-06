'''
Day 26 of '30 days of 30
Programs challenege 
'''

'''
Use CSV Module 
Read data from 
a CSV file:

'''

import csv

with open('ayaz.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)




