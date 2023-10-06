'''
Day 19 of '30 days of 30
 Programs challenege '''
'''


Check number is perfect
or not

a number that is equal
to the sum of its 
positive divisors
'''

number = int(input("Enter Number: "))
sum = 0
for i in range(1,number):
    if number%i==0:
        sum+=i
if number==sum:
    print(f"{number} is perfect number")
else:
    print(f"{number} is not perfect number")

