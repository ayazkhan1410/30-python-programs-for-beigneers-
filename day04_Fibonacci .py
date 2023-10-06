'''Day 4 of '30 days of 30
   Programs challenege '''
   
# print Fibonacci Sequence
#using recursion

def fab(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fab(n-1) + fab(n-2)


user_input = int(input('Enter Number : '))
res = fab(user_input)
print('Result : ', res)