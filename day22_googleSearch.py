'''
Day 22 of '30 days of 30
Programs challenege '''

'''
Perform Google Search
using Python
'''

import pywhatkit as p

try:
    p.search("Python")
    print("Successfully searched")
except:
    print("NETWORK ERROR..")