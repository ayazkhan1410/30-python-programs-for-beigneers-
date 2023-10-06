
'''
Day 21 of '30 days of 30
Programs challenege '''


'''
Play a YouTube video:
using Python
'''

import pywhatkit as p

try:
    p.playonyt("https://www.youtube.com/watch?v=hzSY6yKEGhk&t=13s&ab_channel=WaheedIslamicTV")
except:
    print("Network error")

