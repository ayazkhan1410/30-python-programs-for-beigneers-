'''Day 7 of '30 days of 30
   Programs challenege '''

                      
# [1, -4, 7, 12] => 1+7+12 = 20. 
# return the sum of all of the positive ones
# note use list comprehension for this task

def func(n):
    return sum([num for num in n if num>0])

list1 = [1, -4, 7, 12]
result = func(list1)
print(f"Sum : {result}")

