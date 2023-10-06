'''
Day 18 of '30 days of 30
 Programs challenege '''
   
'''
Check if a String
is Palindrome or Not
'''

def func(name):
    return name == name[::-1]

name = input("Enter scentence: ")

if func(name):
    print(f"{name} is Palindrome")
else:
     print(f"{name} is not Palindrome")