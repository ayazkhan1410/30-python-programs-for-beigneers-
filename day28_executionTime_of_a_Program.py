'''
Day 28 of '30 days of 30
Programs challenege 
'''

'''
Use Time Module 
Measure execution time
of a program

'''
import time as t

start = t.time()

t.sleep(2)

end = t.time()

total = end - start

print(f"Elapsed time: {total} seconds")
