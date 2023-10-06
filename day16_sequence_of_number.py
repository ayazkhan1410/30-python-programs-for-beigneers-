
'''Day 16 of '30 days of 30
   Programs challenege '''

'''   
Write a Python function to find
the maximum and minimum numbers 
from a sequence of numbers.
Note: Do not use built-in functions.
'''
def func(numbers):
    if not numbers:
        return None,None
    
    max_number = numbers[0]
    min_number = numbers[0]
    
    for num in numbers:
        if num > max_number:
            max_number = num
        elif num < min_number:
            min_number = num
    return max_number,min_number


numbers = [10, 5, 7, 20, 3, 15]
max_value, min_value = func(numbers)
print("Maximum: ", max_value)
print("Minimum: ", min_value)

