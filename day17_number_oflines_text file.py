'''Day 17 of '30 days of 30
   Programs challenege '''
   

'''
Write a Python Program
to count the number of
lines in a text file.
'''

fname = input("Enter file name: ")
try:
    num_lines = 0
    with open(fname, 'r') as f:
        for line in f:
            num_lines += 1
    print("Number of lines:")
    print(num_lines)
except FileNotFoundError:
    print("File not found.")
    
