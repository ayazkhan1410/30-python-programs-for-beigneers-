'''
Day 23 of '30 days of 30
Programs challenege '''

'''
Get information on 
particular topic: 
using Python
'''

import pywhatkit as p

try:
    p.info("Reason of Pakistan economy crisis", lines = 5)
    print("Searched successfully...")
except:
    print("Network error")

