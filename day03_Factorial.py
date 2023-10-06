'''Day 3 of '30 days of 30
   Programs challenege '''

# Take factorial of any number
# use Recursion

def fact(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * fact(n-1)

user_input = int(input('Enter Number : '))
result = fact(user_input)
print(f"Factorial of {user_input} is {result} ")

l